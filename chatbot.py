import google.generativeai as genai

genai.configure(
    api_key="AIzaSyDUDQYA2WPjkYfeaGrNwetnHVdMlJUPh-4"
)

model = genai.GenerativeModel("models/gemini-1.0-pro")

response = model.generate_content("Merhaba! Çalışıyor musun?")
print(response.text)
