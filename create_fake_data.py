import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'list_from_db.settings')
django.setup()

from faker import Faker
from main_app.models import DataModels

fake = Faker()


def fake_data(num=10):
    for _ in range(num):
        dt = DataModels()
        dt.name = fake.word()
        dt.save()
    print(f"Successfully created {num} datas.")


if __name__ == '__main__':
    fake_data()
