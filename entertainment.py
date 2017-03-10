import fresh_tomatoes
import media

# instance objects are created by calling the Movie class in the media module.
toy_story = media.Movie("Toy Story","A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A marine on alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

gangs_of_ny = media.Movie("Gangs of New York", "Amsterdam returns to Five Points to get revenge on his father's killer",
                          "https://upload.wikimedia.org/wikipedia/en/a/ae/Gangs_of_New_York_Poster.jpg",
                          "https://www.youtube.com/watch?v=qHVUPri5tjA")

school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet authors",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

pulp_fiction = media.Movie("Pulp Fiction", "Storylines of mobsters, fringe players, small-time criminals, and a mysterious briefcase",
                           "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                           "https://www.youtube.com/watch?v=tGpTpVyI_OQ")

# store movie objects in a movies list and then pass the list into the open_movies_page function.
movies = [toy_story, avatar, gangs_of_ny, school_of_rock, midnight_in_paris, pulp_fiction]
fresh_tomatoes.open_movies_page(movies)
