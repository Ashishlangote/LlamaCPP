from llama_cpp import Llama


def docx_process_file(prompt_text):
    llm = Llama(
        model_path="/home/devuser/llama_cpp/model/Meta-Llama-3-70B-Instruct-v2.Q2_K.gguf",
        chat_format="llama-3",
        n_ctx=8192,
        n_threads=16,
        n_batch=8192,
        n_threads_batch=16,
        verbose=False
    )
    chat = llm.create_chat_completion(
        messages=[
            {
                "role": "user",
                "content": prompt_text
            }
        ],
        max_tokens=8192,
        temperature=0,
    )
    output = chat["choices"][0]["message"]["content"]
    return output.replace('\n', '<br>')
