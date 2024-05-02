import os
import google.generativeai as genai

from dotenv import load_dotenv

# load the api key from the environment variables for security
load_dotenv()
GEM_API_KEY = os.getenv('GEM_API_KEY')
genai.configure(api_key=GEM_API_KEY)

ticket_title = input("What is the title of the ticket? ")

# create the gemini model and input the ticket title with a detailed prompt 
gemini = genai.GenerativeModel('gemini-pro')
chat = gemini.start_chat(history=[])

prompt = f"Since you are a master with requirements engineering, can you generate a jira ticket for the given ticket title: {ticket_title}. The response should output a completed scope for the task that could include descriptions, acceptance criteria, sub-tasks, a user story section, assumptions, and any other relevant details. Also if there are any ambiguities then feel free to ask"

# NOTE that we are using a chat-loop so that we can let the LLM handle for lack of clarity
while True:
    gem_response = chat.send_message(prompt)
    print(gem_response.text)

    print("If you are satisfied with the response then press 'ctrl + c'")
    prompt = input("Still not satisfied with response? Then send a follow up prompt here: ")