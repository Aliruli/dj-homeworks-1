import csv
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    """Создаем класс, для импорта объектов \
        (телефонов) из файла ".CSV"

    """
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        """Функция чтения файла ".CSV", \

            которая производит открытие файла, \

                проходит по его ключам и значениям, а также сохраняет \

                    полученное в базу данных.

        """
        with open('phones.csv', 'r') as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                id = line[0]
                name = line[1]
                price = line[2]
                image = line[3]
                release_date = line[4]
                lte_exists = line[5]

                Phone.objects.create(
                    id=id,
                    name=name,
                    price=price,
                    image=image,
                    release_date=release_date,
                    lte_exists=lte_exists
                    )

                self.stdout.write(self.style.SUCCESS(f'Создана успешно \
                                                     "{name}"'))
