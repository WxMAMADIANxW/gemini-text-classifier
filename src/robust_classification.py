import instructor
from vertexai.generative_models import GenerativeModel
import models.model as model 

MODEL = "gemini-1.5-pro"
MODE = instructor.Mode.VERTEXAI_TOOLS
SYSTEM_PROMPT = "Classify the following customer support ticket into a category." 



client = instructor.from_vertexai(GenerativeModel(model_name=MODEL, system_instruction=SYSTEM_PROMPT), mode=MODE)


def classify_ticket(ticket_text: str) -> model.Ticket:
    response = client.create(
        response_model=model.Ticket,
        messages=[
            {
                "role": "user",
                "content": ticket_text,
            },
        ],
        max_retries=3
    )
    
    return response



ticket1 = "I am having trouble with my computer. It won't turn on."

reply = classify_ticket(ticket1)

print(reply.model_dump_json(indent=2))




    
    