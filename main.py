import shutil
import os
from prompt import *
from fastapi import FastAPI, UploadFile, Form
from process import docx_process_file
from cpp import document_process
from utils import get_random_name, docx_process

app = FastAPI(title='Llama-2 | API')

docx_folder = "docx_files"
os.makedirs(docx_folder, exist_ok=True)


@app.post("/upload_file")
async def upload_file(file: UploadFile, prompt: str = Form()):
    random_name = str(get_random_name())
    file_path = os.path.join(docx_folder, f'{random_name}.docx')
    with open(file_path, "wb") as file_object:
        shutil.copyfileobj(file.file, file_object)
    text = docx_process(random_name)
    prompt_txt = affiliation2(text, prompt)
    data = docx_process_file(prompt_txt)
    return {'original': text.replace('\n', '<br>'), 'output': data}


@app.post("/file")
async def output_json(file: UploadFile):
    random_name = str(get_random_name())
    file_path = os.path.join(docx_folder, f'{random_name}.docx')
    with open(file_path, "wb") as file_object:
        shutil.copyfileobj(file.file, file_object)
    text = docx_process(random_name)
    prompt_txt = affiliation3(text)
    data = document_process(prompt_txt)
    return data
