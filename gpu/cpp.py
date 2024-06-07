from llama_cpp import Llama
import json


def document_process(document):
    llm = Llama(
        model_path="/home/devuser/llama_cpp/model/Meta-Llama-3-70B-Instruct-v2.Q2_K.gguf",
        chat_format="llama-3",
        n_ctx=4096,
        n_gpu_layers=-1,
        n_batch=4096,
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
