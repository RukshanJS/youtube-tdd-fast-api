from pydantic import BaseModel, Field

class Todo(BaseModel):
    id: int = Field(default=None)
    title: str
    description: str
    completed: bool