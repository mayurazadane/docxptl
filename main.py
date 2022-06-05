# for creating automated documents from template doc
from docxtpl import DocxTemplate, InlineImage

personName = ['Akash', 'Ankush', 'Aayushi', 'Mohit', 'Shlok', 'Aastha', 'Pooja']

for pItr, p in enumerate(personName):
    doc = DocxTemplate("inviteTemp.docx")  # template document
    context = {
        "todayStr": "21/12/2021",
        "recipientName": p,
        # "recipientName" : "John Doe",
        "evntDtStr": "25st December, 2021",
        "venueStr": "the beach",
        "senderName": "Hayley Shah",
        "bannering": InlineImage(doc, "party.jpg")
    }
    doc.render(context)
    doc.save("invites/invitation_{0}.docx".format(pItr))
