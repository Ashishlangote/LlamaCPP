from llama_cpp import Llama


def docx_process_file(prompt_text):
    llm = Llama(
        model_path="/mnt/data/llama_cpp/models/Meta-Llama-3-8B-Instruct-v2.Q8_0.gguf",
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
                "content": prompt_text
            }
        ],
        max_tokens=4096,
        temperature=0,
    )
    output = chat["choices"][0]["message"]["content"]
    return output.replace('\n', '<br>')
