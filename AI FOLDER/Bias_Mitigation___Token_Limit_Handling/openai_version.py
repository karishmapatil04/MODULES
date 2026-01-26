from openai import OpenAI
import config

# Initialize OpenAI client
client = OpenAI(api_key=config.OPENAI_API_KEY)

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


def bias_mitigation_activity():
    """Conducts the bias mitigation activity."""
    print("\n=== BIAS MITIGATION ACTIVITY ===\n")
    
    prompt = input("Enter a prompt to explore bias (e.g., 'Describe the ideal doctor'): ")
    initial_response = generate_response(prompt)
    print(f"\nInitial AI Response:\n{initial_response}")
    
    modified_prompt = input(
        "Modify the prompt to make it more neutral (e.g., 'Describe the qualities of a doctor'): "
    )
    modified_response = generate_response(modified_prompt)
    print(f"\nModified AI Response (Neutral):\n{modified_response}")


def token_limit_activity():
    """Conducts the token limit activity."""
    print("\n=== TOKEN LIMIT ACTIVITY ===\n")
    
    long_prompt = input(
        "Enter a long prompt (more than 300 words, e.g., a detailed story or description): "
    )
    long_response = generate_response(long_prompt)
    print(f"\nResponse to Long Prompt:\n{long_response[:500]}...")
    
    short_prompt = input("Now, condense the prompt to be more concise: ")
    short_response = generate_response(short_prompt)
    print(f"\nResponse to Condensed Prompt:\n{short_response}")


def run_activity():
    """Runs the entire activity for the user."""
    print("\n=== AI Learning Activity ===")
    
    activity_choice = input(
        "Which activity would you like to run? (1: Bias Mitigation, 2: Token Limits): "
    )

    if activity_choice == "1":
        bias_mitigation_activity()
    elif activity_choice == "2":
        token_limit_activity()
    else:
        print("Invalid choice. Please choose either 1 or 2.")


if __name__ == "__main__":
    run_activity()
