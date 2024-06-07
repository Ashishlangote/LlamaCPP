from llama_cpp import Llama
from docx import Document
import json


def docx_process(filename):
    doc = Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)


text = docx_process("docs.docx")
json_schema = '''{"authors":[{"author":"","authorPrefix":"","authorSuffix":"","authorDegrees":"","affiliation":[{"affiliationId":"","correspondingAuthor":"","department":"","organization":"","street":"","city":"","state":"","postalCode":"","country":"","email":"","phone":""},{"affiliationId":"","correspondingAuthor":"","department":"","organization":"","street":"","city":"","state":"","postalCode":"","country":"","email":"","phone":""}]}]}'''
prompt = f"""{text}\nGiven above content is manuscript, accurately identify and categorize information regarding authors and their affiliations. Extract details such as author names, their contributions, and affiliations, including author prefix, suffix, and degrees accompanying the author name. Affiliation details are typically located following the author's name and are indicated by footnote or endnote numbers. Specifically categorize each affiliation into Department, Organization, Street, Postal-code, City, State, and Country if present. Provide a structured output with a list of authors, and for each author, ensure that all affiliations are captured as a list, including all relevant details such as affiliation ID, corresponding author status, department, organization, street, city, state, postal code, country, email, and phone number. Use the provided template for the output JSON structure:{json_schema}"""

llm = Llama(
    model_path="/mnt/data/llama_cpp/models/Meta-Llama-3-8B-Instruct-v2.Q8_0.gguf",
    chat_format="llama-3",
    n_ctx=4096,
    n_gpu_layers=-1,
    n_batch=4096,
    verbose=True
)
chat = llm.create_chat_completion(
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    response_format={
        "type": "json_object"
    },
    max_tokens=4096,
    temperature=0,
)
data = json.loads(chat["choices"][0]["message"]["content"])
print(data)