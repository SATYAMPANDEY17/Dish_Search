import pandas as pd
from django.core.management.base import BaseCommand
from search.models import Dish

class Command(BaseCommand):
    help = 'Load data from CSV file into the database'

    def handle(self, *args, **kwargs):
        data = pd.read_csv(r'C:\Users\Dell\Desktop\search\restaurant_search\data\restaurants_small.csv')
        for index, row in data.iterrows():
            Dish.objects.get_or_create(name=row['name'], defaults={'description': row['full_details']})
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
