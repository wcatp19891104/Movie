__author__ = 'fei'
import webbrowser


class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


if __name__ == "__main__":
    movie = Movie("tiny times",
                  "tell friendship among four girls",
                  "https://importanceofbeinggay.files.wordpress.com/2013/08/tiny-times.jpg",
                  "https://www.youtube.com/watch?v=U2FdzS9DdQU")
    movie.show_trailer()
