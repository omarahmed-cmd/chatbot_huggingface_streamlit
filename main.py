import streamlit as st
import asyncio
from transformers import pipeline

# Create a placeholder for the pipeline
text_gen_pipe = None

def load_model():
    return pipeline("text2text-generation", model="declare-lab/flan-alpaca-gpt4-xl")

async def generate_response(prompt, text_gen_pipe):
    response = text_gen_pipe(prompt, max_length=250)  # Adjust max_length as needed
    return response[0]['generated_text']

st.title('Chatbot')
st.markdown('---')
prompt = st.text_input("Enter your question:")

# Load the model only once, when the app starts
if text_gen_pipe is None:
    text_gen_pipe = load_model()



if prompt:
    response = asyncio.run(generate_response(prompt, text_gen_pipe))
    st.write(response)


