from openai import OpenAI
import config
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Initialize OpenAI client
client = OpenAI(api_key=config.OPENAI_API_KEY)

# Function to generate AI response
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

# Step 1: Get essay details
def get_essay_details():
    print(Fore.CYAN + "\n=== AI Writing Assistant ===\n")

    topic = input(Fore.YELLOW + "What is the topic of your essay? ")
    essay_type = input(
        Fore.YELLOW
        + "What type of essay are you writing? (Argumentative, Expository, Descriptive, Persuasive, Analytical): "
    )

    print(Fore.GREEN + "\nSelect the desired essay word count:")
    print(Fore.GREEN + "1. 300 words")
    print(Fore.GREEN + "2. 900 words")
    print(Fore.GREEN + "3. 1200 words")
    print(Fore.GREEN + "4. 2000 words")

    word_count_choice = input(Fore.YELLOW + "Enter choice number: ")
    word_count_dict = {"1": "300", "2": "900", "3": "1200", "4": "2000"}
    length = word_count_dict.get(word_count_choice, "300")

    target_audience = input(Fore.YELLOW + "Target audience: ")
    specific_points = input(Fore.YELLOW + "Specific points to include: ")

    stance = input(Fore.YELLOW + "Your stance (For / Against / Neutral): ")
    references = input(Fore.YELLOW + "Any sources or references?: ")
    writing_style = input(Fore.YELLOW + "Preferred writing style (Formal, Academic, Creative): ")

    outline_needed = input(
        Fore.YELLOW + "Would you like an outline first? (Yes/No): "
    ).lower()

    return {
        "topic": topic,
        "essay_type": essay_type,
        "length": length,
        "target_audience": target_audience,
        "specific_points": specific_points,
        "stance": stance,
        "references": references,
        "writing_style": writing_style,
        "outline_needed": outline_needed,
    }

# Step 2: Generate Essay Content
def generate_essay_content(details):
    temperature = float(
        input(
            Fore.YELLOW
            + "Enter temperature (0.2 = structured, 0.7 = creative): "
        )
    )

    introduction_prompt = (
        f"Write an introduction for a {details['essay_type']} essay "
        f"on '{details['topic']}' with a {details['stance']} stance."
    )

    introduction = generate_response(introduction_prompt, temperature)
    print(Fore.CYAN + "\n=== Generated Introduction ===")
    print(Fore.GREEN + introduction)

    body_style = input(
        Fore.YELLOW
        + "Write body step-by-step or full draft? (Step-by-step / Full draft): "
    ).lower()

    if body_style == "full draft":
        body_prompt = (
            f"Write a detailed {details['essay_type']} essay on "
            f"'{details['topic']}' with a {details['stance']} stance."
        )
        body = generate_response(body_prompt, temperature)
        print(Fore.CYAN + "\n=== Generated Full Body ===")
        print(Fore.GREEN + body)
    else:
        body_step_prompt = (
            f"Write step-by-step arguments for an essay on "
            f"'{details['topic']}' with a {details['stance']} stance. "
            "Include reasoning and examples."
        )
        body_step = generate_response(body_step_prompt, temperature)
        print(Fore.CYAN + "\n=== Generated Step-by-Step Body ===")
        print(Fore.GREEN + body_step)

    conclusion_prompt = (
        f"Write a conclusion for a {details['essay_type']} essay "
        f"on '{details['topic']}' with a {details['stance']} stance."
    )
    conclusion = generate_response(conclusion_prompt, temperature)
    print(Fore.CYAN + "\n=== Generated Conclusion ===")
    print(Fore.GREEN + conclusion)

# Step 3: Feedback and Refinement
def feedback_and_refinement():
    satisfaction = input(
        Fore.YELLOW + "Rate the essay (1–5 stars): "
    )

    if satisfaction != "5":
        feedback = input(
            Fore.YELLOW + "How can we improve it?: "
        )
        print(
            Fore.CYAN
            + f"\nThank you! We'll refine the essay using your feedback: {feedback}"
        )
    else:
        print(Fore.CYAN + "\nGreat! Glad you're satisfied.")

# Main Function
def run_activity():
    print(Fore.CYAN + "\nWelcome to the AI Writing Assistant!")

    details = get_essay_details()
    generate_essay_content(details)
    feedback_and_refinement()

# Run the program
if __name__ == "__main__":
    run_activity()
