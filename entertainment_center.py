import fresh_tomatoes
import media


def make_actor_list(table):
    # Generates a list of Actor objects using data from table which should
    # be a list of lists in the following format:
    #   [[name, month_of_birth, day_of_birth, year_of_birth], ...]
    # name is a string but all other fields are integers.
    actors = []
    for row in table:
        actors.append(media.Actor(row[0], row[1], row[2], row[3]))
    return actors


def make_director_list(table):
    # Generates a list of Director objects using data from table which should
    # be a list of lists in the following format:
    #   [[name, month_of_birth, day_of_birth, year_of_birth], ...]
    # name is a string but all other fields are integers.
    directors = []
    for row in table:
        directors.append(media.Director(row[0], row[1], row[2], row[3]))
    return directors


def get_airplane():
    # Generate the Movie object for "Airplane!"
    actors = make_actor_list([
        ["Robert Hays", 7, 24, 1947],
        ["Julie Hagerty", 6, 15, 1955],
        ["Leslie Nielsen", 2, 11, 1926]])
    directors = make_director_list([
        ["Jim Abrahams", 5, 10, 1944],
        ["David Zucker", 10, 16, 1947],
        ["Jerry Zucker", 3, 11, 1950]])
    movie = media.Movie(
        "Airplane!",
        ("A man afraid to fly must ensure that a plane lands safely after the "
        "pilots become sick."),
        media.MovieRatingEnum.PG,
        "images/imdb-airplane.jpg",
        "https://www.youtube.com/watch?v=rzRJWy-3_Dc",
        actors,
        directors)
    return movie


def get_better_off_dead():
    # Generate the Movie object for "Better Off Dead"
    actors = make_actor_list([
        ["John Cusack", 6, 28, 1966],
        ["David Ogden Stiers", 10, 31, 1942],
        ["Kim Darby", 7, 8, 1947]])
    directors = make_director_list([["Savage Steve Holland", 1, 1, 1960]])
    movie = media.Movie(
        "Better Off Dead",
        ("A teenager has to deal with his girlfriend dumping him among family "
         "crises, homicidal paper boys, and a rival skier."),
        media.MovieRatingEnum.PG,
        "images/imdb-better_off_dead.jpg",
        "https://www.youtube.com/watch?v=DWTouGjZt6A",
        actors,
        directors)
    return movie


def get_ferris_beullers_day_off():
    # Generate the Movie object for "Ferris Beuller's Day Off"
    actors = make_actor_list([
        ["Matthew Broderick", 3, 21, 1962],
        ["Alan Ruck", 7, 1, 1956],
        ["Mia Sara", 6, 19, 1967]])
    directors = make_director_list([["John Hughes", 2, 18, 1950]])
    movie = media.Movie(
        "Ferris Bueller's Day Off",
        ("A high school wise guy is determined to have a day off from school, "
         "despite what the principal thinks of that."),
        media.MovieRatingEnum.PG13,
        "images/imdb-ferris.jpg",
        "https://www.youtube.com/watch?v=R-P6p86px6U",
        actors,
        directors)
    return movie


def get_hot_tub_time_machine():
    # Generate the Movie object for "Hot Tub Time Machine"
    actors = make_actor_list([
        ["John Cusack", 6, 28, 1966],
        ["Rob Corddry", 2, 4, 1971],
        ["Craig Robinson", 10, 25, 1971],
        ["Clark Duke", 5, 5, 1985]])
    directors = make_director_list([["Steve Pink", 2, 3, 1966]])
    movie = media.Movie(
        "Hot Tub Time Machine",
        ("A malfunctioning time machine at a ski resort takes a man back to "
         "1986 with his two friends and nephew, where they must relive a "
         "fateful night and not change anything to make sure the nephew "
         "is born."),
        media.MovieRatingEnum.R,
        "images/imdb-hot_tub.jpg",
        "https://www.youtube.com/watch?v=_TXNEE6SaoI",
        actors,
        directors)
    return movie


def get_superbad():
    # Generate the Movie object for "Superbad"
    actors = make_actor_list([
        ["Michael Cera", 6, 7, 1988],
        ["Jonah Hill", 12, 20, 1983]])
    directors = make_director_list([["Greg Mottola", 7, 11, 1964]])
    movie = media.Movie(
        "Superbad",
        ("Two co-dependent high school seniors are forced to deal with "
         "separation anxiety after their plan to stage a booze-soaked party "
         "goes awry."),
        media.MovieRatingEnum.R,
        "images/imdb-superbad.jpg",
        "https://www.youtube.com/watch?v=KAOvCCmsrbo",
        actors,
        directors)
    return movie


def get_super_troopers():
    # Generate the Movie object for "Super Troopers"
    actors = make_actor_list([
        ["Erik Stolhanske", 8, 23, 1968],
        ["Jay Chandrasekhar", 4, 9, 1968],
        ["Steve Lemme", 11, 13, 1968],
        ["Kevin Heffernan", 5, 25, 1968],
        ["Paul Soter", 8, 16, 1969]])
    directors = make_director_list([["Jay Chandrasekhar", 4, 9, 1968]])
    movie = media.Movie(
        "Super Troopers",
        ("Five Vermont state troopers, avid pranksters with a knack for "
         "screwing up, try to save their jobs and out-do the local police "
         "department by solving a crime."),
        media.MovieRatingEnum.R,
        "images/imdb-super_troopers.jpg",
        "https://www.youtube.com/watch?v=MPhWl_S8ies",
        actors,
        directors)
    return movie


# Create the list of Movie objects.
movies = [
    get_airplane(),
    get_better_off_dead(),
    get_ferris_beullers_day_off(),
    get_hot_tub_time_machine(),
    get_superbad(),
    get_super_troopers()
]

# Generate index.html.
fresh_tomatoes.open_movies_page(movies)