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
        cols = len(g.get("entities"))
        row += 1
        #ws.write(row, 0, "Clave \ Entidad ", formatt)
        ws.merge_range(row, 0, row +  2, 0, "Clave \ Entidad ", formatt)
        clss = 0
        worksheet.set_column(0, cols, width=20)
        for cl in range(0, cols):

            crow = row
            print(g.get("entities")[clss]["name"])
            print("COLS: {0} - {1}".format(clss, cols))
            #ws.merge_range(row, cl + 1, row, cl + 1, g.get("entities")[clss]["name"], merged_format)
            ws.write(row, cl + 1, g.get("entities")[clss]["name"], formatt)
            crow += 1
            ws.write(row+1, cl + 1, "Relevance: {0}".format(str(g.get("entities")[clss]["relevance"])),
                           formatt)
            #ws.write(row, cl + 1, g.get("entities")[clss]["name"], formatt)
            crow += 1
            ws.write(row + 2, cl + 1,
                           "Wiki: {0}".format(str(g.get("entities")[clss]["wiki"])),
                           formatt)
            crow += 1
            for l, m in enumerate(g.get("meassures")):
                print(g.get("entities")[clss]["name"], m.get("e"))
                if (g.get("entities")[clss]["name"] == m.get("e")):
                    ws.write(crow, 0,
                             m.get("k"),
                             formatt)
                    ws.write(crow, cl + 1,
                             m.get("ratio"),
                             formatt)
                    crow += 1
            clss += 1

        row += 8


keyss = [#{"it":["'machine learning'"], "keys":["machine_learning"]},
          #{"it": ["'machine learning'","python"], "keys": ["machine_learning","python"]},
          {"it": ["'machine learning'","python", "algorithms"], "keys": ["Machine_learning","Python_(programming_language)", "Algorithms"]}]

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
    finally:
        workbook.close()
