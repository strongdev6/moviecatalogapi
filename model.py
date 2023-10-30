from datetime import date
from pydantic import BaseModel, Field
import uuid


class Movies(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    title: str
    releaseDate: date
    director: str
    rating: int
    genre: str
    leadActor: str
    leadActress: str