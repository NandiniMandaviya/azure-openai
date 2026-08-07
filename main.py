from parsing import run_parse_and_chunk
from creating_v_db import run_add_to_chroma_db

if __name__ == "__main__":
    run_parse_and_chunk()
    run_add_to_chroma_db()