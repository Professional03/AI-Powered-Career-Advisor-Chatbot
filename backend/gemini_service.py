from google import genai
from backend.config import Config
from backend.log import log_info, log_error


class GeminiService:

    def __init__(self, model_name="gemini-2.5-flash"):
        self.client = genai.Client(api_key=Config.GEMINI_API_KEY)
        self.model_name = model_name

    def generate_response(self, prompt):
        try:
            log_info("Sending request to Gemini API")
            
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )

            log_info("Received response from Gemini API")
            return response.text

        except Exception as e:
            log_error(f"API Error: {str(e)}")
            return "Something went wrong while generating response."