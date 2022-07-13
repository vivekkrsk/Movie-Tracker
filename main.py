import pickle
from objects import person
from tmdb import tmdb

# pickle_off = open("EmpID.pickle", 'rb')
# EmpID = pickle.load(pickle_off)
# print(EmpID)

print('\nWelcome to Movie Tracker\n')
ans = input('Are you an existing user?(Y/n)')
if ans == 'Y' or ans == 'y':
    print('\nLogin.')
    userid = input('Enter userid: ')
    pword = input('Enter password: ')
    main()
else:
    print('\nSign Up.')
    name = input('Enter your name: ')
    userid = input('Enter userid: ')
    pword = input('Enter password: ')
    nuser = person(name, userid, pword)

def main():


