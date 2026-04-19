from google import genai
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)



def errorFixer(images, selected_option):
    try:
        #print(  Image.open(images))
        response = client.models.generate_content(model="gemini-2.5-flash", 
                                                  contents= [selected_option, Image.open(images[0])])
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"