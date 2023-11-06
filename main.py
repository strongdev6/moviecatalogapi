import uuid
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Movies(BaseModel):
    id: int = Field(default_factory=lambda: uuid.uuid4().int)  # Generates a unique ID if not provided
    title: str


movies = []  # This will be a list of Movies instances


@app.get("/movies")
async def get_movies():
    return {"movies": movies}


@app.get("/movies/{movie_id}")
async def get_movie(movie_id: int):
    movie = next((movie for movie in movies if movie.id == movie_id), None)
    if movie:
        return {"movie": movie}
    else:
        return {"message": "No movie found"}, 404


@app.post("/movies")
async def create_movie(movie: Movies):
    movies.append(movie)
    return {"message": f"Movie titled '{movie.title}' created"}, 201


@app.delete("/movies/{movie_id}")
async def delete_movie(movie_id: int):
    movie = next((movie for movie in movies if movie.id == movie_id), None)
    if movie:
        movies.remove(movie)
        return {"message": f"Movie titled '{movie.title}' was deleted"}
    else:
        return {"message": "No movie found"}, 404


@app.put("/movies/{movie_id}")
async def update_movie(movie_id: int, update_data: Movies):
    # Find the movie by its ID and update it with the provided data
    for idx, movie in enumerate(movies):
        if movie.id == movie_id:
            updated_movie_data = movie.copy(update=update_data.model_dump(exclude_unset=True))
            movies[idx] = updated_movie_data
            return {"message": f"Movie with id '{movie_id}' has been updated", "movie": updated_movie_data}
        else:
            return {"message": "No movie found"}, 404
