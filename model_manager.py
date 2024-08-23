"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

class ModelManager:
  def __init__(self):
    self.history = [
      {
        "role": "user",
        "parts": "you are a landin page builder for building landing pages in next js, keep this in mind when answering the following questions. Also keep your answers short and concise."
      }
    ]

    self.generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 64,
      "max_output_tokens": 8192,
      "response_mime_type": "text/plain",
    }


    self.model  = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=self.generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
  )

    self.chat_session = self.model.start_chat(
      history= self.history)

  genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

  # Create the model

  def generate(self, prompt):

    self.history.append({"role": "user", "parts": prompt})

    response = self.chat_session.send_message(prompt)
    print(response.text)
    # self.write_res(response.text)

    self.history.append({"role": "model", "parts": response.text})
    return response.text

  def write_res(self,res):
    with open('res.txt', 'w') as file:
      file.write(res + '\n')
      file.close()


  def set_model(self, model):
    if model == "flash":
      self.model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=self.generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
        # system_instruction="You are a landin page builder for building landing pages in next js, keep this in mind when answering the following questions. Also keep your answers short and concise.",
      )
    elif model == "pro":
      self.model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config=self.generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
      )


