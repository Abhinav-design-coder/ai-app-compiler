from pydantic import BaseModel
from typing import List

class Intent(BaseModel):
    entities: List[str]
    roles: List[str]
    features: List[str]
    authentication: bool
    payments: bool