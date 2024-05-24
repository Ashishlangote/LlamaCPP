from llama_cpp import Llama
import json


def document_process(document):
    llm = Llama(
        model_path="/home/devuser/llama_cpp/model/Meta-Llama-3-70B-Instruct-v2.Q2_K.gguf",
        chat_format="llama-2",
        n_ctx=2048,
        n_threads=16,
        n_batch=8192,
        n_threads_batch=16,
        verbose=False
    )
    chat = llm.create_chat_completion(
        messages=[
            {
                "role": "user",
                "content": document
            }
        ],
        response_format={
            "type": "json_object",
        },
        max_tokens=4096,
        temperature=0,
    )
    output = [json.loads(chat["choices"][0]["message"]["content"])]
    return output
