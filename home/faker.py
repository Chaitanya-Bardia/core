from .models import *
from faker import Faker
import random

fake = Faker()

def generate_data(n=10)->bool:
    [Student.objects.create(
        name = fake.name(),
        age = random.randint(18,40),
        address = fake.address(),
        father_name = fake.name()
    )for i in range(0,n)]
    return True