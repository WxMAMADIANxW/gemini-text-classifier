import vertexai
import json

from vertexai.generative_models import GenerativeModel

vertexai.init()




model = GenerativeModel(
  model_name="gemini-1.5-flash",
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="Classify the following customer support ticket into a category."
)

def classify_ticket(ticket_text: str) -> str:
    """this function classifies a ticket into a category

    Args:
        ticket_text (str): _description_

    Returns:
        dict: _description_
    """
    chat_session = model.start_chat(
 history=[] 
)
    response = chat_session.send_message(ticket_text)

    return response.candidates[0].content.parts[0].text




TICKET2 = "I ordered a laptop from your store last week (Order #12345), but I received a tablet instead. \nThis is unacceptable! I need the laptop for work urgently. Please resolve this immediately or I'll have to dispute the charge."
result = classify_ticket(TICKET2)

print(result)