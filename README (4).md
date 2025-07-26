# Conversational AI Backend

This repository contains the backend service for the **Conversational AI agent**, implemented with **FastAPI**, **PostgreSQL**, and **Groq LLM API**.  

The service stores e-commerce data, maintains conversation history for multiple users and sessions, and integrates with an LLM to generate AI-powered responses.

---

## **Features**

- **E-commerce Data:** Load product & customer data from CSV files.
- **Multi-user Conversations:** Robust schema to store conversation histories with multiple sessions.
- **Chat API:** `/api/chat` endpoint stores user messages and AI responses.
- **LLM Integration:** Uses [Groq API](https://console.groq.com/) for intelligent replies.

---

## **Project Structure**

```
backend/
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── main.py
│   └── llm_integration.py
├── data/
│   ├── products.csv
│   └── customers.csv
├── load_data.py
├── requirements.txt
└── README.md
```

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/ritikkumar64/Conversational-AI.git
cd Conversational-AI/backend
```

### **2. Create Virtual Environment & Install Dependencies**
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### **3. Set up PostgreSQL Database**
```bash
createdb conversational_ai
```

### **4. Load Data from CSV**
```bash
python load_data.py
```

### **5. Run the FastAPI Server**
```bash
uvicorn app.main:app --reload
```

---

## **Environment Variables**

Create a `.env` file inside the `backend/` folder and add:
```
GROQ_API_KEY=your_api_key_here
```

---

## **API Usage**

### **POST /api/chat**

**Request:**
```json
{
  "message": "Show me available products",
  "conversation_id": null
}
```

**Response:**
```json
{
  "conversation_id": 1,
  "response": "Here are some products..."
}
```

---

## **Commit History**

- `feat: Complete Milestone 2 Database Setup`
- `feat: Complete Milestone 3 Data Schemas`
- `feat: Complete Milestone 4 Core Chat API`
- `feat: Complete Milestone 5 LLM Integration`

---

## **License**

This project is licensed for educational and development use.  
