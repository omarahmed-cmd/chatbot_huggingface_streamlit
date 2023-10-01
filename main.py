# import streamlit as sl
# from transformers import pipeline

# # Create a placeholder for the pipeline
# text_gen_pipe = None

# sl.title('Owais Chatbot') 
# sl.markdown('---')

# prompt = sl.text_input("Enter your question:")

# pipe = pipeline("text2text-generation", model="declare-lab/flan-alpaca-gpt4-xl")
# respond = pipe(prompt)
# sl.write(respond[0]['generated_text'])

# import streamlit as st
# from transformers import pipeline

# # Create a placeholder for the pipeline
# text_gen_pipe = None

# st.title('Owais Chatbot')
# st.markdown('---')

# prompt = st.text_input("Enter your question:")

# if prompt:
#     if text_gen_pipe is None:
#         text_gen_pipe = pipeline("text2text-generation", model="declare-lab/flan-alpaca-gpt4-xl")

#     respond = text_gen_pipe(prompt, max_length=230)  # Increase max_length to generate longer responses
#     st.write(respond[0]['generated_text'])

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


