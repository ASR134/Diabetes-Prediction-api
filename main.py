from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Literal, Annotated
from fastapi.responses import JSONResponse
import pandas as pd
import pickle
from fastapi.middleware.cors import CORSMiddleware


# import ml model
with open("trained_model.sav","rb") as f:
    model = pickle.load(f)
    

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
    )




# pydantic model

class user_input(BaseModel):
    
    Pregnancies : Annotated[int, Field(...,description="No. of Pregnancies")]
    Glucose : Annotated[int, Field(...,description="Glucose level",gt=0)]
    BloodPressure : Annotated[int, Field(...,description="BloodPressure Level",gt=0)]
    SkinThickness : Annotated[int, Field(...,description="SkinThickness")]
    Insulin : Annotated[int, Field(...,description="Insulin level")]
    BMI : Annotated[float, Field(...,description="Body Mass Indes",gt=0,lt=50)]
    DiabetesPedigreeFunction : Annotated[float, Field(...,description="Diabetes Pedigree function")]
    Age : Annotated[int, Field(...,description = "Age",gt=0,lt=120)]
    
    
@app.post("/predict")
def prediction(data : user_input):# pydantic validates the input send by client and create an instance of pydantic model and 
# assigns it to data. so data parameter is a pydantic model obj.
    
     input_df = pd.DataFrame([{
         
         "Pregnancies":data.Pregnancies,
         "Glucose":data.Glucose,
         "BloodPressure":data.BloodPressure,
         "SkinThickness":data.SkinThickness,
         "Insulin":data.Insulin,
         "BMI":data.BMI,
         "DiabetesPedigreeFunction":data.DiabetesPedigreeFunction,
         "Age":data.Age
         }])
     
     prediction = model.predict(input_df)[0]
     if prediction==0:
         result = "Diabetic"
     else : 
         result = "Non Diabetic"
     
     return JSONResponse(status_code=200, content={"predicted category " : result})
    

     
         
     
    
    
    
    
    
    
    
    
    