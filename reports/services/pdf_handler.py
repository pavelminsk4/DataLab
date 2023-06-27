import aspose.words as aw

lic = aw.License()

#Try to set license from the folder with the python script.
try :
    lic.set_license("Aspose.Total.Product.Family.lic")
    print("License set successfully.")
except RuntimeError as err :
    # We do not ship any license with this example, visit the Aspose site to obtain either a temporary or permanent license.
    print("\nThere was an error setting the license: {0}".format(err))

def convert_docx_to_pdf(docx_path, report_path):
  doc = aw.Document(docx_path)
  doc.save(report_path)
