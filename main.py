from fastapi import FastAPI
from model import Movies

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


movies = []


# get all movies listing
@app.get("/movies")
async def get_movie():
    return {"movie": movies}


# get a single movie listing
@app.get("/movies/{movie_id}")
async def get_movie(movie_id: int):
    try:
        return {"movie": movies[movies.index(movie_id)]}
    except:
        return {"message": "No movie found"}


# create a movie listing
@app.post("/movies")
async def create_movie(movie: Movies):
    movies.append(movie)
    return {"message": "Movie was created"}


# delete a movie listing
@app.delete("/movies/{movie_id}")
async def delete_movie(movie_id: int):
    for movie in movies:
        if movie.id == movie_id:
            movies.remove(movie)
            return {"message": "Movie was deleted"}
    return {"message": "No movie found"}
