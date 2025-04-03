from pyexpat.errors import messages
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                          task="text-generation")
model = ChatHuggingFace(llm=llm)

messages =[
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about Langchain")
]
result = model.invoke(messages)
messages.appendAIMessage(content=result.content)
print(messages)