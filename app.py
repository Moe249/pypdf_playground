from PyPDF2 import PdfReader, PdfWriter
import PyPDF2

import sys

sys.tracebacklimit = 0


def encrypt(reader, writer):
    # open file and add pages to writer
    for page in reader.pages:
        writer.add_page(page)

    # Insert password from user
    print("Enter encryption password: ")

    password = input()
    writer.encrypt(password)

    path = "encrypted files/" + reader.metadata.title + ".pdf"
    # create file
    with open(path, "wb") as pdfFile:
        writer.write(pdfFile)

    print("Your file is encrypted successfully!")
    print("Find the file at: ({})".format(path))

    return path


def decrypt(path):
    # Let's Remove The password from the PDFs
    encryptedFilePath = path

    new_reader = PdfReader(encryptedFilePath)

    # open with password
    if new_reader.is_encrypted:
        print("Enter decryption password: ")
        password = input()
        new_reader.decrypt(password)

    new_writer = PdfWriter()
    # open file and store pages in writer
    for page in new_reader.pages:
        new_writer.add_page(page)
    decryptedFilePath = "decrypted files/" + reader.metadata.title + ".pdf"
    # make file
    with open(decryptedFilePath, "wb") as pdfFile:
        new_writer.write(pdfFile)

    print("Your file is decrypted successfully!")
    print("Find the file at: ({})".format(decryptedFilePath))


filePath = "example.pdf"

reader = PdfReader(filePath)
writer = PdfWriter()

encryptedFilePath = encrypt(reader, writer)

decrypt(encryptedFilePath)
