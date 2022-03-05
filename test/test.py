from flask import request


response = request.post("http://127.0.0.1:5050/call", "frfrf")

print(response)