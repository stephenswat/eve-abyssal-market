import tempfile
import requests
import bz2
import csv

from django.core.management.base import BaseCommand


SDE_BASE = 'https://www.fuzzwork.co.uk/dump/latest/'


class SDECommand(BaseCommand):
    def get_data_from_bz2_url(self, url):
        with tempfile.TemporaryFile() as tmp:
            tmp.write(requests.get(url).content)
            tmp.seek(0)

            with bz2.BZ2File(tmp, 'r') as uncompressed:
                data = uncompressed.read().decode()

        with tempfile.TemporaryFile(mode='w+t') as tmp:
            tmp.write(data)
            tmp.seek(0)

            for x in csv.DictReader(tmp):
                yield x

    def _create_helper(self, url, name, fun, total=None):
        count = 0

        print("Start creating %s..." % (name))

        for x in self.get_data_from_bz2_url(url):
            fun(x)
            count += 1

            if count % 10 == 0 or (total is not None and count == total):
                limit = "unknown" if total is None else str(total)
                print(
                    "    Progress: {count} out of approximately {limit}\r"
                    .format(count=count, limit=limit),
                    end=""
                )

        print("\nFinish creating %s (%d total)..." % (name, count))
