# Endpoint Unit Test Generator

This application is a CLI tool for generating unit tests from functions defined in a Python file containing endpoint definitions. It utilizes the Typer library for building the command-line interface and integrates with the ChatGPT model to generate unit tests.

## Installation

To install the application, you can use pipenv:

pipenv install --dev

This will install the necessary dependencies, including those specified in the Pipfile and Pipfile.lock.

## Usage

To use the application, run the following commands:

Add your OPENAI_API_KEY to the .env file

start the small API_server.py to the backround to act as a server for the endpoints declared in endpoints.py file.

to run the test generator, run the CLI_LLM_generatory.py file. this will generate tests for the chosen function in endpoints.py file

pipenv run python CLI_LLM_generator.py  <file_path>  <- Defaults to endpoints.py

Replace <file_path> with the path to the Python file containing endpoint definitions. The application will prompt you to select a function from the file, and then it will generate unit tests for the selected function.

TODO run.py


## Features

- Select a function from an endpoints file.
- Generate unit tests based on the selected function.
- Utilizes the ChatGPT model (3.5-turbo) for generating test cases.


## TODO

this is a work in progress proof of concept app where it can be possible to generate code and functions based on test definitions. currently this application only implemetns the test generation side as a POC. when finished, the flow of the application would be:

1. generate a stack of acceptance tests for you wanted function using an LLM to expand your test array.
2. the system runs the tests against a dynamically assigned endpoint. if the tests fail the test results and the function are passed to an LLM and the function recoded. this cycle can be ran as many times as neede to get a function which passes acceptance tests.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

