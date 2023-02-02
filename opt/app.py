import streamlit as st
import tempfile
from pathlib import Path
import os
def main():
    st.title("viewsmooth")
    st.caption("[View source code](https://github.com/na0ki-y/viewsmooth)")
    uploaded_file = st.file_uploader("Choose a file")
    files = os.listdir("/")
    print(files)
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            st.markdown("## Original PDF file")
            fp = Path(tmp_file.name)
            fp.write_bytes(uploaded_file.getvalue())
            st.write(tmp_file.name)

    title = st.text_input('filepath',"/home/user/prog/result/")

if __name__=="__main__":
    main()