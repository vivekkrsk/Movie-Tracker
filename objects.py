from unicodedata import name


class Person:
    def __init__(self):
        self.name = name
        self.watched = []
        self.watchlist = []
    
    def append_watched(self, movie):
        self.watched.append(movie)
    
    def get_watched(self):
        return self.watched
    
    def remove_watched(self, movie):
        try:
            self.watched.remove(movie)
        except ValueError:
            print("\nNo movie with this name is in watched list.")
        
    
    def append_watchlist(self, movie):
        self.watchlist.append(movie)
    
    def get_watchlist(self):
        return self.watchlist
    
    def remove_watchlist(self, movie):
        self.watchlist.remove(movie) 
