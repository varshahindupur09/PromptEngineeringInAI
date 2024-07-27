# Movie Making Mania using Gemini Vision Pro
This project is a Chatbot designed to work with specific data provided to it. Gemini Vision Pro captures and stores this data, enabling the chatbot to assist users with their questions on the topic.

## Table of Contents
* Introduction
* Installation
* Extract Data Using Gemini Vision Pro
*  hatbot to Interact with Users

## Objective
Develop a domain-specific chatbot that combines the strengths of a Large Language Model (LLM) for understanding and processing natural language queries with the efficiency of a vector database for data storage and retrieval. The chatbot will provide personalized recommendations in a specific domain of interest.

## Assignment Description
You will develop a chatbot that interacts with users to understand their needs and preferences, generating personalized recommendations using Retrieval-Augmented Generation (RAG). The recommendations should be based on user inputs and must be accurate to the user's stated preferences, using data from the vector store only.

## Key Features of this ChatBot:
1. User Interaction: The chatbot allows users to input their preferences and needs through a conversational Gradio interface.
2. RAG-Based Recommendations: Generating recommendations using RAG based on the user's input.
3. Intelligent Responses: Providing relevant and accurate responses to user queries and requests. This is taken care of by integrating RAG.
4. Pre-existing Data: Recommendations comes only from the existing list of data available in the system, not sourced from the internet.
5. Backend Integration: Utilizing LangChain for managing the flow of interactions. Storing details and descriptions in a vector database.
6. Data Fetching: Fetching the top K (K <= 3) data entries based on user descriptions using similarity search in the vector database.
7. Prompt Engineering for Movie Making Data: Using prompt engineering to generate mock data, which will be stored in the vector database for similarity search.

## The Chatbot Images showing its answering skills for the given information.

<img width="1038" alt="image" src="https://github.com/user-attachments/assets/6aae1c5d-51c1-472e-8343-9afee11ae433">

This image shows user asking the question - What is film preservation and why does it matter?

## The Chatbot Images showing its answering skills for the non-related information.

<img width="979" alt="image" src="https://github.com/user-attachments/assets/07087d1b-d682-4f9e-9051-b08a503891b9">

This image shows user asking the question - Why is the sky blue?

## Gemini Vector Database deployed:
<img width="1180" alt="image" src="https://github.com/user-attachments/assets/63eebbee-18e3-449f-951d-0f54ef3cfdff">

## Workflow:
### Data Collection and Preprocessing:
Collect movie data including titles, genres, ratings, and descriptions.
Clean and preprocess the data to ensure it is in a suitable format for generating embeddings.

### Embedding Generation:
Use a pre-trained embedding model to generate embeddings for movie titles and descriptions.
Store these embeddings in a vector database for efficient retrieval.

### Vector Database Integration:
Initialize and configure the vector database.
Index the movie embeddings for fast similarity searches.

### LangChain Integration:
Set up LangChain to manage the interaction flow between the user inputs, LLM responses, and vector database retrievals.
Define the prompts and response generation logic.

### Retrieval-Augmented Generation (RAG) Workflow:
User inputs a query through the Streamlit interface.
LangChain processes the query and retrieves relevant movie embeddings from the vector database.
The LLM uses the retrieved embeddings to generate a natural language response recommending movies.

### Streamlit Interface
Develop a user-friendly web interface for inputting queries and displaying recommendations.
Implement input fields and submit buttons for user interaction.

## Summary
This project demonstrates how to build a Movie Making Chatbot system using RAG with LLMs, LangChain, and a vector database. Users can input their queries through a Streamlit interface, and the system retrieves relevant movie embeddings from a vector database to generate recommendations using a language model. The setup integrates various components to provide an efficient and scalable solution for personalized movie recommendations.

## Youtube Video: https://youtu.be/HRHBa0tjPbU

## Report PDF:
It is available in my Repository.
Link: https://github.com/varshahindupur09/PromptEngineeringInAI/blob/main/RAG_CHATBOT/PreviousReportChatbotRAG.pdf
Link: https://github.com/varshahindupur09/PromptEngineeringInAI/blob/main/RAG_CHATBOT/ReportChatbotRAG.pdf

