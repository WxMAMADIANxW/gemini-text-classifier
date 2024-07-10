from enum import Enum
from typing import List
from pydantic import BaseModel, Field


class TicketCatgory(str, Enum):
    """Category of the ticket

    Args:
        str (_type_): title of the category
        Enum (_type_): category of the ticket
    """
    ACCOUNT_ACCESS = "account_access"
    MATERIAL_ISSUE = "material_issue"
    APPLICATION_ACCESS = "application_access"
    NEW_EMPLOYEE_CREATION = "new_employee_creation"


class TicketUrgency(str, Enum):
    """Urgency of the ticket

    Args:
        str (_type_): title of the urgency
        Enum (_type_): urgency of the ticket
    """
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"
    

class Ticket(BaseModel):
    """Class of a ticket

    Args:
        BaseModel (_type_): pydantic base model
    """
    category: TicketCatgory
    urgency: TicketUrgency
    key_information: List[str] = Field(description="List of key points extracted from the ticket")
    suggested_action: str = Field(description="Brief suggestion for handling the ticket")  


    