import google.generativeai as palm
import requests


palm.configure(api_key='AIzaSyARaOJ146arb0tNd6rdGKYJbuDUCW8kU0M')
palm.chat_async

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
print(model)

user_text = 'List of chapters'

prompt = "Write Python code to access bard api from Streamlit community cloud hosted app"

completion = palm.generate_text(
                model=model,
                prompt=prompt,
                temperature=0,
                # The maximum length of the response
                max_output_tokens=800,
            )

print(completion.result)
