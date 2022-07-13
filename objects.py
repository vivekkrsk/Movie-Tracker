from tmdb import tmdb


class user:
    def __init__(self, name, userid, pword):
        self.name = name
        self.id = userid
        self.pword = pword
        self.watched = []
        self.watchlist = []
    
    def append_watched(self, movie):
        result = tmdb.search(movie).json()['results']
        j = 1
        for i in result:
            print(j + '. ' + i['title'])
        idx = int(input('\nEnter index number : '))
        self.watched.append(result[idx-1]['id']) 
    
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
