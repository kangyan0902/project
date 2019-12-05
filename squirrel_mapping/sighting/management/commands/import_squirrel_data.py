import csv
from django.core.management import BaseCommand
from dateutil import parser
from sighting.models import Squirrel

class Command(BaseCommand):
    help = 'Import the squirrel csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            next(reader)
            unique_id = list()
            for row in reader:
                if row[2] in unique_id:
                    continue
                else:
                    squirrel = Squirrel.objects.get_or_create(
                            Latitude = float(row[0]),
                            Longitude = float(row[1]),
                            Unique_Squirrel_ID = row[2],
                            Shift = row[4],
                            Date = row[5],
                            Age = row[7],
                            Primary_Fur_Color = row[8],
                            Location = row[12],
                            Specific_Location = row[14],
                            Running = True if row[15] == 'TRUE' else False,
                            Chasing = True if row[16] == 'TRUE' else False,
                            Climbing = True if row[17] == 'TRUE' else False,
                            Eating = True if row[18] == 'TRUE' else False,
                            Foraging = True if row[19] == 'TRUE' else False,
                            Other_Activities = True if row[20] == 'TRUE' else False,
                            Kuks = True if row[21] == 'TRUE' else False,
                            Quaas = True if row[22] == 'TRUE' else False,
                            Moans = True if row[23] == 'TRUE' else False,
                            Tail_Flags = True if row[24] == 'TRUE' else False,
                            Tail_Twitches = True if row[25] == 'TRUE' else False,
                            Approaches = True if row[26] == 'TRUE' else False,
                            Indifferent = True if row[27] == 'TRUE' else False,
                            Runs_From = True if row[28] == 'TRUE' else False
                    )
                    unique_id.append(row[2])
