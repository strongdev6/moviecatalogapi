from pydantic import BaseModel


class Movies(BaseModel):
    id: int
    title: str
    releaseYear: int
    director: str
    rating: int
    genre: str
    leadActor: str
    leadActress: str