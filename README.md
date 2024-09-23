# PDF Text Extractor

This Python script extracts text from PDF files in a specified directory and saves the extracted text as individual .txt files.

## Features
- Extracts text from multiple PDF files in a directory
- Attempts to extract the title from PDF metadata
- Removes headers and footers from extracted text
- Saves extracted text with cleaned filenames

## Requirements
- Python 3.x
- PyPDF2 library

## Installation

1. Clone this repository or download the `pdf_scraper.py` file.
2. Install the required library:
pip install PyPDF2


## Usage

Run the script from the command line with two arguments:

python pdf_scraper.py <input_directory> <output_directory>


- `<input_directory>`: The directory containing the PDF files you want to process
- `<output_directory>`: The directory where the extracted text files will be saved

Example: python pdf_scraper.py PDFs PDFs_scrapped


## How it works
The script performs the following steps:

1. Scans the input directory for PDF files
2. For each PDF file:
   - Extracts the title from metadata or first line of text
   - Extracts text from all pages
   - Removes headers and footers
   - Saves the extracted text to a .txt file in the output directory

## Limitations

- The header and footer removal assumes they are in the first and last lines of each page
- PDF files with complex layouts or embedded images may not extract perfectly

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or bug fixes.

## License

[MIT License](https://opensource.org/licenses/MIT)