from models import *
import build

# Populate random data with your models


codecool_bp_1 = CodecoolClass.create(location='Budapest', year=2016)

mentor_1 = Mentor.create(first_name='Salamon', last_name='Daniel'. year_of_birth=1992,
                            gender='male', codecool_bp_1, nickname='Dani')
mentor_1.save()
mentor_1.insert()  # necessary??
