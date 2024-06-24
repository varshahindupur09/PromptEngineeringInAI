import streamlit as st
import requests
import json

# Function to get response from Ollama Gemma:2B
def get_llm_response(query):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "gemma:2b",
        "prompt": query
    }
    response = requests.post(url, json=payload, stream=True)
    print(response.text)

    # Process the streaming response
    full_response = ""

    for line in response.iter_lines():
        if line:
            json_line = json.loads(line.decode('utf-8'))
            full_response += json_line.get("response", "")
            if json_line.get("done"):
                break
    return full_response

# Streamlit app
st.title("Restaurant Menu Chatbot")
st.write("Ask about Food King restaurant menu and place pickup orders.")

query = st.text_input("Enter your query:")

if st.button("Submit"):
    response = get_llm_response(query)
    st.write("Response:")
    st.write(response)
