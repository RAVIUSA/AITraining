file_name = ["sample.pdf", "report.docx", "presentation.pptx", "data.xlsx", "notes.txt", "DATA.PDF"]
pdf_files = []

for i in file_name:
    if i.endswith(".pdf") or i.endswith(".PDF"):    # "sample.pdf".endswith(".pdf")  # True
        pdf_files.append(i)

print("PDF files in the list are:", pdf_files)


doc_files = []
ppt_files = []

# function endswith , startswith
for i in file_name:
    if i.endswith(".pdf") or i.endswith(".PDF"):    # "sample.pdf".endswith(".pdf")  # True
        pdf_files.append(i)
    elif i.endswith(".docx") or i.endswith(".DOCX"):
        doc_files.append(i)
    elif i.endswith(".pptx") or i.endswith(".PPTX"):
        ppt_files.append(i)


print("PDF files in the list are:", pdf_files)
print("DOCX files in the list are:", doc_files)
print("PPTX files in the list are:", ppt_files)
