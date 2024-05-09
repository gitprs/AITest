import os
from flask import Flask

secret_key = os.getenv('OPEN_API_THREAD_KEY')
if not secret_key:
    raise ValueError("No API key provided. Set the OPEN_API_THREAD_KEY environment variable.")
else:
    print("Secret Key:", secret_key)  # This will print the key to the terminal
