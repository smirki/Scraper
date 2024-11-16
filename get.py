import csv
import os
from groq import Groq

# Initialize Groq client
client = Groq(
    api_key="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"
)

# Sample CSV data
csv_data = """
function_title,exact_parameters,function_description
"add_expense", "amount: float, category: str, description: str", "Returns None. Adds an expense entry to the database with the given amount, category, and description."
"view_expenses", "start_date: str (YYYY-MM-DD), end_date: str (YYYY-MM-DD)", "Returns a list of expenses within the specified date range. Each expense is a dictionary with 'amount', 'category', and 'description'."
"add_income", "amount: float, source: str, description: str", "Returns None. Adds an income entry to the database with the given amount, source, and description."
"view_income", "start_date: str (YYYY-MM-DD), end_date: str (YYYY-MM-DD)", "Returns a list of income entries within the specified date range. Each income entry is a dictionary with 'amount', 'source', and 'description'."
"calculate_balance", "", "Returns the current balance as a float by subtracting total expenses from total income."
"generate_report", "start_date: str (YYYY-MM-DD), end_date: str (YYYY-MM-DD)", "Returns a dictionary with total income, total expenses, and balance for the specified date range."
"save_data", "filename: str", "Returns None. Saves the current data to a file with the given filename in JSON format."
"load_data", "filename: str", "Returns None. Loads data from the specified file in JSON format and updates the current data."
"set_budget", "category: str, amount: float", "Returns None. Sets or updates the budget for a specific category."
"view_budget", "category: str", "Returns the budget for the specified category as a float."
"""

def generate_function_code(function_name, params, description):
    """Send a request to the Groq API to generate function code and return the function code only."""
    prompt = f"""
    Generate the full function code in Python.

    Function Name: {function_name}
    Purpose: {description}
    Inputs: {params}
    Outputs: {description.split('Returns ')[1] if 'Returns ' in description else 'Output description not provided'}
    """

    print(prompt)

    try:
        # Request code generation from the Groq API
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "system",
                    "content": "Generate the full function code in Python, without any additional text or formatting. Do not and do not use ```"
                },
                {
                    "role": "user",
                    "content": prompt.strip()
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )

        # Extract the generated function code from the response
        function_code = completion.choices[0].message.content

        # Debugging: Print the extracted function code to verify it
        print(f"Generated code for {function_name}:\n{function_code}\n")

        return function_code


    except Exception as e:
        # If an error occurs, return the full response for debugging purposes
        response_str = str(completion)
        print(f"Failed to generate code for {function_name}: {e}")
        return f"# Failed to generate code for {function_name}.\n# Error: {str(e)}\n\nFull Response:\n{response_str}"

def save_to_file(filename, content):
    """Save generated code or error content to the appropriate file."""
    with open(filename, 'w') as file:
        file.write(content)

def main():
    # Parse the CSV data
    csv_reader = csv.DictReader(csv_data.strip().splitlines())
    
    for row in csv_reader:
        function_name = row['function_title'].strip()
        params = row['exact_parameters'].strip()
        description = row['function_description'].strip()

        # Generate code for each function and get the function code only
        generated_code = generate_function_code(function_name, params, description)

        # Generate the filename based on the function name
        filename = f"{function_name}.py"

        # Save the function code or error content to the appropriate file
        save_to_file(filename, generated_code)
        print(f"Generated code for {function_name} and saved to {filename}")

if __name__ == "__main__":
    main()
