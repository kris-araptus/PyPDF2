import os
import argparse
from PyPDF2 import PdfReader
import re

def extract_title_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        if '/Title' in reader.metadata:
            return reader.metadata['/Title']
        else:
            # If no title in metadata, use the first line of the first page
            first_page_text = reader.pages[0].extract_text()
            first_line = first_page_text.split('\n')[0].strip()
            return first_line if first_line else os.path.splitext(os.path.basename(pdf_path))[0]

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text = ''
        for page in reader.pages:
            page_text = page.extract_text()
            # Remove header and footer (assuming they're in the first and last lines)
            lines = page_text.split('\n')
            if len(lines) > 2:
                cleaned_text = '\n'.join(lines[1:-1])
            else:
                cleaned_text = page_text
            text += cleaned_text + '\n'
    return text

def clean_filename(filename):
    return re.sub(r'[^\w\-_\. ]', '_', filename)

def process_pdfs_in_directory(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_dir, filename)
            title = extract_title_from_pdf(pdf_path)
            text = extract_text_from_pdf(pdf_path)
            
            # Save extracted text to a file named after the PDF title
            output_filename = clean_filename(title) + '.txt'
            output_path = os.path.join(output_dir, output_filename)
            
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(f"Title: {title}\n\n")
                output_file.write(text)
            
            print(f"Processed: {filename} -> {output_filename}")

def main():
    parser = argparse.ArgumentParser(description="Extract text from PDF files in a directory.")
    parser.add_argument("input_dir", help="Directory containing PDF files")
    parser.add_argument("output_dir", help="Directory to save extracted text files")
    args = parser.parse_args()

    # Use the current working directory as the base for both input and output directories
    current_dir = os.getcwd()
    input_dir = os.path.join(current_dir, args.input_dir)
    output_dir = os.path.join(current_dir, args.output_dir)

    process_pdfs_in_directory(input_dir, output_dir)
    print("Text extraction completed.")

if __name__ == "__main__":
    main()
