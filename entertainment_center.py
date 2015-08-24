__author__ = 'fei'
import fresh_tomatoes
import media


tiny_times = media.Movie("Tiny Times",
                         "Tell friendship among four girls",
                         "https://importanceofbeinggay.files.wordpress.com/2013/08/tiny-times.jpg",
                         "https://www.youtube.com/watch?v=U2FdzS9DdQU")


miss_granny = media.Movie("Miss Granny",
                          "A Granny return to her 20s",
                          "http://linkis.com/url-image/http://www.soompi.com/wp-content/uploads/2014/12/luhan.jpg",
                          "https://www.youtube.com/watch?v=HdZbuNuSKoI")

kung_fu_panda = media.Movie("Kung Fu Panda",
                            "When he's not busy eating, Po is living out his dreams of fighting along side the Furious \
                            Five to protect the Valley of Peace",
                            "http://www.dreamworks.com/kungfupanda/images/uploads/images/_1095/KFP3-teaser-poster-P1.jpg",
                            "https://youtu.be/LFKAHc0bJrU"
                            )

movies = [tiny_times, miss_granny, kung_fu_panda]
fresh_tomatoes.open_movies_page(movies)


