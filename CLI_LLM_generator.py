import os
import inspect
import re
import typer


from LLM_generator import generate_unit_tests
from test_API_app import TestAPI


app = typer.Typer()
test_instance = TestAPI()
def read_functions(file_path):
    functions = []
    with open(file_path, 'r') as file:
        content = file.read()
        # Find all function definitions using regular expression
        # lempikurssini: Regex:Creating unmaintainable mystery code cs302
        function_definitions = re.findall(r'def\s+([^\(]+)\((.*?)\)(.*?)(?=\ndef|\Z)', content, re.DOTALL)
        for name, params, body in function_definitions:
            # Add function name, parameters, and body to the list
            functions.append({"name": name.strip(), "parameters": params.strip(), "body": body.strip()})
    return functions

@app.command()
def select_function(file_path: str = "./endpoints.py"):
    """
    Select a function from an endpoints file to generate tests for
    """
    functions = read_functions(file_path)
    if not functions:
        typer.echo(f"No functions found in {file_path}")
        raise typer.Abort()
    
    typer.echo("Select a function to generate tests for using LLM:")
    for index, function in enumerate(functions):
        typer.echo(f"{index + 1}. {function['name']}")
    
    choice = typer.prompt("Enter the number of the function to generate tests for")
    try:
        choice = int(choice)
        if choice < 1 or choice > len(functions):
            raise ValueError
    except ValueError:
        typer.echo("Invalid choice. Please enter a number between 1 and", len(functions))
        raise typer.Abort()
    
    selected_function = functions[choice - 1]
    typer.echo(f"Selected function: {selected_function['name']}")
    typer.echo(f"Parameters: {selected_function['parameters']}")
    typer.echo(f"Body:\n{selected_function['body']}")

    # TODO add filtering of good and bad test cases and save to folder. 

    test_cases = generate_unit_tests( selected_function['name']+selected_function['parameters']+selected_function['body'] )
    print("----------GENERATED TESTS---------")
    print(test_cases)
    print("----------------------------------")

    test_instance.run_parametrized_test(test_cases)

if __name__ == "__main__":
    app()

# generate tests

# let use pick test cases

# create tests file

#run tests
    
