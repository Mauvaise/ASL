import pickle

userName = []
database = {}
f = open('C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/userData/database.p','rb')
database[userName].append(pickle.load(f))
f.close
              



userName = raw_input('Please enter your name: ')

if userName in database:
    print 'Welcome back ' + userName + '.'

else: 
    userName = database.keys()
    print 'Welcome ' + userName + '.'





pickle.dump(database, open('C:/Users/Tetris/Desktop/HCI 2016/Deliverable 7/userData/database.p','wb'))