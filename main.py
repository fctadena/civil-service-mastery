import os
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv('GEMENI_API', 'default_value')  # 'default_value' is optional
if api_key == 'default_value':
    print("Environment variable 'GEMENI_API' is not set.")
else:
    print(f"API Key: {api_key}")