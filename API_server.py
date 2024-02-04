# app.py

# a small server, which reads api endpoint descriptions from endpoints.py and hosts these to work as a target for LLM generated tests. currently defaults to localhost

# TODO add capability to reload functions when the tests for the last one do not pass.
# TODO tidy upp the wrapper handling. now most of the responsibility is here, but probably for more complex endpoits some of it should be transferred to the endpoints.py?

from flask import Flask, request, jsonify
import importlib
import inspect
import urllib

app = Flask(__name__)

def list_routes():
    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(rule.methods)
        line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, rule))
        output.append(line)

    for line in sorted(output):
        print(line)

# Load functions from functions.py
functions_module = importlib.import_module('endpoints')

# Define execute_function outside of the loop
def execute_function(obj):
    def wrapper():
        req_data = request.get_json()
        print(req_data)
        params = req_data.get("params", [])
        print(params)
        try:
            result = obj(*params)
            return jsonify({"result": result})
        except Exception as e:
            return jsonify({"error": str(e)}), 400
        
     # Set a unique name for the wrapper function
    wrapper.__name__ = f'{obj.__name__}_wrapper'
    return wrapper

# Dynamically create endpoints for each function
for name, obj in inspect.getmembers(functions_module):
    if inspect.isfunction(obj):
        app.add_url_rule(f'/functions/{obj.__name__}', view_func=execute_function(obj), methods=['POST']) 
       
        
list_routes()
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

