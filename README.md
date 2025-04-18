# 🧠 AI-Based Hourly Sheet Tracking System

This project is an AI-enhanced solution designed to optimize manufacturing performance by tracking hourly sheet data, predicting machine downtime, and detecting anomalies in real-time. The system leverages machine learning models (Random Forest) and provides an interactive interface using Streamlit.

---

## 📊 Data Flow Diagram

The following flowchart visually represents how data moves through the system:

![Dataflow Diagram](./A_flowchart_diagram_titled_"AI-Based_Hourly_Sheet_.png)

---

## 🛠 System Components

### 1. Operator Input (Frontend)
- Machine ID
- Operator ID
- Shift
- Product Type
- Units Produced
- Number of Defects

The input is collected using a **Streamlit web application**.

---

### 2. Preprocessing
- Encodes categorical variables (e.g., Machine, Shift).
- Formats inputs into a structured DataFrame.
- Adds features like previous defects and rolling averages.

---

### 3. AI Model (Backend)
- **Random Forest Classifier** trained on historical manufacturing data.
- Predicts the **risk of downtime** with associated confidence.
- Can be extended with anomaly detection (e.g., Isolation Forest).

---

### 4. Output Prediction
- Displayed in the Streamlit UI.
- Example Output:


---

### 5. Feedback Loop (Optional)
- Logs input data and predictions.
- Can be used for model retraining and continuous improvement.

---

## 🚀 Features

- 🔍 Predict machine downtime using Random Forest
- 💬 Conversational AI assistant (optional feature)
- ⚙️ Real-time monitoring via Streamlit
- 📈 Anomaly detection (optional integration)
- 🧪 Model accuracy: ~81%

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
