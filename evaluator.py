import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# load_dotenv()
# client = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))

# def eval(cus_email, trainee_email):
#     prompt = f"""I want you to assume the role of a customer serivce trainer. A customer sent the follwing email: {cus_email}. The customer serivce officer sent this reply email: {trainee_email}. Evaluate the reply based on 1.Tone, 2.Clarity, 3.Helpfulness, 4.Correctness. Return your answer in valid JSON with this exact structre and do not include any markdown or explanation:
#               {{"overall_score": <number out of 10>,
#                 "strengths": ["point 1", "point 2"],
#                 "improvements": ["point 1", "point 2"],
#                 "suggested_reply": "a better sample reply"}} """
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",messages=[{"role": "system", "content": "You are an expert customer service trainer."},
#         {"role": "user", "content": prompt}], temperature=0.3)
#     content = response.choices[0].message.content
#     content = content.strip()
#     return json.loads(content)

def eval(cus_email, trainee_email):
    return {
        "overall_score": 7.8,
        "strengths": [
            "Polite and professional tone",
            "Shows empathy toward the customer"
        ],
        "improvements": [
            "Could be clearer about next steps",
            "Could provide a more concrete resolution timeline"
        ],
        "suggested_reply": (
            "Dear Customer, I’m sorry for the delay in your refund and understand "
            "how frustrating this must be. I will check the status of your refund "
            "and provide you with an update as soon as possible."
        )
    }