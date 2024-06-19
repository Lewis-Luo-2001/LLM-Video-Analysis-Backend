import requests
from env import YOUR_API_KEY

init_prompt_en = """
                Please summarize the following transcript and list out the key points.
            """

init_prompt_zh = """
                請總結以下的文字並列出重點。
            """

# Set the base URL for the API
base_url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={YOUR_API_KEY}'

def interact_with_gemini(prompts: list, language="en", is_task=False):
  """
  Sends a prompt to Gemini and returns the generated text.

  Args:
      prompt: The text prompt to send to Gemini.

  Returns:
      The generated text by Gemini, or an error message if unsuccessful.
  """

  input_text = ""
  init_prompt = init_prompt_en

  for prompt in prompts:
    input_text += f"{prompt.role}: {prompt.content} \n"

  if language == "zh":
    init_prompt = init_prompt_zh

  if is_task:
    input_text = init_prompt + input_text

  # Prepare the request data
  data = {
    "contents": [
      {
        "parts": [
          {
            "text": input_text
          }
        ]
      }
    ]
  }

  headers = {'Content-Type': 'application/json'}

  import time

  time.sleep(12)

  try:
    response = requests.post(base_url, headers=headers, json=data)
    response.raise_for_status()  # Raise an exception for unsuccessful status codes

    gemini_response = response.json()["candidates"][0]["content"]["parts"][0]["text"]
    return gemini_response

  except requests.exceptions.RequestException as e:
    return f"Error: {e}"

  except:
    import json
    return json.dumps(response.json(), indent=4)

if __name__ == "__main__":
    print(interact_with_gemini(prompt))