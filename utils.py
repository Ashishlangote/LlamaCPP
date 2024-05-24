from docx import Document
import re
import uuid


def get_random_name():
    return uuid.uuid1()


def docx_process(filename):
    doc = Document(f'docx_files/{filename}.docx')
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)
