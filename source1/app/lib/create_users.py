import csv
import os.path
import datetime
import random
from app.models import User, ActivityPeriod

class PopulateData(object):

    def read_file(self):
        my_path = os.path.abspath(os.path.dirname("__file__"))
        filepath = os.path.join(my_path, 'data.csv')
        self.add_data(filepath)

    def get_date(self):
        # Naively generating a random date
        day = random.randint(1, 28)
        month = random.randint(1, 12)
        year = random.randint(2016, 2020)
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        return datetime.datetime(year, month, day, hour, minute, second)

    def add_data(self, filename):
        f = open(filename, 'rb')
        with open(filename, 'r') as f:
            reader = csv.reader(f) 
            for row in reader:
                try:
                    data = {
                        "email": row[0],
                        "name": row[1]
                    }  
                    user_obj = User.objects.update_or_create(
                        email = data.get('email'),
                        name = data.get('name'),
                        defaults=data
                    )
                    for _ in range(3):
                        activity_obj = ActivityPeriod.objects.update_or_create(
                            user=user_obj[0],
                            start_time=self.get_date(),
                            end_time=self.get_date()
                        )
                except:
                    pass
