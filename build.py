# This script can create the database tables based on your models

from models import *

'''def connection(database):
    database.connect()
    # List the tables here what you want to create...
    database.create_tables([Person, Mentor, Student, CodecoolClass], safe=True)
'''

'''database.connect()
    # List the tables here what you want to create...
    database.create_tables([Person, Mentor, Student, CodecoolClass], safe=True)'''

db.connect()
db.create_tables([Person, Mentor, Student, CodecoolClass], safe=True)