import datetime
import webbrowser


class Actor():
    """An instance of this class stores information about an actor."""

    def __init__(self, name, month_of_birth, day_of_birth, year_of_birth):
        self.name = name
        self.date_of_birth = datetime.date(year_of_birth,
                                           month_of_birth,
                                           day_of_birth)


class MovieRatingEnum():
    """This class represents an enumeration of valid movie ratings."""

    G = "G"
    PG = "PG"
    PG13 = "PG-13"
    R = "R"


class Movie():
    """An instance of this class stores information about a movie."""
    
    def __init__(self, movie_title, movie_storyline, rating, poster_image,
                 trailer_youtube, actor_list):
        self.title = movie_title
        self.storyline = movie_storyline
        self.rating = rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.actor_list = actor_list

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)