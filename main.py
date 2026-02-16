from openai import OpenAI       ##it will connect the main file to LLm
import json                     ##to store the req & res in json
from datetime import datetime   ##to store logs while saving req & res
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(base_url="https://openrouter.ai/api/v1")    ##LLM will auto reads my api key in the .env

user_prompt = input("Enter your prompt: ")  

##sending input to the LLM 

response = client.responses.create(model = "mistralai/mistral-7b-instruct", input = user_prompt)

generated_text = response.output_text

##temp
##generated_text = "This is a mock response because API quota is exceeded."

print("\nGenerated Response:")
print(generated_text)

##logs part in json file

log_entry = {
    "timestamp" :datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "prompt": user_prompt,
    "response":generated_text
}

file_name = "llm_logs.json"

##checking if file exsts before read and write 

try:
    with open(file_name, "r") as file:
        logs=json.load(file)
except FileNotFoundError:
    logs = []

##writting

logs.append(log_entry)

with open(file_name, "w") as file:
    json.dump(logs, file, indent=4)


##saving to json file

print("prompt and response saved to logs.json")


