import openai
import config

# Initialize OpenAI client
client = openai.OpenAI(api_key="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")

def generate_response(prompt, temperature=0.3):
    """Generate a response from OpenAI API."""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # lightweight & fast
            temperature=temperature,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


def reinforcement_learning_activity():
    """Conducts the reinforcement learning activity."""
    print("\n=== REINFORCEMENT LEARNING ACTIVITY ===\n")

    prompt = input("Enter a prompt for the AI model (e.g., 'Describe the lion'): ")
    initial_response = generate_response(prompt)
    print(f"\nInitial AI Response:\n{initial_response}")

    rating = int(input("\nRate the response from 1 (bad) to 5 (good): "))
    feedback = input("Provide feedback for improvement: ")

    # Simulated improvement (no real fine-tuning here)
    improved_response = (
        f"{initial_response}\n\n"
        f"🔁 Improved using your feedback:\n{feedback}"
    )

    print(f"\nImproved AI Response:\n{improved_response}")

    
def role_based_prompt_activity():
    """Conducts the role-based prompts activity."""
    print("\n=== ROLE-BASED PROMPTS ACTIVITY ===\n")

    category = input("Enter a category (e.g., science, history, math): ")
    item = input(f"Enter a specific {category} topic: ")

    teacher_prompt = f"You are a teacher. Explain {item} in simple terms."
    expert_prompt = f"You are an expert in {category}. Explain {item} in a detailed, technical manner."

    teacher_response = generate_response(teacher_prompt)
    expert_response = generate_response(expert_prompt)

    print(f"\n--- Teacher's Perspective ---\n{teacher_response}")
    print(f"\n--- Expert's Perspective ---\n{expert_response}")

   

def run_activity():
    """Runs the entire activity."""
    print("\n=== AI Learning Activity ===")

    choice = input(
        "Which activity would you like to run?\n"
        "1: Reinforcement Learning\n"
        "2: Role-Based Prompts\n"
        "Enter choice: "
    )

    if choice == "1":
        reinforcement_learning_activity()
    elif choice == "2":
        role_based_prompt_activity()
    else:
        print("❌ Invalid choice.")


if __name__ == "__main__":
    run_activity()
