import openai

def summarize_text(text):
    prompt = f"""
    Summarize this research paper clearly and concisely:
    {text[:3000]}
    """
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content.strip()
