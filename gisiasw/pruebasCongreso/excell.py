import xlsxwriter
from testSyERySM import get_values

def generate_book(ws, data, formatt):

    row = 0
    ws.write(row, 0, "Tabla de Similitudes entre Claves y Entidades dados una URL")
    row +=3
    for i, g in enumerate(data):
        ws.write(row, 0, "URL:  " + g.get("url"), formatt)
        cols = len(g.get("entities"))
        row += 1
        ws.write(row, 0, "Clave \ Entidad ", formatt)
        for cl in range(cols):
            crow = row
            ws.write(row, cl + 1, g.get("entities")[cl], formatt)
            crow += 1
            for l, m in enumerate(g.get("meassures")):
                ws.write(crow, 0, m.get("k"), formatt)
                if (g.get("entities")[cl] == m.get("e")):
                    ws.write(crow, cl + 1, max(m.get("value")))
                    crow += 1

        row += 7

# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('congreso.xlsx')

try:

    values = get_values()
    google = values.get("google")
    bing = values.get("bing")
    bold = workbook.add_format({'bold': True})
    worksheet = workbook.add_worksheet("google")
    generate_book(worksheet, google, bold)
    worksheet2 = workbook.add_worksheet("bing")
    generate_book(worksheet2, bing, bold)

    workbook.close()
except Exception, e:
    print(e)
    workbook.close()
