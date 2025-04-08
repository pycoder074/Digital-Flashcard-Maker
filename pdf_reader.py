import requests
import PyPDF2
import os
import tempfile

def pdf_read(url: str):
    try:
        # Make the request to download the PDF
        r = requests.get(url, verify=False)
        r.raise_for_status()  # Raise an exception for bad responses

        # Check if the Downloads directory exists, if not, create it
        downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
        if not os.path.exists(downloads_dir):
            os.makedirs(downloads_dir)

        # Save the PDF content to a temporary file
        with tempfile.NamedTemporaryFile(delete=False) as tmp_pdf:
            tmp_pdf.write(r.content)
            tmp_pdf_path = tmp_pdf.name

        # Open the saved PDF and extract text
        with open(tmp_pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ""

            # Loop through each page and extract the text
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()

        # Print the extracted text or process it further
        if text:
            print("Text extracted from PDF:")
            with open('flashcards_text.txt', 'w', encoding = 'utf-8') as f:
                f.write(text)
        else:
            print("No text could be extracted from the PDF.")
        
        # Optionally delete the temporary file after use
        os.remove(tmp_pdf_path)

    except requests.exceptions.RequestException as e:
        print(f"Error downloading the PDF: {e}")
    except PyPDF2.errors.PdfReadError as e:
        print(f"Error reading the PDF: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

import csv

# Function to read the glossary from a text file and extract the terms and definitions
def extract_terms_from_txt(txt_file):
    try:
        # Open the text file and read the contents
        with open(txt_file, 'r', encoding='utf-8') as file:
            glossary_text = file.read()

        # Split the glossary text into lines and process each line
        terms_and_definitions = []
        for line in glossary_text.strip().split("\n"):
            # Split each line at the first hyphen to separate the term and definition
            if " - " in line:
                term, definition = line.split(" - ", 1)
                terms_and_definitions.append([term.strip(), definition.strip()])

        return terms_and_definitions

    except Exception as e:
        print(f"Error reading the file: {e}")
        return []

# Function to save extracted terms and definitions into a CSV file
def save_to_csv(terms_and_definitions, csv_filename):
    try:
        # Write the data to a CSV file
        with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Term", "Definition"])  # Write the header row
            writer.writerows(terms_and_definitions)  # Write the extracted term-definition pairs

        print(f"CSV file '{csv_filename}' created successfully.")

    except Exception as e:
        print(f"Error writing to CSV: {e}")

# File paths
txt_file = 'flashcards_text.txt'  # The input text file containing the glossary
csv_filename = 'glossary_terms.csv'  # The output CSV file name

# Extract terms and definitions from the text file
terms_and_definitions = extract_terms_from_txt(txt_file)

# If there were terms extracted, save them to CSV
if terms_and_definitions:
    save_to_csv(terms_and_definitions, csv_filename)
else:
    print("No terms were extracted from the text file.")

