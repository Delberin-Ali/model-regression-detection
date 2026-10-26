from enum import Enum

from pydantic import BaseModel, Field

class EmailCategory(str, Enum):
    BILLING = "billing"
    TECHNICAL = "technical"
    ACCOUNT = "account"
    GENERAL = "general"



class EmailClassification(BaseModel):
    category: EmailCategory
    summary: str = Field(
        min_length= 1, 
        max_length= 300
    )