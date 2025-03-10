from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "tell me about virat kohli"

doc_embeddings = embedding.embed_documents(documents)
query_embeddings = embedding.embed_query(query)

scores = cosine_similarity([query_embeddings],doc_embeddings)
index,score = sorted(list(enumerate(scores)), key= lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is:", score)
#[0.6630,0.3486,0.3434,0.3961,0.3951]- we can see first vector result is high so the answer is from first vector. This is individual vector representation.