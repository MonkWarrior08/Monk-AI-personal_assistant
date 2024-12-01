from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the client
client = OpenAI()  # This will now find the OPENAI_API_KEY from .env

def chat_with_assistant(assistant_id, user_message):
    # Create a thread
    thread = client.beta.threads.create()
    
    # Add a message to the thread
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_message
    )
    
    # Run the assistant and wait for completion
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id
    )
    
    # Wait for run to complete
    while run.status in ["queued", "in_progress"]:
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
    
    # Get the messages
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    
    # Print the latest assistant message
    for message in messages.data:
        if message.role == "assistant":
            print(message.content[0].text.value)
            break

# Example conversation loop
def main():
    assistant_id = ""  # Replace with your assistant ID
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            break
        print("\nAssistant: ", end="")
        chat_with_assistant(assistant_id, user_input)

if __name__ == "__main__":
    main()
