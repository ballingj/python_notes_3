'''
pip install -U setuptools
pip install python-docx 
'''

'''
# /ImportEngine/Cat.py

class Cat():
    def __init__(self, name, age, isIndoor=True):
        self.name = name
        self.age = age
        self.isIndoor = isIndoor

    def speak(self):
        print(f'rrr"')
    
    def __repr__(self):
        return f'<{self.name}, {self.age}, {self.isIndoor}>'


# /ImportEngine/ImportInterface.py

from abc import ABC, abstractmethod

from typing import List
from .Cat import Cat

class ImportInterface(ABC):

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[Cat]:
        pass


# /ImportEngine/DocxImporter.py

from typing import List
import docx

from .ImportInterface import ImportInterface
from .Cat import Cat

class DocxImporter(ImportInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        cats = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(',')
                new_cat = Cat(parse[0], int(parse[1]), bool(parse[2]))
                cats.append(new_cat)

        return cats


# /ImportEngine/CSVImporter.py
# pip install pandas

from typing import List
import pandas

from .ImportInterface import ImportInterface
from .Cat import Cat

class CSVImporter(ImportInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        cats = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_cat = Cat(row['Name'], row['Age'], row['isIndoor'])
            cats.append(new_cat)

        return cats

# /ImportEngine/Importer.py

from typing import List

from .ImportInterface import ImportInterface
from .Cat import Cat
from .DocxImporter import DocxImporter
from .CSVImporter import CSVImporter


class Importer(ImportInterface):
    importers = [DocxImporter, CSVImporter]

    @classmethod
    def parse(cls, path: str) -> List[Cat]:
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)



# run.py

#from ImportEngine import DocxImporter, CSVImporter
from ImportEngine import Importer

# print(DocxImporter.parse('./data/cats.docx'))
# print(CSVImporter.parse('./data/cats.csv'))

print(Importer.parse('./data/cats.csv'))
print(Importer.parse('./data/cats.docx'))


# /ImportEngine/__init__py

from .DocxImporter import DocxImporter
from .CSVImporter import CSVImporter
from .Importer import Importer


#  /ImportEngine/PDFImporter.py

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

'''
