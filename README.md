<div align="center">

# 🏥 Diabetes Prediction API

### *AI-Powered Health Risk Assessment*

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)](LICENSE)

**A powerful REST API that leverages machine learning to predict diabetes risk based on patient health metrics.**

[Features](#-features) • [Quick Start](#-quick-start) • [API Documentation](#-api-endpoints) • [Examples](#-usage-examples) • [Deployment](#-deployment)

---

</div>

## ✨ Features

<table>
<tr>
<td width="50%">

### ⚡ **Lightning Fast**
Built with FastAPI for exceptional performance and async support

### 🛡️ **Type-Safe**
Automatic validation with Pydantic ensures data integrity

</td>
<td width="50%">

### 🌐 **CORS Ready**
Pre-configured for seamless frontend integration

### 🤖 **ML-Powered**
Utilizes trained scikit-learn models for accurate predictions

</td>
</tr>
</table>

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- 🐍 **Python 3.7+**
- 📦 **pip** (Python package manager)

---

## 🚀 Quick Start

### 1️⃣ Clone the Repository

```bash
git clone <your-repository-url>
cd <repository-name>
```

### 2️⃣ Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Launch the API 🎉

```bash
uvicorn main:app --reload
```

<div align="center">

**🎊 Congratulations! Your API is now running! 🎊**

Access it at: **http://127.0.0.1:8000**

📚 Interactive Docs: **http://127.0.0.1:8000/docs**

</div>

---

## 📦 Dependencies

```txt
uvicorn      # ASGI server
pydantic     # Data validation
scikit-learn # Machine learning
numpy        # Numerical computing
pandas       # Data manipulation
fastapi      # Web framework
```

---

## 📁 Project Structure

```
📂 diabetes-prediction-api
 ┣ 📜 main.py                 # FastAPI application
 ┣ 📜 trained_model.sav       # Pre-trained ML model
 ┣ 📜 requirements.txt        # Python dependencies
 ┗ 📜 README.md              # Documentation
```

---

## 🎯 Running the API

Start the development server:

```bash
uvicorn main:app --reload
```

<div align="center">

### 🌟 Available Endpoints

| Service | URL |
|---------|-----|
| 🏠 **API Base** | http://127.0.0.1:8000 |
| 📖 **Swagger Docs** | http://127.0.0.1:8000/docs |
| 📘 **ReDoc** | http://127.0.0.1:8000/redoc |

</div>

---

## 🔌 API Endpoints

### `POST /predict` - Diabetes Risk Prediction

Analyzes patient health metrics to predict diabetes risk.

#### 📥 Request Body

```json
{
  "Pregnancies": 2,
  "Glucose": 120,
  "BloodPressure": 70,
  "SkinThickness": 20,
  "Insulin": 80,
  "BMI": 25.5,
  "DiabetesPedigreeFunction": 0.5,
  "Age": 33
}
```

#### 📊 Parameters

| Parameter | Type | Description | Constraints |
|-----------|:----:|-------------|:-----------:|
| `Pregnancies` | `int` | Number of pregnancies | Required |
| `Glucose` | `int` | Glucose level (mg/dL) | > 0 |
| `BloodPressure` | `int` | Blood pressure (mm Hg) | > 0 |
| `SkinThickness` | `int` | Triceps skin fold thickness (mm) | Required |
| `Insulin` | `int` | 2-Hour serum insulin (mu U/ml) | Required |
| `BMI` | `float` | Body Mass Index | 0 < BMI < 50 |
| `DiabetesPedigreeFunction` | `float` | Diabetes pedigree function | Required |
| `Age` | `int` | Age in years | 0 < Age < 120 |

#### 📤 Response

```json
{
  "predicted category ": "Non Diabetic"
}
```

<div align="center">

**Prediction Values**

| Result | Description |
|--------|-------------|
| ✅ `"Non Diabetic"` | Low risk of diabetes |
| ⚠️ `"Diabetic"` | High risk of diabetes |

</div>

#### 📡 Status Codes

| Code | Description |
|------|-------------|
| `200 OK` | ✅ Successful prediction |
| `422 Unprocessable Entity` | ❌ Invalid input data |

---

## 💻 Usage Examples

### 🔧 Using cURL

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "Pregnancies": 2,
    "Glucose": 120,
    "BloodPressure": 70,
    "SkinThickness": 20,
    "Insulin": 80,
    "BMI": 25.5,
    "DiabetesPedigreeFunction": 0.5,
    "Age": 33
  }'
```

### 🐍 Using Python

```python
import requests

url = "http://127.0.0.1:8000/predict"

patient_data = {
    "Pregnancies": 2,
    "Glucose": 120,
    "BloodPressure": 70,
    "SkinThickness": 20,
    "Insulin": 80,
    "BMI": 25.5,
    "DiabetesPedigreeFunction": 0.5,
    "Age": 33
}

response = requests.post(url, json=patient_data)
result = response.json()

print(f"Prediction: {result['predicted category ']}")
```

### 🌐 Using JavaScript

```javascript
const url = "http://127.0.0.1:8000/predict";

const patientData = {
  Pregnancies: 2,
  Glucose: 120,
  BloodPressure: 70,
  SkinThickness: 20,
  Insulin: 80,
  BMI: 25.5,
  DiabetesPedigreeFunction: 0.5,
  Age: 33
};

fetch(url, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify(patientData),
})
  .then(response => response.json())
  .then(result => {
    console.log("Prediction:", result["predicted category "]);
  })
  .catch(error => console.error("Error:", error));
```

---

## 📚 Interactive API Documentation

FastAPI automatically generates beautiful, interactive documentation:

<table>
<tr>
<td width="50%" align="center">

### 🎨 Swagger UI
**http://127.0.0.1:8000/docs**

✅ Interactive interface  
✅ Test endpoints live  
✅ View schemas  
✅ Execute requests  

</td>
<td width="50%" align="center">

### 📖 ReDoc
**http://127.0.0.1:8000/redoc**

✅ Clean documentation  
✅ Three-panel design  
✅ Easy navigation  
✅ Print-friendly  

</td>
</tr>
</table>

---

## 🤖 Model Information

The API leverages a **pre-trained machine learning model** (`trained_model.sav`) for diabetes prediction.

> ⚠️ **Important**: Ensure `trained_model.sav` is present in the project root directory before starting the API.

---

## 🌐 CORS Configuration

The API accepts requests from **any origin** by default.

> 🔒 **Production Tip**: Restrict CORS to specific domains for security:

```python
origins = [
    "http://localhost:3000",
    "https://yourdomain.com",
]
```

---

## ⚠️ Error Handling

The API provides **automatic validation** through Pydantic. Invalid requests return detailed error messages.

**Example Error Response:**

```json
{
  "detail": [
    {
      "loc": ["body", "Glucose"],
      "msg": "ensure this value is greater than 0",
      "type": "value_error.number.not_gt"
    }
  ]
}
```

<div align="center">

**Common Error Types**

| Error | Status Code | Description |
|-------|:-----------:|-------------|
| Validation Error | `422` | Invalid input parameters |
| Missing Field | `422` | Required field not provided |
| Type Mismatch | `422` | Wrong data type provided |

</div>

---

## 🚀 Deployment

### Production Checklist

- [ ] Remove `--reload` flag
- [ ] Configure specific CORS origins
- [ ] Use production ASGI server
- [ ] Set up environment variables
- [ ] Enable HTTPS/SSL
- [ ] Implement rate limiting
- [ ] Add logging and monitoring

### Production Server Setup

**Using Gunicorn with Uvicorn Workers:**

```bash
gunicorn main:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000
```

**Using Docker:**

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 🤝 Contributing

Contributions are **welcome**! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. 💍 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🎉 Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact


**Project Link**: [https://github.com/ASR134/diabetes-prediction-api](https://github.com/ASR134/diabetes-prediction-api)

---

## 🙏 Acknowledgments

<div align="center">

Built with ❤️ using

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)

</div>

---

<div align="center">

**⭐ Star this repo if you find it helpful! ⭐**

Made with 💙 by Aman Singh Rawat

</div>
