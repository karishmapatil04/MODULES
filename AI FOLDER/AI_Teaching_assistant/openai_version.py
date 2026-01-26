import streamlit as st
from openai import OpenAI
import config

# Initialize the OpenAI client
client = OpenAI(api_key=config.OPENAI_API_KEY)

# Function to generate AI response from OpenAI
def generate_response(prompt, temperature=0.3):
    """Generate a response from OpenAI API."""
    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt,
            temperature=temperature
        )
        return response.output_text
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI Setup
def setup_ui():
    st.title("AI Teaching Assistant")
    st.write("Welcome! You can ask me anything about various subjects, and I'll provide an answer.")

    # Get user input (question)
    user_input = st.text_input("Enter your question here:")

    if user_input:
        # Show the user's input
        st.write(f"**Your question:** {user_input}")
        
        # Generate AI response from OpenAI
        response = generate_response(user_input)
        
        # Display AI's response
        st.write(f"**AI's answer:** {response}")
    else:
        st.write("Please enter a question to ask.")

# Main function to run the app
def main():
    setup_ui()

if __name__ == "__main__":
    main()