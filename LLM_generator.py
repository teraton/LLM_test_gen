import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()  # take environment variables from .env.


# todo , parametrize
function_code = """
def sum_numbers(a, b):
    return a + b
"""

# Set up your OpenAI API key

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def generate_unit_tests(function_code):
    # Define the prompt
    prompt = f"Generate unit tests for the following function:\n\n{function_code}\n\nPotential unit tests. these should be in the following JSON format where the JSON object contains the the parameters in params field and the expected result in expected_result field."

    # Call the completion endpoint of the ChatGPT API
    chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are an expert system in creating standardized unit test answers to the questions provided by the user. try to generate varied responses to the queries. as you are an expert in testing you take into account boundary value analysis and other testing best practices. answer with a JSON object called tests, which contains only the endpoint field which is the name of the function,  params and expected_result fields for the test cases. params is a list object."},
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo",
    )

    # Extract the generated tests from the response
    return (chat_completion.choices[0].message.content)

