import os
import pathlib
import shutil
import time

import requests
import streamlit as st

LIBRARY: dict[str, str] = {
    "Pride and Prejudice": "https://www.gutenberg.org/ebooks/1342.epub.noimages",
    "Les Miserables": "https://www.gutenberg.org/ebooks/135.epub.noimages",
}

LIBRARY_PATH: pathlib.Path = pathlib.Path.cwd() / "library"

st.title("RAG Librarian")

choices = st.multiselect(
    ":book: Choose your books",
    LIBRARY.keys(),
    default=LIBRARY.keys(),
)

if st.button("Download books from Project Gutenberg"):
    if LIBRARY_PATH.exists():
        shutil.rmtree(LIBRARY_PATH)

    LIBRARY_PATH.mkdir(parents=True, exist_ok=True)

    with st.spinner("Downloading..."):
        for choice in choices:
            url = LIBRARY[choice]
            fname = url.rsplit("/", 1)[1]
            dest_fname: str = os.path.splitext(fname)[0]
            r = requests.get(url, allow_redirects=True)
            (LIBRARY_PATH / dest_fname).open("wb").write(r.content)

    st.success("Done downloading!")
