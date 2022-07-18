import imp
from tmdb import tmdb
from genre_ids import genres


class person:
    def __init__(self, name, userid, pword):
        self.name = name
        self.id = userid
        self.pword = pword
        self.watched = []
        self.watchlist = []
        self.genre_count =  {
            'Action' : 0,
            'Adventure' : 0,
            'Animation' : 0,
            'Comedy' : 0,
            'Crime' : 0,
            'Documentary' : 0,
            'Drama' : 0,
            'Family' : 0,
            'Fantasy' : 0,
            'History' : 0,
            'Horror' : 0,
            'Music' : 0,
            'Mystery' : 0,
            'Romance' : 0,
            'Science Fiction' : 0,
            'TV Movie' : 0,
            'Thriller' : 0,
            'War' : 0,
            'Western' : 0}

    
    def append_watched(self, movie):
        result = tmdb.search(movie).json()['results']
        if len(result) == 0:
            '\nPlease check the spelling of the movie.'
            return None, None
        j = 1
        for i in result:
            if j > 5:
                break
            print(str(j) + '. ' + i['title'] + '  - ' + i['release_date'])
            j += 1
        
        idx = int(input('\nEnter index number : '))
        list1 = [result[idx-1]['id'], result[idx-1]['title']]
        self.watched.append(list1)
        for i in result[idx-1]['genre_ids']:
            self.genre_count[genres[i]] += 1
        
        return result[idx-1]['id'], result[idx-1]
    
    def get_watched(self):
        return self.watched
    
    def remove_watched(self, movie):
        try:
            self.watched.remove(movie)
        except ValueError:
            print("\nNo movie with this name is in watched list.")
        
    
    def append_watchlist(self, movie):
        result = tmdb.search(movie).json()['results']
        j = 1
        for i in result:
            print(j + '. ' + i['title'])
        idx = int(input('\nEnter index number : '))
        self.watchlist.append(result[idx-1]['id'])
        print('Done')
    
    def get_watchlist(self):
        return self.watchlist
    
    def remove_watchlist(self, movie):
        self.watchlist.remove(movie)
    
    def show_stats(self):
        print('Genre Count: \n')
        print(self.genre_count)
    
