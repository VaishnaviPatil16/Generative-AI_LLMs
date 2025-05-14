from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(temperature=0.5,max_new_tokens=100)
)

prompt = PromptTemplate(
    template= "Generate 5 interetsing facts about {topic}",
    input_variables=["topic"]
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

chain = prompt | model |parser  

result= chain.invoke({"topic":"Cricket"})
print(result)


#Visualize Chain
chain.get_graph().print_ascii()