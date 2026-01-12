from typing import List
from datetime import datetime
from datetime import date
from .rating import get_rating
from person import person

GENRES = frozenset([
    "ACTION & ADVENTURE",
    "COMEDY",
    "DRAMA",
    "HORROR",
    "ROMANCE",
    "SCIENCE FICTION & FANTASY",
    "WESTERN"
])

class Movie:
    def __init__(self,
                 rt_link: str,  # required
                 title: str,  # required
                 rt_rating: str,  # required
                 genre: str,  # required
                 directors: str | None = None,
                 release_date: date | None = None,
                 streaming_date: date | None = None,
                 length: int | None = None,
                 company: str | None = None,
                 score: int | None = None,
                 count: int | None = None,
                 ):
        # checking the for validity
        self._validate_string(rt_link, "Rotten Tomatoes link")
        self._validate_string(title, "Movie title")
        self._validate_optional_dates(release_date, streaming_date)
        self._validate_positivity(length, "Runtime")
        self._validate_positivity(count, "Audience count")
        self._validate_audience_rating(score)
        self._validate_optional_string(company, "Production company")

        # Assignment
        self.rt_link = rt_link
        self.title = title
        self.content_rating = get_rating(rt_rating)
        self.genre = genre
        self.directors = get_directors(directors)
        self.release_date = release_date
        self.streaming_date = streaming_date
        self.length = length
        self.company = company
        self.score = score
        self.count = count

    # -------------------------
    # Validation check
    # -------------------------

    def _validate_string(self, value: str, field_name: str) -> None:
        if not isinstance(value, str):
            raise ValueError(f"{field_name} must be a non-empty string")

    def _validate_optional_string(self, value: str, field_name: str) -> None:
        if value is not None and not isinstance(value, str):
            raise ValueError(f"{field_name} must be a non-empty string or None")

    def _validate_optional_dates(self, original: date, streaming: date) -> None:
        if original is None or original is not isinstance(original, date):
            return
        if streaming is None or streaming is not isinstance(streaming, date):
            return
        if streaming < original:
            raise ValueError("Streaming release date cannot be before original release date")

    def _validate_positivity(self, value: int, field_name: str) -> None:
        if value is None:
            return
        if value <= 0:
            raise ValueError(f"{field_name} must be greater than 0")

    def _validate_audience_rating(self, value: int) -> None:
        if value is None:
            return
        if value < 0 or value > 100:
            raise ValueError("Audience rating must be between 0 and 100")

    def relevant_score(self) -> bool:
        """
        Return True if the score is relevant (score exists and at least 100 votes).
        """
        if self.score is None or self.count is None:
            return False
        return self.score >= 100

    def is_classic(self) -> bool:
        """
        Return True if the movie is at least 20 years old and has a relevant
        score higher than 80.
        """
        if self.release_date is None or self.score is None:
            return False

        years_old = (date.today() - self.release_date).days / 365.25
        return years_old >= 20 and self.score > 80

    def is_short(self) -> bool:
        """
        Return True if the movie is a short film (length < 30 minutes).
        """
        return self.length is not None and self.length < 30

    def url(self) -> str:
        """Return the Rotten Tomatoes URL for the movie."""
        return f"https://www.rottentomatoes.com/{self.rt_link}"

def get_directors(director_csv: str) -> list[person.Person] | None:
    if director_csv is None:
        return None
    all_directors = []
    for names in director_csv.split(','):
        name = names.strip()
        persons = person.get_person(name)
        all_directors.append(persons)
    return all_directors


class ActionAdventure(Movie):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, genre = "ACTION & ADVENTURE", **kwargs)

class Comedy(Movie):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, genre = "COMEDY", **kwargs)
    def is_slapstick(self) -> bool:
        return self.relevant_score() and self.score < 40

class Drama(Movie):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, genre = "DRAMA", **kwargs)

class Horror(Movie):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, genre = "HORROR", **kwargs)
    def is_scary(self) -> bool:
        if self.content_rating is None:
            return False
        return self.content_rating.rank > 2

class Romance(Movie):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, genre = "ROMANCE", **kwargs)
    def is_cosy(self) -> bool:
        return self.length is not None and 70 <= self.length <= 100

class ScienceFictionFantasy(Movie):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, genre = "SCIENCE FICTION & FANTASY", **kwargs)

class Western(Movie):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, genre = "WESTERN", **kwargs)


def parse_date(value: str) -> date | None:
    value = value.strip()
    if not value:
        return None
    return datetime.strptime(value, "%m/%d/%Y").date()

def parse_int(value: str) -> int | None:
    value = value.strip()
    if not value:
        return None
    return int(value)


genre_map = {
    "ACTION & ADVENTURE": ActionAdventure,
    "COMEDY": Comedy,
    "DRAMA": Drama,
    "HORROR": Horror,
    "ROMANCE": Romance,
    "SCIENCE FICTION & FANTASY": ScienceFictionFantasy,
    "WESTERN": Western,
}

def create_movie(movie_info: dict) -> Movie:
    """
    Create a Movie subclass instance from a single CSV row.
    :param movie_info: Dictionary containing movie information with keys
    :return: Instance of a Movie subclass corresponding to the genre.
    :raises ValueError: If the genre is unknown.
    """

    genre = movie_info.get("genre", "").upper().strip()
    if genre not in genre_map:
        raise ValueError(f"Onbekend genre: {genre}")

    movie_class = genre_map[genre]

    # Maak een instance en sla die op
    movie_instance = movie_class(
        rt_link=movie_info.get("rotten_tomatoes_link", ""),
        title=movie_info.get("movie_title", ""),
        rt_rating=movie_info.get("content_rating", ""),
        directors=movie_info.get("directors") or None,
        release_date=parse_date(movie_info.get("original_release_date")),
        streaming_date=parse_date(movie_info.get("streaming_release_date")),
        length=parse_int(movie_info.get("runtime")),
        company=movie_info.get("production_company") or None,
        score=parse_int(movie_info.get("audience_rating")),
        count=parse_int(movie_info.get("audience_count")),
    )

    return movie_instance

