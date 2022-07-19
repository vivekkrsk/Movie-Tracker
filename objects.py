import imp
from tmdb import tmdb
from genre_ids import genres
import pandas as pd
import matplotlib.pyplot as plt


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
        
        self.top_genre = ['Action', 'Adventure',]

    
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
        if list1 not in self.watched:
            self.watched.append(list1)
            for i in result[idx-1]['genre_ids']:
                self.genre_count[genres[i]] += 1
            
            return result[idx-1]['id'], result[idx-1]
        else:
            print("\nYou have already added this movie to watched.")
            return None, None
    
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
        genre_count_data = {'genres' : self.genre_count.keys(), 'counts' : self.genre_count.values()}
        genre_count_df = pd.DataFrame.from_dict(genre_count_data)

        print('\nYour top genres: ')
        print(genre_count_df.nlargest(5, 'counts').to_string(index=False))

        pie_s_n = input('\nDo you want to see the pie chart?(y/n)')
        if pie_s_n == 'y' or pie_s_n == 'Y':
            plt.pie(genre_count_df["counts"], labels=genre_count_df["genres"])
            plt.title('Genre pie chart')
            plt.show()


        
    
