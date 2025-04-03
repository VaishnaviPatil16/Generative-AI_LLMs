#Static Prompt
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
# import streamlit as st


# load_dotenv()

# llm =HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#       task="text-generation")

# model = ChatHuggingFace(llm=llm)

# st.header('Reasearch Tool')
# user_input= st.text_input('Enter your prompt')

# if st.button('Summarize'):
#     result = model.invoke(user_input)
#     st.write(result.content)

# Enter your prompt: Summariza attention all you need reserach paper.
# Enter your prompt: Summariza word2 vec reserach paper.Static 

#Static prompt is not recommended as if user enter some wrong research paper name then model will hallucinate it. 


#Dynamic Prompt: We can take key values from user and will fill it in the prompt.
# 
# -------------------------
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
# import streamlit as st
# from langchain_core.prompts import PromptTemplate,load_prompt

# load_dotenv()

# llm =HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#       task="text-generation")

# model = ChatHuggingFace(llm=llm)

# st.header('Reasearch Tool')
# paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

# style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

# length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# template = PromptTemplate(
#     template="""
#      "\nPlease summarize the research paper titled \"{paper_input}\" with the following specifications:\nExplanation Style: {style_input}  \nExplanation Length: {length_input}  \n1. Mathematical Details:  \n   - Include relevant mathematical equations if present in the paper.  \n   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  \n2. Analogies:  \n   - Use relatable analogies to simplify complex ideas.  \nIf certain information is not available in the paper, respond with: \"Insufficient information available\" instead of guessing.  \nEnsure the summary is clear, accurate, and aligned with the provided style and length.\n",
# """,
# input_variables= ['paper_input','style_input','length_input'], validate_template=True
 
# #  #It will check whether it has exact 3 (placeholders)inputs from user or not, 1. Default validation in  prompt template. (This feature is not in f string hence we use prompt teamplate, 2. Reusability by using prompt in different pages as through json file. 3.Langchain Ecosystem ))

# template = load_prompt('template.json')

# prompt =template.invoke({
#     'paper_input':paper_input,
#     'style_input':style_input,
#     'length_input':length_input
# })
# if st.button('Summarize'):
#     result = model.invoke(prompt)
#     st.write(result.content)

#-----------------Chain-------------

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

llm =HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
      task="text-generation")

model = ChatHuggingFace(llm=llm)

st.header('Reasearch Tool')
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')


if st.button('Summarize'):
   chain = template | model
   results = chain.invoke({'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input})
   st.write(results.content)


