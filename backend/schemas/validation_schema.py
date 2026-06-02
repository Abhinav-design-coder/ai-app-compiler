from pydantic import BaseModel

class ValidationSchema(BaseModel):
    valid: bool
    errors: list = []
