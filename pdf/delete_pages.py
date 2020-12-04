'''
@author: Hongwei Shao
'''
from PyPDF2 import PdfFileReader, PdfFileWriter

import os
import argparse

def deletePages(in_pdf, pages):
    """
    docstring
    """
    out_pdf = PdfFileWriter()
    for i in range(in_pdf.getNumPages()):
        if i + 1 in pages:
            continue
        out_pdf.addPage(in_pdf.getPage(i))

    return out_pdf

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('input', help='Input pdf file.')
    arg_parser.add_argument('-p', '--pages', help="The pages to be deleted.", nargs='+', type=int)
    arg_parser.add_argument('-o', '--output', help="Output pdf file.")
    args = arg_parser.parse_args() 

    print(72 * "=")
    print("Deleting pages %s in %s..." % (str(args.pages), args.input))
    with open(args.input, 'rb') as input_stream:
        input_file = PdfFileReader(input_stream)
        filename = args.output
        if not filename:
            filename = args.input.replace('.pdf', 'with pages %s deleted.pdf') % str(args.pages)
        with open(filename, 'wb') as output_stream:
            output_file = deletePages(input_file, args.pages)
            output_file.write(output_stream)

    print("Pages deleted successfully.")
    print(72 * "=")
