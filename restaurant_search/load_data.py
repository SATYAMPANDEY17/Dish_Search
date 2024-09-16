import pandas as pd
from search.models import Dish

data = pd.read_csv('restaurant_search\data\restaurants_small.csv')

for index, row in data.iterrows():
    Dish.objects.create(name=row['name'], description=row['description'])
