import subprocess
import os
import time

def start_api_server():
    print("Starting API server...")
    api_process = subprocess.Popen(["python", "API_app.py"])
    return api_process

def start_cli_generator():
    print("Starting CLI generator...")
    cli_process = subprocess.Popen(["python", "CLI_LLM_generator.py"], stdin=subprocess.PIPE)
    return cli_process

if __name__ == "__main__":
    api_process = start_api_server()
    time.sleep(5)  # Wait for API server to start (adjust delay as needed)
    cli_process = start_cli_generator()
    cli_process.communicate()  # Wait for CLI generator to finish execution
