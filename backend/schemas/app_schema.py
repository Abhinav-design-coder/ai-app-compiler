from pydantic import BaseModel
from typing import List, Dict

class AppSchema(BaseModel):
    intent: Dict
    modules: List[str]
    schema: Dict
