import os
import pdfkit
import zipfile

options = {
    'dpi': 365,
    'page-size': 'A1',
    'margin-top': '0.25in',
    'margin-right': '0.25in',
    'margin-bottom': '0.25in',
    'margin-left': '0.25in',
    'javascript-delay': 1000,  # add delay to allow SVG to render fully
    'enable-local-file-access': None  # allow wkhtmltopdf to access local files
}

directory = 'svgs'

for filename in os.listdir(directory):
    postcodes = []
    fzip = os.path.join(directory, filename)
    # checking if it is a file

    if os.path.isfile(fzip) and '.zip' in fzip:
        # print(fzip)
        print("aa")
        with zipfile.ZipFile(fzip, 'r') as zip_ref:
            zip_ref.extractall(fzip.split('.')[0])
            directory_file = fzip.split('.')[0]
            print(".")
            for ff in os.listdir(directory_file):
                # print(ff)
                postcodes = []
                f = os.path.join(directory_file, ff)
                # print(f)
                # checking if it is a file
                if os.path.isfile(f) and '.svg' in f:
                    # print(f)
                    wkhtml_path = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')

                    pdfkit.from_file(f, f.split('.')[0] + '.pdf', configuration=wkhtml_path, options=options)
                    print("...")

