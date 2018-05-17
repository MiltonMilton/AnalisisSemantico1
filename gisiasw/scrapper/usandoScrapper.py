from Scrapper import Scrapper

s = Scrapper()

url = 'https://www.24siete.info/nota-238175-economia-las_posibles_condiciones_del_fmi_para_realizar_el_acuerdo_con_argentina.html'

texto = s.buscarHTML('noticia',url)

print(texto)