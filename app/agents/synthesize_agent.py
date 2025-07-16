from agents.summarize_agent import summarize_text

def synthesize_topics(summary_list):
    joined = "\n\n".join(summary_list)
    return summarize_text(joined)
