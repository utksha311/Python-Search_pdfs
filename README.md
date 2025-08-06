# Python-Search_pdfs
Python Streamlit script to search for specific strings within all the .pdf files in a given directory and its subdirectories

The search is performed efficiently using multithreading to process multiple PDF files concurrently.

Features
 - Interactive Web Interface: A simple and clean user interface built with Streamlit.
 - Recursive Search: Automatically searches all subdirectories for PDF files.
 - Multithreaded Performance: Uses Python's ThreadPoolExecutor to speed up the searching process, especially for a large number of files.
 - Case-Insensitive Matching: The search function is case-insensitive, ensuring it finds matches regardless of capitalization.
 - Detailed Results: Displays the name of each matching file along with the specific page numbers where the string was found.
 - Robust Error Handling: Skips and reports on any corrupted or unreadable PDF files without stopping the entire process.

Prerequisites:
install streamlit PyPDF2

Code Overview:
 - search_string_in_pdf(directory, search_string): The main function that orchestrates the search. It uses os.walk to find all PDF files and submits each file to the ThreadPoolExecutor for processing.
 - search_string_in_pdf_content(pdf_file, search_string): This function is executed by a separate thread for each PDF. It opens the file, extracts text page by page using PyPDF2, and returns a dictionary of found page numbers.
 - main(): The Streamlit entry point. It sets up the UI elements like the title, text inputs, and a search button, and displays the results.
