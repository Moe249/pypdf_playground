from PyPDF2 import PdfReader, PdfWriter
import PyPDF2

import sys

sys.tracebacklimit = 0


def encrypt(reader, writer):
    # open file and add pages to writer
    for page in reader.pages:
        writer.add_page(page)

    # Password
    print("Enter encryption password: ")

    password = input()
    # if password != Null:
    writer.encrypt(password)

    # reader.
    print("Metadata")
    title = reader.metadata.title

    # create file
    with open("encrypted files/${title}.pdf", "wb") as pdfFile:
        writer.write(pdfFile)

    print("File is encrypted successfully!")


def decrypt():
    # Let's Remove The password from the PDFs
    encryptedFilePath = "encrypted.pdf"

    new_reader = PdfReader(encryptedFilePath)

    # open with password
    if new_reader.is_encrypted:
        print("Enter encryption password: ")
        password = input()
        new_reader.decrypt(password)

    new_writer = PdfWriter()
    # open file and store pages in writer
    for page in new_reader.pages:
        new_writer.add_page(page)

    print("Decrypted file is created")

    # make file
    with open("decrypted files/decrypted.pdf", "wb") as pdfFile:
        new_writer.write(pdfFile)


filePath = "example.pdf"

reader = PdfReader(filePath)
writer = PdfWriter()

encrypt(reader, writer)

decrypt()
