import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","intro_project.settings")

import django
django.setup()

import random
from intro_app.models import Topic,AccessRecord,WebPage
import faker

fake = faker.Faker()
topics = ["gaming","development","television","cinema","sports","business"]

def get_topic():
    t = Topic.objects.get_or_create(topic_name = random.choice(topics))[0]
    t.save()
    return t

def populate(n = 10):
    for entry in range(n):
        topic = get_topic()

        webpg = WebPage.objects.get_or_create(topic = topic, name = fake.name(), link = fake.url())[0]
        webpg.save()

        acc_record = AccessRecord.objects.get_or_create(name = webpg,date = fake.date())[0]
        acc_record.save()

if __name__=='__main__':
    print("populating")
    populate(15)
    print("done")