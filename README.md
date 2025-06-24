# Knowledge Base LLM Agent using Google Gemini-1.5-Flash model

A micro-agent that ingests user queries, retrieves context from a knowledge base, and generates structured, source-cited responses while preventing hallucinations.

---

## **Features**

- **Semantic search** with FAISS vector database  
- **Hallucination prevention** through strict context grounding  
- **Source-cited responses** with document references  
- **SQLite query logging**  
- **FastAPI REST endpoint**  
- **Google Gemini integration**

---

## **Python Version**

This code is written in **Python 3.11.9**

---

## **Setup and Installation**

### 1. Clone the repository

```bash
git clone https://github.com/Arnab-arp/Knowledge-based-LLM-model.git
cd Knowledge-based-LLM-model
```

### 2. Install dependencies

> **Note:** It is highly recommended to use a virtual environment.

```bash
pip install -r requirements.txt
```

---

## **File Requirements**

1. Create a `.env` file in the project root.
2. Add your Google Gemini API key:

```env
GEMINI_API_KEY='Your Google Gemini API key'
```

> **Tip:** Head over to [AI Studio API Key](https://aistudio.google.com/apikey) to obtain your key.

---

## **How to Run the Project**

1. **Activate** your virtual environment (if using one):

   ```bash
   .venv\Scripts\activate
   ```

2. **Start** the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

---

## **How to Test**

Use **Postman** or any API client:

1. **Method:** `POST`  
2. **URL:** `http://localhost:8000/query`  
3. **Headers:**

   | Key             | Value                |
   | --------------- | -------------------- |
   | Content-Type    | application/json     |

4. **Body:** Select **raw** → **JSON**, then send:

   ```json
   {
     "query": "Why GraphQL?"
   }
   ```

5. **Response:** You will receive a structured, source-cited JSON response in the response area.

---
