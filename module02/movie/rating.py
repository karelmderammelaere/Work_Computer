RATING_DATA = {
        "NR": ("Not rated", 0),
        "G": ("Suitable for all ages", 1),
        "PG": ("Parental guidance suggested", 2),
        "PG-13": ("Parents strongly cautioned", 3),
        "R": ("Under 17 requires accompanying parent or adult guardian", 4),
        "NC17": ("Adults only", 5),
    }

class MovieRating:
    def __init__(self, code: str, description: str, rank: int) -> None:
        self._check_code(code)
        self._check_exists_in_ratings(code, description, rank)

        self.code = code
        self.description = description
        self.rank = rank

    def __repr__(self):
        return f"Rating({self.code})"

    def __eq__(self, other) -> bool:
        return self.rank == other.rank
    def __lt__(self, other) -> bool:
        return self.rank < other.rank
    def __gt__(self, other) -> bool:
        return self.rank > other.rank
    def __le__(self, other) -> bool:
        return self.rank <= other.rank
    def __ge__(self, other) -> bool:
        return self.rank >= other.rank

    def _check_code(self, code: str):
        if not isinstance(code, str) or not code.strip():
            raise ValueError("Code must be a non-empty string")

    def _check_exists_in_ratings(self, code, description, rank):
        data = RATING_DATA.get(code)
        if not data or data[0] != description or data[1] != rank:
            raise ValueError(f"Invalid MovieRating combination: {code}, {description}, {rank}")


def get_rating(code: str) -> MovieRating:
    """
    Return a MovieRating object for a given code
    :param code: rating code
    :return: a MovieRating object
    """
    data = RATING_DATA.get(code)

    if data is None:
        raise ValueError(f"Invalid movie rating code: {code}")

    description, rank = data

    return MovieRating(code, description, rank)


