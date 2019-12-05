from django.core.management.base import BaseCommand, CommandError
from sighting.models import Squirrel
from sighting.models import get_model
import csv
import sys

class Command(BaseCommand):
    help = ("Output the squirrel data as CSV")

    def handle(self, *args, **kwargs):
        model = get_model(sighting, Squirrel)
        field_names = [f.name for f in model._meta.fields]
        writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL)
        writer.writerow(field_names)
        for instance in model.objects.all():
            writer.writerow([unicode(getattr(instance, f)).encode('utf-8') for f in field_names])