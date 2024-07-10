import instructor
from vertexai.generative_models import GenerativeModel
# pylint: disable-next=global-statement
import models.model as model 

MODEL = "gemini-1.5-pro"
MODE = instructor.Mode.VERTEXAI_TOOLS
SYSTEM_PROMPT = """
You are an AI assistant for a large IT company's IT support team. 
Your role is to analyse incoming IT support tickets and provide stuctured information to help our team respond quickly and effectively.

Business context:
- We handle hundreds of tickets every day accross a wide range of categories.
- Quickly identifying the category and urgency of each ticket is crucial for collaborators satisfaction and team efficiency.
- We prioritize tickets based on urgency (low, medium, high, urgent) and category.

Your tasks:
1. Categorized the ticket into the most appropriate category.
2 .Identify the urgency of the ticket (low, medium, high, urgent).
3. Extract key information from the ticket that will help our it support team assess the situation.
4. Provide a initial action that our team can take to address the ticket.

Remember:
- Be objective and base your analysis solely on the information provided in the ticket.
- If you're unsure about any aspect, reflect that in your confidence score.
- For 'key_information', extract specific details like names, type of material.
- The 'suggested_action' should be a brief, actionable step for our support team.
""" 



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



ticket1 = """
Bonjour, tous les jours quand j'essaie de me connecter à ma session mon compte est bloqué. je dois toujours appeler le support pour le débloquer.
"""
reply = classify_ticket(ticket1)
print(reply.model_dump_json(indent=2))


ticket2 = """
Le micro de mon ordinateur est cassé ou ne fonctionne pas 
J'ai essayé de le réparer en redémarrant l'ordinateur mais cela n'a pas fonctionné.
J'ai un call avec un clients dans quelques minutes pour un deal d'une dizaine de milliers d'euros.
Est-ce que vous pouvez m'aider à résoudre ce problème rapidement ?
"""
reply = classify_ticket(ticket2)
print(reply.model_dump_json(indent=2))

ticket3 = """
Une personne m'harcele sur teams l'entreprise.
"""
reply = classify_ticket(ticket3)
print(reply.model_dump_json(indent=2))
    
    