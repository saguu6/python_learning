import os
#need to set up the setting
os.environ.setdefault('DJANGO_SETTINGS_MODULE','fristproject.settings')

import django
django.setup()

##fake pop script
import random
from firstapp.models import AccessRecord,Topic,Webpage
from faker import Faker

fakegen = Faker()  #creating instace of Faker

topics = ['Search','social','marketplace','news','games']

def add_topic():
     t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
     t.save()
     return t

def populate(N=5):
    for entry in range(N):
        #get topic for enrty
        top = add_topic()

        #create the fake data for the entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create the new webpage enetry

        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #create a fake access record for that Webpage

        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete")
