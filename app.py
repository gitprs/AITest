from flask import Flask, request, render_template
import os
from openai import OpenAI

# Ensure the OPENAI_API_KEY is set in your environment variables for security
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("No API key provided. Set the OPENAI_API_KEY environment variable.")

client = OpenAI(api_key=api_key)

'''
# Create a new assistant
my_assistant = client.beta.assistants.create(
    instructions="You are a medical healthcare compliance officer. When asked a question, respond as a seasoned professional from the healthcare medical compliance, coding, and medical billing field.",
    name="PRS Expert",
    tools=[{"type": "code_interpreter"}],
    model="gpt-3.5-turbo-0125",
)
'''
assistant_id = "asst_SROMBvCH1Fr3EYQ1I8jgZ22x"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form.get('user_input')
    if not user_input:
        return render_template('index.html', error="Please enter some text to chat with the bot.")

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",  # Specify the model directly if needed
            messages=[
                {"role": "system", "content": "I am the PRS Expert coding and compliance chatbot, ready to assist you."},
                {"role": "user", "content": user_input},
            ]
        )
        # print("DEBUG RESPONSE:", response)  # Add this line to print the response
        chat_response = response.choices[0].message.content  # Access method based on previous assumptions
        return render_template('index.html', user_input=user_input, chatgpt_response=chat_response)
    except Exception as e:
        # print("DEBUG ERROR:", e)  # Print errors to help with debugging
        return render_template('index.html', error=f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)  # Consider setting debug=False in a production environment
