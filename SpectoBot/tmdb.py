import os
import random
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"
IMG_URL = "https://image.tmdb.org/t/p/w500"


def make_request(endpoint, params=None):
    if params is None:
        params = {}

    params.update({
        "api_key": API_KEY,
        "language": "ru-RU"
    })

    response = requests.get(f"{BASE_URL}{endpoint}", params=params, timeout=15)
    response.raise_for_status()
    return response.json()


def normalize_movie(movie):
    return {
        "title": movie.get("title", "Без названия"),
        "year": movie.get("release_date", "----")[:4] if movie.get("release_date") else "----",
        "rating": movie.get("vote_average", 0),
        "overview": movie.get("overview", "Описание отсутствует."),
        "poster": IMG_URL + movie["poster_path"] if movie.get("poster_path") else None
    }


def pick_movie(results):
    filtered = [movie for movie in results if movie.get("title") and movie.get("overview")]
    if not filtered:
        filtered = results

    if not filtered:
        return None

    return normalize_movie(random.choice(filtered))


def get_random_movie(category="random", genre_id=None):
    if category == "genre":
        data = make_request(
            "/discover/movie",
            {
                "sort_by": "popularity.desc",
                "page": random.randint(1, 5),
                "vote_count.gte": 200,
                "with_genres": genre_id,
                "include_adult": False
            }
        )
        return pick_movie(data.get("results", []))

    if category == "popular":
        data = make_request(
            "/movie/popular",
            {
                "page": random.randint(1, 5)
            }
        )
        return pick_movie(data.get("results", []))

    if category == "top":
        data = make_request(
            "/movie/top_rated",
            {
                "page": random.randint(1, 5)
            }
        )
        return pick_movie(data.get("results", []))

    data = make_request(
        "/discover/movie",
        {
            "sort_by": "popularity.desc",
            "page": random.randint(1, 5),
            "vote_count.gte": 300,
            "include_adult": False
        }
    )
    return pick_movie(data.get("results", []))