import webbrowser

class Movie():
    """This class provides a way to store movie related information"""

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    # initialize method for the Movie class to create instance variables.
    def __init__(self, movie_title, movie_story, poster_image, trailer_youtube):
        self.title = movie_title
        self.story = movie_story
        self.poster = poster_image
        self.trailer = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer)
