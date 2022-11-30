# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 11/29/2022
# Description: Write a class named Movie, StreamingService, and StreamingGuide. StreamingGuide will have
# a list of StreamingServices, and a Streaming Service will have a dictionary of Movies. The where_to_watch_movie
# method needs to use this nested information to determine which StreamingServices,
# if any, have the desired movie available.

class Movie:
    """Represents general information of a specific movie."""

    def __init__(self, title, genre, director, year):
        self.__title = title  # Title of the movie
        self.__genre = genre  # Genre of the movie
        self.__director = director  # Director of the movie
        self.__year = year  # Year the movie was produced

    def get_title(self):
        """Returns the title of the movie."""
        return self.__title

    def get_genre(self):
        """Returns the genre of the movie."""
        return self.__genre

    def get_director(self):
        """Returns the director of the movie."""
        return self.__director

    def get_year(self):
        """Returns the year the movie was produced."""
        return self.__year


class StreamingService:
    """Represents a specific Streaming Service with certain movies."""

    def __init__(self, name):
        self.__name = name  # Name of the Streaming Service
        self.__catalog = {}  # Dictionary of movies

    def get_name(self):
        """Returns the name of the streaming service."""
        return self.__name

    def get_catalog(self):
        """Returns movies within a dictionary."""
        return self.__catalog

    def add_movie(self, movie):
        """Adds a movie to the catalog."""
        self.__catalog[movie.get_title()] = movie

    def delete_movie(self, movie_title):
        """Deletes a movie from the catalog if it is already there."""
        if movie_title in self.__catalog:
            del self.__catalog[movie_title]


class StreamingGuide:
    """Represents streaming services."""

    def __init__(self):
        self.__stream_serv = []  # A list of Streaming Services

    def add_streaming_service(self, streamingservice):
        """Adds a streaming service to a list."""
        self.__stream_serv.append(streamingservice)

    def delete_streaming_service(self, streaming_name):
        """Deletes an existing streaming service within a list."""
        for service in self.__stream_serv:
            if service.get_name() == streaming_name:
                self.__stream_serv.remove(service)

    def where_to_watch_movie(self, movie_title):
        """Creates a list of movies."""
        for service in self.__stream_serv:
            if movie_title in service.get_catalog():
                return [service.get_catalog()[movie_title].get_title() + " (" + str(service.get_catalog()[movie_title].
                                                                                    get_year()) + ")",
                        service.get_name()]
        return None


# movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
# movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
# movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
# movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)

# stream_serv_1 = StreamingService('Netflick')
# stream_serv_1.add_movie(movie_2)

# stream_serv_2 = StreamingService('Hula')
# stream_serv_2.add_movie(movie_1)
# stream_serv_2.add_movie(movie_4)
# stream_serv_2.delete_movie('The Seventh Seal')
# stream_serv_2.add_movie(movie_2)

# stream_serv_3 = StreamingService('Dizzy+')
# stream_serv_3.add_movie(movie_4)
# stream_serv_3.add_movie(movie_3)
# stream_serv_3.add_movie(movie_1)

# stream_guide = StreamingGuide()
# stream_guide.add_streaming_service(stream_serv_1)
# stream_guide.add_streaming_service(stream_serv_2)
# stream_guide.add_streaming_service(stream_serv_3)
# stream_guide.delete_streaming_service('Hula')
# search_results = stream_guide.where_to_watch_movie('Little Women')
# print(search_results)
