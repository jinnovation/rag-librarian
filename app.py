import streamlit as st
import time

LIBRARY: dict[str, str] = {
    "Pride and Prejudice": "https://www.gutenberg.org/ebooks/1342.epub.noimages",
    "Les Miserables": "https://www.gutenberg.org/ebooks/135.epub.noimages",
}

st.title("RAG Librarian")

st.multiselect(
    ":book: Choose your books",
    LIBRARY.keys(),
    default=LIBRARY.keys(),
)


if st.button("Download books"):
    download_progress_bar = st.progress(
        0, text="Downloading books from Project Gutenberg..."
    )
    for percent_complete in range(100):
        time.sleep(0.01)
        download_progress_bar.progress(
            percent_complete + 1, text="Downloading books from Project Gutenberg..."
        )


x = st.slider("Select a value")
st.write(x, "squared is", x * x)
