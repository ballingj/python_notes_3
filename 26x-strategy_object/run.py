from ImportEngine import DocxImporter, CSVImporter
from ImportEngine import Importer, PDFImporter

print(DocxImporter.parse('./data/cats.docx'))
print(CSVImporter.parse('./data/cats.csv'))
print(PDFImporter.parse('./data/cats.pdf'))
