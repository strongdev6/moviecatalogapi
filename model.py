from datetime import date
from pydantic import BaseModel, Field
import uuid


class Movies(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    title: str
    releaseDate: date  # format "YYYY-MM-DD" in payload
    director: str
    rating: int
    genre: str
    leadActor: str
    leadActress: str