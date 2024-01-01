import openai

OPEN_AI_ORGANIZATION='org-d5zLhIfEX8XvY9ovC9YsRTXh'
OPEN_AI_API_KEY='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'

openai.api_key = OPEN_AI_API_KEY

response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[
            {'role': 'user', 'content': 'hi, gpt'}],
                temperature=0.0,
)

print(response)
