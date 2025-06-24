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

#**Demo**
1. ![image](https://github.com/user-attachments/assets/4d72eb84-5894-402b-b414-7914379c39f0)
   **Input**
```bash
   {
       "query": "Explain what is GraphQL and why it is important?"
   }
```
   **Output**
```bash
   {
       "agent": "* GraphQL is a query language and server-side runtime for APIs that provides clients with precisely the data they request, offering an alternative to REST.  It allows fetching data from multiple sources with a single API call, making APIs faster, more flexible, and developer-friendly.  [source_data_0.txt]\n\n* GraphQL's importance stems from its efficiency in retrieving only the necessary data, preventing under-fetching or over-fetching.  It simplifies the process of retrieving data for related objects simultaneously, reducing the number of API calls.  This makes it a highly efficient API type for queries. [source_data_6.txt]\n\n*  GraphQL's query language allows developers to control the structure of the API response and provides broad access to schema objects and properties, offering a flexible way to present digital resources. [source_data_2.txt]\n\n*  GraphQL offers excellent data modeling, allows retrieval of required data in a single API call, provides great tooling (easy client SDK generation), and features self-documentation. [source_data_8.txt]\n",
       "sources": [
           "source_data_0.txt",
           "source_data_2.txt",
           "source_data_6.txt",
           "source_data_9.txt",
           "source_data_8.txt"
       ]
   }
```

2. ![image](https://github.com/user-attachments/assets/e5ed65c1-8136-4747-8da3-cf3145cdf22d)
   **Input**
```bash
{
    "query": "Who is Walter White?"
}
```

   **Output**
```bash
{
    "agent": "I don't know.\n",
    "sources": [
        "source_data_7.txt",
        "source_data_2.txt",
        "source_data_8.txt",
        "source_data_9.txt",
        "source_data_5.txt"
    ]
}
```
