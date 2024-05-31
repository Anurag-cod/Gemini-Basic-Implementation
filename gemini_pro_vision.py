from dotenv import load_dotenv  # Importing the load_dotenv function to load environment variables
load_dotenv()  # Loading environment variables from a .env file if present

import streamlit as st  # Importing the Streamlit library for building web apps
import google.generativeai as genai  # Importing the Google Generative AI library
import os  # Importing the os module for interacting with the operating system
from PIL import Image

# Configuring the Google Generative AI library with the API key loaded from environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initializing the Generative Model from the Google Generative AI library
model = genai.GenerativeModel('gemini-pro') 

# Function to generate responses based on the question provided
def get_responses(input,image):
    if input!="":
        response = model.generate_content([input,image])
    else:
        response=model.generate_content(image)
    return response.text

# Setting up the title of the Streamlit web app
st.title("Gemini image App")

# Adding a text input field for users to input their questions
input = st.text_input("Enter your question here:")


# Use st.file_uploader() to upload an image file
image_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Check if an image file was uploaded
if image_file is not None:
    # Display the uploaded image
    image=Image.open(image_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

# Adding a button for users to submit their questions
submit = st.button("Tell about the image")

# Handling the user input and generating a response upon clicking the submit button
if submit:
    response = get_responses(input,image)  # Generating response based on the user's question
    st.subheader("The response is")  # Adding a subheader to display the response
    st.write(response)  # Displaying the generated response
