from urllib import response
import requests
import config

class tmdb:
    def search(movie):
        words = movie.split()
        movie = '+'.join(words)
        response = requests.get('https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(config.api_key, movie))

        #results = response.json()['results']

        return response

    def search_by_id(movieid):
        response = requests.get('')

def main():
    response = requests.get('https://api.themoviedb.org/3/genre/movie/list?api_key={}&language=en-US'.format(config.api_key))
    print(response.json())
main()
