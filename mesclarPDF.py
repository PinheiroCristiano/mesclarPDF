from PyPDF2 import PdfFileMerger

pdfs = ["arq1.pdf", "arq2.pdf","arq3.pdf","arq4.pdf","arq5.pdf"]
arquivoSaida = "arquivoMesclado.pdf"

mesclar = PdfFileMerger()

for pdf in pdfs:
    mesclar.append(open(pdf, 'rb'))

with open(arquivoSaida, 'wb') as saida:
    mesclar.write(saida)
