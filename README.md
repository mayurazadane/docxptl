# Docxptl

## Creating automated reports from templates using docxptl libraries in Python

The packages used are :
1. python-docx for reading, writing and creating sub documents
2. jinja2 for managing tags inserted into the template docx

python-docx-template has been created because python-docx is powerful for creating documents but not for modifying them.

The idea is to begin to create an example of the document you want to generate with microsoft word, it can be as complex as you want : pictures, index tables, footer, header, variables, anything you can do with word. Then, as you are still editing the document with microsoft word, you insert jinja2-like tags directly in the document. You save the document as a .docx file (xml format) : it will be your .docx template file.

Now you can use python-docx-template to generate as many word documents you want from this .docx template and context variables you will associate.

Here in the code - 
inviteTemp.docx - is the template word document.
invites folder - has generated result documents from code.
