import os
from nbclient import NotebookClient
import nbformat

def run_notebooks(input_file):
    notebooks = [
        "app/notebooks/app.ipynb"
    ]
    
    output_dir = "data/"
    os.makedirs(output_dir, exist_ok=True)
    
    os.environ["INPUT_FILE"] = input_file
    os.environ["OUTPUT_DIR"] = output_dir
    
    for notebook in notebooks:
        print(f"Đang chạy {notebook} ...")
        nb = nbformat.read(notebook, as_version=4)
        client = NotebookClient(nb)
        client.execute()
    print("Hoàn tất xử lý!")
    return f"Kết quả lưu tại {output_dir}"
