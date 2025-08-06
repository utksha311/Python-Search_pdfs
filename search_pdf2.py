#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
from PyPDF2 import PdfReader
from concurrent.futures import ThreadPoolExecutor
import streamlit as st

def search_string_in_pdf(directory, search_string):
    matching_files = {}
    with ThreadPoolExecutor() as executor:
        futures = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.pdf'):
                    file_path = os.path.join(root, file)
                    futures.append(executor.submit(search_string_in_pdf_content, file_path, search_string))
        for future in futures:
            matching_pages = future.result()
            if matching_pages:
                for file, page_nums in matching_pages.items():
                    if file in matching_files:
                        matching_files[file].extend(page_nums)
                    else:
                        matching_files[file] = page_nums
    return matching_files

def search_string_in_pdf_content(pdf_file, search_string):
    matching_pages = {}
    try:
        with open(pdf_file, 'rb') as file:
            reader = PdfReader(file)
            for page_num, page in enumerate(reader.pages, start=1):
                text = page.extract_text()
                if text and search_string.lower() in text.lower():
                    if pdf_file in matching_pages:
                        matching_pages[pdf_file].append(page_num)
                    else:
                        matching_pages[pdf_file] = [page_num]
    except Exception as e:
        st.error(f"Error processing {pdf_file}: {e}")
    return matching_pages

def main():
    st.title("PDF Search App")

    search_directory = st.text_input("Enter the directory path to search in:")
    search_string = st.text_input("Enter the string to search for:")

    if st.button("Search"):
        if search_directory and search_string:
            matching_files = search_string_in_pdf(search_directory, search_string)
            if matching_files:
                st.write("Matching files found:")
                for file, page_nums in matching_files.items():
                    file_name = os.path.basename(file)
                    page_nums_str = ', '.join(str(page_num) for page_num in page_nums)
                    st.markdown(f"**{file_name}** [{page_nums_str}]")
            else:
                st.write("No matching files found.")
        else:
            st.error("Please provide both directory path and search string.")

if __name__ == "__main__":
    main()

