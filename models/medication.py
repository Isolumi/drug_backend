from pydantic import BaseModel
from datetime import datetime

class Medication(BaseModel):
    name: str
    date_received: datetime
    num_refills: int
    duration: int
    