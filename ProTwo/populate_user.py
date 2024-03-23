import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","ProTwo.settings")

import django
django.setup()

import faker
from AppTwo.models import User

fake = faker.Faker()

def populate(n=10):
    for entry in range(n):
        first_name = str(fake.name()).split()[0]
        last_name = str(fake.name()).split()[1]
        email = fake.email()

        user = User.objects.get_or_create(first_name = first_name, last_name=last_name,email=email)[0]
        user.save()

if __name__=='__main__':
    print("populating")
    populate()
    print("done")