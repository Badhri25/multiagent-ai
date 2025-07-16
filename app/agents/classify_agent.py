import openai

def classify_topic(text, topic_list):
    prompt = f"""
    Given this paper content:
    {text[:2000]}
    Match and return the most suitable topic from this list:
    {topic_list}
    """
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content.strip()
