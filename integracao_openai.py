import openai
import dotenv
import os

dotenv.load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")
resposta = openai.completions.create(
    model='gpt-3.5-turbo',
    prompt=[
        {
            "role": "system",
            "content": "gere apenas os nomes de produtos ficticios conforme solicitação do usuario"
        },
        {
            "role": "user",
            "content": "Gere 5 produtos"
        }
    ]
)

print(resposta)
