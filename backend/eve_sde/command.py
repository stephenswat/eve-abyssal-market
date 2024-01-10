import tempfile
import requests
import bz2
import csv
import tqdm

from django.core.management.base import BaseCommand


SDE_BASE = "https://www.fuzzwork.co.uk/dump/latest/"


class SDECommand(BaseCommand):
    def _create_helper(self, url, name, fun):
        count = 0

        print("Start creating %s..." % (name))

        with tempfile.TemporaryFile() as tmp:
            tmp.write(requests.get(url).content)
            tmp.seek(0)

            with bz2.BZ2File(tmp, "r") as uncompressed:
                data = uncompressed.read().decode()

        with tempfile.TemporaryFile(mode="w+t") as tmp:
            tmp.write(data)
            tmp.seek(0)

            reader = csv.DictReader(tmp)

            for x in tqdm.tqdm(reader):
                fun(x)

        print("\nFinish creating %s..." % (name))
