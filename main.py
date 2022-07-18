import pickle
from objects import person
from tmdb import tmdb
import genre_ids

pickle_off = open("db.pickle", 'rb')
db = pickle.load(pickle_off)

def main(suser, db):
    check = 'y'
    while check == 'Y' or check == 'y':
        print('\n')
        print('1. Add to watched')
        print('2. Add to watchlist')
        print('3. Show my watched list')
        print('4. Show my watchlist')
        print('5. Show my stats')

        ans = int(input('\nChoose your option : '))

        if ans == 1:
            ka = 'y'
            while ka == 'Y' or ka == 'y':
                mvname = input('Movie name: ')
                mvid, mv = suser.append_watched(mvname)
                if mvid != None:
                    if mvid not in  db['mvdb']:
                        db['mvdb'][mvid] = mv
                    print('Added to watched.')
                    ka = input('Keep adding?(Y/n)')

        elif ans == 2:
            ka = 'y'
            while ka == 'y' or ka == 'Y':
                mvname = input('Movie name: ')
                suser.append_watchlist(mvname)
                print('Added to your watchlist')
                ka = input('Keep adding?(y/n)')

        elif ans == 3:
            for i in suser.get_watched():
                print(i[1])
        
        elif ans == 5:
            suser.show_stats()
        
        check = input("\nDo you need to do something else?(Y/n)")
    
    pickling_on = open("db.pickle","wb")
    pickle.dump(db, pickling_on)
    pickling_on.close()
        
    



def login(db):
    print('\nLogin.')
    while True:
        userid = input('Enter userid: ')
        pword = input('Enter password: ')
        if userid in db['users'] and db['users'][userid].pword == pword:
            session_user = db['users'][userid]
            break
        else:
            print('Wrong userid or password.\nRe-enter.')
    main(session_user, db)

def sign_up(db):
    print('\nSign Up.')
    name = input('Enter your name: ')
    userid = input('Enter userid: ')
    pword = input('Enter password: ')
    nuser = person(name, userid, pword)
    db['users'][userid] = nuser
    main(nuser, db)

def developer(db):
    print(db)

print('\n\t\tWelcome to Movie Tracker\n')
print('1. Login\n2. Signup\n3. Developer\n')
while True:
    logorsign = input('Choose : ')
    if logorsign == '1':
        login(db)
        break
    elif logorsign == '2':
        sign_up(db)
        break
    elif logorsign == '3':
        developer(db)
        break
    else:
        print('Enter valid option.')


