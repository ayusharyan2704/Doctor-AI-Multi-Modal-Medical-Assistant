from dotenv import load_dotenv
import os
import base64
from groq import Groq

# Step 1: Load .env variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Optional: fallback check below

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing from .env or environment variables")

# Step 2: Encode image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Step 3: Analyze image with LLM
def analyze_image_with_query(query, encoded_image, model="meta-llama/llama-4-scout-17b-16e-instruct"):
    client = Groq(api_key=GROQ_API_KEY)

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}},
            ],
        }
    ]

    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content



# if __name__ == "__main__":
#     test_image ="skin_rash.jpg"  # Make sure this image exists in the same folder
#     query = "What kind of skin issue is visible in this image?"

#     encoded = encode_image(test_image)
#     response = analyze_image_with_query(query, encoded)

#     print("🤖 Diagnosis from AI Doctor:\n")
#     print(response)
