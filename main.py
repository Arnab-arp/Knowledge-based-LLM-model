# FastAPI Implementation

from Modules.appretriever import VectorRetriever
from Modules.logger import QueryLog
from Modules.llm_agent import MiniLLM
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


vec_ret = VectorRetriever()
mini_agent = MiniLLM()
log = QueryLog()
app = FastAPI()

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    agent: str
    sources: list[str]


# Building API
@app.post('/query', response_model=QueryResponse)

async def queryHandeler(request: QueryRequest):
    user_query = request.query
    relevent_contexts = vec_ret.retrieve(query=user_query) # sending the query to get relevent contexts
    srcs = [ctx["file_id"] for ctx in relevent_contexts]
    agent_response = mini_agent.generate_response(query=user_query, contexts=relevent_contexts)
    log.log_query(
        query=user_query,
        answer=agent_response,
        sources=srcs
        )
    return {
        "agent": agent_response,
        "sources": srcs
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)