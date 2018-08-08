import xlsxwriter
from testSyERySM import get_values

def generate_book(ws, data, formatt, merged_format):
    alg = ["wup", "sde", "lin", "path"]
    row = 0
    ws.write(row, 0, "Tabla de Similitudes entre Claves y Entidades dados una URL")

    row +=3
    for i, g in enumerate(data):
        print(g.get("entities"))
        ws.write(row, 0, "URL:  " + g.get("url"), formatt)
        cols = len(g.get("entities")) * 4
        row += 1
        ws.write(row, 0, "Clave \ Entidad ", formatt)
        ws.merge_range(row, 0, row +  3, 0, "Clave \ Entidad ", formatt)
        clss = 0
        for cl in range(0, cols, 4):

            crow = row
            print(g.get("entities"))
            print("COLS: {0} - {1}".format(clss, cols))
            ws.merge_range(row, cl + 1, row, cl + 4, g.get("entities")[clss]["name"], merged_format)
            #ws.write(row, cl + 1, g.get("entities")[clss], formatt)
            crow += 1
            ws.merge_range(row+1, cl + 1, row+1, cl + 4, "Relevance: {0}".format(str(g.get("entities")[clss]["relevance"])),
                           merged_format)
            crow += 1
            ws.merge_range(row + 2, cl + 1, row + 2, cl + 4,
                           "Wiki: {0}".format(str(g.get("entities")[clss]["wiki"])),
                           merged_format)
            crow += 1
            for l in range(0,4):
                ws.write(crow, cl + 1 + l, alg[l], formatt)
            crow += 1
            for l, m in enumerate(g.get("meassures")):
                if (g.get("entities")[clss]["name"] == m.get("e")):
                    ws.write(crow, 0, m.get("k"), formatt)
                    for l, v in enumerate(m.get("value")):
                        ws.write(crow, cl + 1 + l, v)
                    crow += 1
            clss += 1

        row += 8


keyss = [{"it":["'machine learning'"], "keys":["machine_learning"]},
          {"it": ["'machine learning'","python"], "keys": ["machine_learning","python"]},
          {"it": ["'machine learning'","python", "algorithms"], "keys": ["machine_learning","python", "algorithms"]}]

for i,key in enumerate(keyss):
    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook('congreso_{0}.xlsx'.format(i))
    try:
        print("<<<<<<<INITIALIZING PROCESS>>>>>>>")
        values = get_values(key=key)
        google = values.get("google")
        bing = values.get("bing")
        bold = workbook.add_format({'bold': True})
        merge_format = workbook.add_format({
                'bold':     True,
                'border':   6,
                'align':    'center',
                'valign':   'vcenter',
                'fg_color': '#D7E4BC',
            })
        worksheet = workbook.add_worksheet("google")
        generate_book(worksheet, google, bold, merge_format)
        worksheet2 = workbook.add_worksheet("bing")
        generate_book(worksheet2, bing, bold, merge_format)

        workbook.close()
    except Exception, e:
        print(e)
        workbook.close()
