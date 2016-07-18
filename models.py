from peewee import *

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop
db = PostgresqlDatabase('makaimark', user='makaimark')


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db



class CodecoolClass(BaseModel):
    location = CharField()
    year = DateTimeField()



class Person(BaseModel):
    first_name = CharField()
    last_name = CharField()
    year_of_birth = DateTimeField()
    gender = CharField()
    codecool_class = ForeignKeyField(CodecoolClass)



class Student(BaseModel, Person):
    nick_name = CharField()



class Mentor(BaseModel, Person):
    knowledge_level = IntegerField()
    energy_level = IntegerField()
