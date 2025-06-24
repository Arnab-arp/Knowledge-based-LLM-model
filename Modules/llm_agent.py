# LLM prompt + response handling

# My reference : https://ai.google.dev/gemini-api/docs/quickstart

import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv() # loading the .env file for the API key

# print(os.getenv('OPENAI_API_KEY'))

class MiniLLM:
    def __init__(self):
        self.model_name = "gemini-1.5-flash"
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    def _completeRessponse(self, prompt, temp):
        system_instruction_text = "You are a technical research assistant."

        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[{"role": "user", "parts": [{"text": prompt}]}], # Only user content here
            config=types.GenerateContentConfig(
                temperature=temp,
                system_instruction=system_instruction_text
            )
        )
        return response.text

    def generate_response(self, query, contexts, model_temp=0.0):
        context_str = '\n\n'.join(
            f"[Source: {context['file_id']}] {context['text_info']}"
            for context in contexts
        )

        prompt = f'''
You MUST only use the context provided to answer the following query. Do not make up facts outside the context.
Format response as bullet points, with sources. If the answer is not in the context, 
say "I don't have much imformation about this" or "I don't know" in appropriate context.

Context:
{context_str}

Query: {query}
Answer:
'''     
        response = self._completeRessponse(prompt=prompt, temp=model_temp)
        return response


if __name__ == '__main__':
    from appretriever import VectorRetriever
    
    my_query = 'Sunbeam'
    contexts = VectorRetriever().retrieve(
        query=my_query
    )
    agent_response = MiniLLM().generate_response(query=my_query, contexts=contexts)
    print(agent_response)