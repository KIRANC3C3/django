from fpdf import FPDF
x=int(input("how many pdf's do you need?"))
for i in range(x):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', '', 16)
    pdf.cell(40, 10, 'hello ra')
    pdf.output('Test{}.pdf'.format(i), 'F')



