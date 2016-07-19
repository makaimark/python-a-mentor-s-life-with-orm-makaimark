from peewee import *

# Configure your database connection here
# database name = should be your username on your laptop
# database user = should be your username on your laptop

db = PostgresqlDatabase('orm_project', user='makaimark')


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db

class CodecoolClass(BaseModel):
    location = CharField()
    year = IntegerField()

    def mentors(self):
        return self.mentorlist

    def students(self):
        return self.studentlist



class Person(BaseModel):
    first_name = CharField()
    last_name = CharField()
    year_of_birth = DateField()
    gender = CharField()


class Student(Person):
    knowledge_level = IntegerField()
    energy_level = IntegerField()
    codecool_class = ForeignKeyField(CodecoolClass, related_name='studentlist')



class Mentor(Person):
    nickname = CharField()
    codecool_class = ForeignKeyField(CodecoolClass, related_name='mentorlist')


