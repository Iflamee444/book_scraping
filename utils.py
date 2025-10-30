import os
import pandas as pd
import requests as rq

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def download_file(url: str, path: str):
    ensure_dir(os.path.dirname(path))
    with rq.get(url, stream=True) as r:
        r.raise_for_status()
        with open(path, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)

def write_csv(data_list, file_path: str):
    ensure_dir(os.path.dirname(file_path))
    df = pd.DataFrame(data_list)
    df.to_csv(file_path, index=False, sep=";", encoding="utf-8-sig")
