# python imports
import csv
import os
from typing import List
from datetime import date

#custom imports
from movie.movie import Movie, create_movie
from movie.rating import MovieRating
from person import person

# These constants must point to the input file reviews.csv,
# and the location of the output file (see item 9)
MOVIE_FILE = "C:\\Users\\0031803\\PycharmProjects\\Work_Computer\\module02\\MovieFile.csv"
EXPORT_FILE = "C:\\Users\\0031803\\PycharmProjects\\Work_Computer\\module02\\ExportFile.csv"


def load_movies(file_location: str) -> List[Movie] | None:
    """
    Load all movies from a csv file into a list of Movie objects.
    :param file_location: Location of the csv file
    :raise FileNotFoundError: When the file cannot be found
    :return: List of Movie objects or None in case of error
    """
    if not os.path.exists(file_location):
        raise FileNotFoundError("Bestand niet gevonden: {file_location}")
    try:
        errors = 0
        movies = []
        with (open(file_location, 'r', encoding="utf-8-sig") as file):
            reader = csv.DictReader(file, delimiter=";")
            for i, row in enumerate(reader):
                try:
                    movie = create_movie(row)
                    movies.append(movie)
                except ValueError as e:
                    errors += 1
                    print(f"Probleem met Lijn {i} : '{e}' => {row}")
        if errors:
            print(f"{errors} films konden niet geladen worden")
    except Exception as e:
        # Exception is a good choice
        print(f"Probleem bij het inlezen van bestand: {file_location} => {e}")
        return None
    return movies

print(load_movies(MOVIE_FILE))


def print_menu():
    print("""
        1) Print het aantal films
        2) Print de films per genre
        3) Aantal personen
        4) Hoogste score
        5) Actiefste regisseur
        6) Kortste en langste film
        7) Enge horror
        8) Scorelijst
        9) Exporteer (films zonder score)
        10) Stop
    """)

def main():
    """
    Load movies and present a menu until the user chooses to stop
    """
    movies = load_movies(MOVIE_FILE)

    while True:
        print_menu()
        choice = input("Maak een keuze: ")

        match choice:
            case "1": print_aantal_films(movies)
            case "2": print_films_per_genre(movies)
            case "3": print_aantal_personen(movies)
            case "4": print_hoogste_score(movies)
            case "5": print_actiefste_regisseur(movies)
            case "6": print_kortste_en_langste_film(movies)
            case "7": print_enge_horror(movies)
            case "8": print_scorelijst(movies)
            case "9": export_films_zonder_score(movies)
            case "10": break
            case _: print("Ongeldige keuze")


def print_aantal_films(movies):
    print(f"Aantal films: {len(movies)}")


def print_films_per_genre(movies):
    """
    Prints the number of films for each genre in a descending order.
    :param movies: lijst van Movie-objecten of subklassen
    """
    result = {}
    for movie in movies:
        genre = movie.genre
        if genre in result:
            result[genre] += 1
        else:
            result[genre] = 1
    # Sorteer de dictionary op aantal (value) in aflopende volgorde
    result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
    for genre, aantal in result.items():
        print(f"{genre}: {aantal}")
    return result


def print_aantal_personen(movies):
    """
    Print het aantal unieke personen (directors) in de lijst van movies.
    :param movies: Lijst van Movie-objecten
    :return: None
    """
    unieke_personen = set()
    for movie in movies:
        if movie.directors:  # directors kan None zijn
            for director in movie.directors:
                unieke_personen.add(director.fullname)
    print(f"Aantal personen: {len(unieke_personen)}")


def print_hoogste_score(movies):
    max_score = 0
    filtered_movies = []
    for m in movies:
        if m.score is not None:
            filtered_movies.append(m)
            if m.score > max_score:
                max_score = m.score
    if len(filtered_movies) < 1:
        print("Er zijn geen movies met scores.")
    print(f"Hoogste score: {max_score}")

    for movie in filtered_movies:
        if movie.score == max_score:
            print(movie.title)


def print_actiefste_regisseur(movies):
    """
    Print de regisseur(s) die het meeste aantal films regisseerden.
    :param movies: Lijst van Movie objecten
    :return: None
    """
    unieke_personen = {}
    for movie in movies:
        if movie.directors:  # directors kan None zijn
            for director in movie.directors:
                if director.fullname in unieke_personen:
                    unieke_personen[director.fullname] += 1
                else:
                    unieke_personen[director.fullname] = 1
    if not unieke_personen:
        print("Geen regisseurs gevonden.")
        return
    hoogste_aantal = max(unieke_personen.values())
    print(f"De regisseur(s) die het meeste aantal ({hoogste_aantal}) films regisseerden zijn:")
    for personname, aantal in unieke_personen.items():
        if aantal == hoogste_aantal:
            print(personname)


def print_kortste_en_langste_film(movies):
    min_length = 100000
    max_length = 0
    movies_with_length = []

    for m in movies:
        if m.length is not None:
            movies_with_length.append(m)
            if m.length < min_length:
                min_length = m.length
            if m.length > max_length:
                max_length = m.length
    if len(movies_with_length) < 1:
        print("Geen filmlengtes beschikbaar")
        return
    print("Kortste film(s):")
    for movie in movies_with_length:
        if movie.length == min_length:
            print(f"{movie.title} ({movie.length} min)")
    print("Langste film(s):")
    for movie in movies_with_length:
        if movie.length == max_length:
            print(f"{movie.title} ({movie.length} min)")


def print_enge_horror(movies):
    print("De enge horror movies zijn:")
    count = 0
    for movie in movies:
        if movie.genre == "HORROR":
            if movie.is_scary():
                print(movie.title)
                count += 1
    print(count)


def print_scorelijst(movies):
    score_telling = {}
    for movie in movies:
        if movie.score is not None:
            if movie.score in score_telling:
                score_telling[movie.score] += 1
            else:
                score_telling[movie.score] = 1
    print("de scorelijst van alle scores van 0 tot 100 en hoeveel films deze score hebben: ")
    for score in range(0, 101):
        aantal = score_telling.get(score, 0)  # 0 als score niet voorkomt
        print(f"{score:3}%: {aantal}")


def export_films_zonder_score(movies, filename=EXPORT_FILE):
    """
    Exporteert films zonder score naar een CSV-bestand, alfabetisch op titel.
    :param movies: lijst van Movie-objecten
    :param filename: naam van het CSV-bestand
    :return: None
    """
    films_zonder_score = [m for m in movies if m.score is None]
    for i in range(len(films_zonder_score)):
        for j in range(i + 1, len(films_zonder_score)):
            if films_zonder_score[i].title.lower() > films_zonder_score[j].title.lower():
                films_zonder_score[i], films_zonder_score[j] = films_zonder_score[j], films_zonder_score[i]
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for movie in films_zonder_score:
            directors = ""
            if movie.directors:
                names = []
                for director in movie.directors:
                    names.append(director.fullname)
                directors = ",".join(names)
            writer.writerow([
                movie.rt_link,
                movie.title,
                movie.content_rating.code,
                movie.genre,
                ",".join(movie.direcotrs),
                movie.release_date or "",
                movie.streaming_date or "",
                movie.length or "",
                movie.company or "",
                movie.score or "",
                movie.count or ""
            ])
    print(f"CSV geëxporteerd naar: {filename}")

if __name__ == "__main__":
   main()
