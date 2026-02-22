def build_carrer_prompt(user_input, chat_history):

    system_prompt = """
You are a professional AI Career Advisor.

Rules:
- Only answer career-related questions.
- Provide structured responses.
- Be practical and actionable.
- Avoid generic motivational fluff.

Response Format:
1. Career Overview
2. Required Skills
3. Learning Roadmap
4. Expected Timeline
5. Interview Preparation
"""
    history_text = '\n'.join(chat_history)

    full_prompt = f"""
{system_prompt}

Conversation History:
{history_text}

User Question:
{user_input}
"""
    return full_prompt