"""
pip install -U setuptools
pip install python-docx 
pip install pandas

sudo apt-get install -y xpdf
"""


from typing import List
import subprocess
import os
import random

from .ImportInterface import ImportInterface
from .Cat import Cat


class PDFImporter(ImportInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        tmp = f'./tmp/{random.randint(0,100000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r")
        cats = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split(',')
                new_cat = Cat(parse[0], int(parse[1]), bool(parse[2]))
                cats.append(new_cat)

        file_ref.close()
        os.remove(tmp)
        return cats
