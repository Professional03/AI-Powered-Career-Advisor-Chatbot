import google.generativeai as genai
from backend.config import Config

genai.configure(api_key=Config.GEMINI_API_KEY)

class GeminiService:
    
    def __init__(self, model_name='gemini-1.5-flash'):
        self.model = genai.GenerationModel(model_name)

    def generate_response(self,prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating response: {str(e)}"