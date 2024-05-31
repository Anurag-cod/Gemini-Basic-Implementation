from dotenv import load_dotenv  # Importing the load_dotenv function to load environment variables
load_dotenv()  # Loading environment variables from a .env file if present

import streamlit as st  # Importing the Streamlit library for building web apps
import google.generativeai as genai  # Importing the Google Generative AI library
import os  # Importing the os module for interacting with the operating system

# Configuring the Google Generative AI library with the API key loaded from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initializing the Generative Model from the Google Generative AI library
model = genai.GenerativeModel('gemini-pro') 

# Function to generate responses based on the question provided
def get_responses(question):
    response = model.generate_content(question)
    return response.text

# Setting up the title of the Streamlit web app
st.title("Question Answering App")

# Adding a text input field for users to input their questions
input = st.text_input("Enter your question here:")

# Adding a button for users to submit their questions
submit = st.button("Ask the question")

# Handling the user input and generating a response upon clicking the submit button
if submit:
    response = get_responses(input)  # Generating response based on the user's question
    st.subheader("The response is")  # Adding a subheader to display the response
    st.write(response)  # Displaying the generated response
