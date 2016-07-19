# This script can create the database tables based on your models

from models import *

<<<<<<< HEAD
'''def connection(database):
    database.connect()
    # List the tables here what you want to create...
    database.create_tables([Person, Mentor, Student, CodecoolClass], safe=True)
'''

'''database.connect()
    # List the tables here what you want to create...
    database.create_tables([Person, Mentor, Student, CodecoolClass], safe=True)'''
=======
>>>>>>> f68c22ec23ba3a988d6ea210742dec0b709c9f10

db.connect()
db.create_tables([Person, Mentor, Student, CodecoolClass], safe=True)