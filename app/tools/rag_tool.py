
import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("emails")

def add_email(id, text):
    collection.add(documents=[text], ids=[id])

def search(query):
    return collection.query(query_texts=[query], n_results=3)
