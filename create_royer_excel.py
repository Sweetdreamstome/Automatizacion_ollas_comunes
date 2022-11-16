import pandas as pd
import os
import requests
# import urllib
from bs4 import BeautifulSoup as bs
from datetime import datetime
#Tratar de descargar un excel desde una página web:
#webscrapping
#el problema con python es que no lee javascript y usualmente los archivos de excel o adicionales estan relacionados a javascript,
#lo que hace el codigo es parsear el html y extraer el ".xls" que este en la página web

# def get_soup(url):
#     response = requests.get(url)
#     #print(response.status_code)
#     #print(response.text)
#     html = response.text
#     soup = bs(html, 'html.parser')
#     #soup = bs(html, 'lxml')
#     #soup = bs(html, 'html5lib')
#     return soup

# DOMAIN = 'https://lfportal.loudoun.gov/LFPortalinternet/'
# URL = 'https://lfportal.loudoun.gov/LFPortalinternet/Browse.aspx?startid=213973&row=1&dbid=0'
# FILETYPE = '.xls'

# soup = get_soup(URL)
# for folder_link in soup.find_all('a', {'class': 'DocumentBrowserNameLink'}):
#     folder_name = folder_link.get('aria-label').split(' ')[0]
#     folder_link = folder_link.get('href')

#     print('folder:', folder_name)
#     os.makedirs(folder_name, exist_ok=True)
    
#     subsoup = get_soup(DOMAIN + folder_link)
#     for file_link in subsoup.find_all('a', {'class': 'DocumentBrowserNameLink'}):
#         file_name = file_link.get('aria-label')[:-4] 
#         file_link = file_link.get('href')
        
#         if file_link.endswith(FILETYPE):
#             print('  file:', file_name)
#             file_name = os.path.join(folder_name, file_name)
#             with open(file_name, 'wb') as file:
#                 response = requests.get(DOMAIN + file_link)
#                 file.write(response.content)

#abrir data localmente
df_formulario = pd.read_excel (
      os.path.join("C:/Users/avill/Downloads","UP Ollas Comunes - Municipalidad de Lima (Respuestas).xlsx"),
      engine='openpyxl',
 )
#print(df_formulario)
#tiene 158 filas y 71 columnas
df_royer = pd.read_excel (
      os.path.join("C:/Users/avill/Downloads","Para Royer 22.09.xlsx"),
      engine='openpyxl',
 )
# print(df_royer)
#filtrar solamente los que tengan i)link de fotos, ii)link de ubicación, iii)coordenadas
df_formulario = df_formulario.dropna(subset=[68]) 
df_formulario = df_formulario.dropna(subset=[69]) 
df_formulario = df_formulario.dropna(subset=[70]) 
df_formulario = df_formulario.dropna(subset=[71]) 

#quedan 63 filas, identificador celular, buscar valores diferentes y crear df que solo tenga estos valores
#columna en formulario: 11, royer: 13
df_formulario = df_formulario.dropna(subset=[11]) 
# df_royer.loc[df_royer[13] == '968541725']
# print(968541725 in set(df_formulario[11]))
# print(967093450 in set(df_royer[13]))

for y in df_formulario[11]:
      if y in set(df_royer[13]):
            df_formulario.drop(df_formulario.loc[df_formulario[11]==y].index, inplace=True)
            
#transcribir los valores nuevos al excel de royer
#crear lista con valores en el orden deseado y ordenar los valores necesarios:
#antes de realizar esta lista, se debe diferenciar si es una olla activada o desactivada, para ver si solo se agrega el celular y el 3. 
#hallar id:
df_royer = df_royer.dropna(subset=[1]) 
id1 = df_royer.iloc[len(df_royer.index) - 1][1] + 1
correo = "---"
distrito = int(df_formulario.iloc[1][4].split('-')[0])
zona = df_formulario.iloc[1][5]
AAHH = df_formulario.iloc[1][6]
ubicacion_exacta = df_formulario.iloc[1][7]
agua = df_formulario.iloc[1][24]
fecha_creacion_olla = "---"
luz = df_formulario.iloc[1][25]
nombre_olla = df_formulario.iloc[1][8]
nombrecompleto_contacto = df_formulario.iloc[1][9]
cargo_contacto = df_formulario.iloc[1][10]
celular_contacto = df_formulario.iloc[1][11]
apoyo_municipalidad = df_formulario.iloc[1][41]
insumos = df_formulario.iloc[1][34]
nombre_org_ayuda = df_formulario.iloc[1][35]
equipos = "---"
dias_semana = "---"
comidas_por_dia = df_formulario.iloc[1][36]
raciones_por_dia = df_formulario.iloc[1][37]
precio_racion = df_formulario.iloc[1][38]
raciones_no_pagadas = df_formulario.iloc[1][40]
zonas_beneficiadas = "---"
familias_beneficiadas = df_formulario.iloc[1][42]
niños_beneficiados = df_formulario.iloc[1][43]
adultos_mayores_beneficiados = df_formulario.iloc[1][44]
discapacidades_beneficiados = df_formulario.iloc[1][45]
blanco1 = "---"
cronicas_beneficiadas = df_formulario.iloc[1][46]
blanco2 = "---"
total_beneficiadas = None #no estoy segura como sale IGUAL AL NUMERO DE RACIONES.
blanco3 = df_formulario.iloc[1][68]
blanco4 = df_formulario.iloc[1][70]
blanco5 = df_formulario.iloc[1][71]
blanco6 = 2
padrones = df_formulario.iloc[1][12]
blanco7 = "---"
blanco8 = "---"
blanco9 = "---"
blanco10 = "---"
blanco11 = "---"
espacio = df_formulario.iloc[1][16]
estado_espacio = "---"
combustible = df_formulario.iloc[1][30]
techo = df_formulario.iloc[1][26]
lavado = df_formulario.iloc[1][29]
higiene = df_formulario.iloc[1][32]
interes_huerto = df_formulario.iloc[1][60]
implementacion_huerto = df_formulario.iloc[1][61]
liderazgo_huerto = df_formulario.iloc[1][62]
blanco12 = "---"
capacitaciones_protocolos_sanitarios = df_formulario.iloc[1][64]
blanco13 = "---"
migrante_atencion = df_formulario.iloc[1][47]
otro_cap = df_formulario.iloc[1][66]
ajustar_padron = df_formulario.iloc[1][13]
estado_olla = df_formulario.iloc[1][3]
razones_inactividad = df_formulario.iloc[1][14]
dias_atencion = df_formulario.iloc[1][15]
funcionamiento_ollas = df_formulario.iloc[1][16]
registro_ruos = df_formulario.iloc[1][17]
tipo_registro_ruos = df_formulario.iloc[1][18]
nivel_instruccion = df_formulario.iloc[1][19]
tipo_celular = df_formulario.iloc[1][20]
tipo_techo = df_formulario.iloc[1][26]
tipo_pared = df_formulario.iloc[1][27]
tipo_suelo = df_formulario.iloc[1][28]
botiquin = df_formulario.iloc[1][31]
implementos = df_formulario.iloc[1][33]
poblacion_migrante = df_formulario.iloc[1][47]
atencion_poblacion_mujeres = df_formulario.iloc[1][48]
atencion_poblacion_varones = df_formulario.iloc[1][49]
atencion_poblacion_ninos = df_formulario.iloc[1][50]
involucramiento_migrante = df_formulario.iloc[1][51]
numero_involucramiento_migrante = int(df_formulario.iloc[1][52])
numero_iniciativas = df_formulario.iloc[1][53]
numero_emprendimientos = df_formulario.iloc[1][54]
numero_idioma_diferente = df_formulario.iloc[1][55]
lenguas = df_formulario.iloc[1][56]
quechua = df_formulario.iloc[1][57]
shipibo = df_formulario.iloc[1][58]
aymara = df_formulario.iloc[1][59]
cual_cap = df_formulario.iloc[1][66]
tipo_aplicativos = df_formulario.iloc[1][22]
blanco14 = "---"
now = datetime.now()
current_time= now.strftime("%d/%m/%Y %H:%M:%S")
updated_at = current_time
# print(df_royer)
df_royer.loc[len(df_royer.index)] = [
      id1,
      correo,
      distrito, 
      zona, 
      AAHH, 
      ubicacion_exacta,
      agua, 
      fecha_creacion_olla,
      luz,
      nombre_olla,
      nombrecompleto_contacto,
      cargo_contacto,
      celular_contacto,
      apoyo_municipalidad,
      insumos,
      nombre_org_ayuda,
      equipos,
      dias_semana,
      comidas_por_dia,
      raciones_por_dia,
      precio_racion,
      raciones_no_pagadas,
      zonas_beneficiadas,
      familias_beneficiadas,
      niños_beneficiados,
      adultos_mayores_beneficiados,
      discapacidades_beneficiados,
      blanco1,
      cronicas_beneficiadas,
      blanco2,
      total_beneficiadas,
      blanco3,
      blanco4,
      blanco5,
      blanco6,
      padrones,
      blanco7,
      blanco8,
      blanco9,
      blanco10,
      blanco11,
      espacio,
      estado_espacio,
      combustible,
      techo,
      lavado,
      higiene,
      interes_huerto,
      implementacion_huerto,
      liderazgo_huerto,
      blanco12,
      capacitaciones_protocolos_sanitarios,
      blanco13,
      migrante_atencion,
      otro_cap,
      ajustar_padron,
      estado_olla,
      razones_inactividad,
      dias_atencion,
      funcionamiento_ollas,
      registro_ruos,
      tipo_registro_ruos,
      nivel_instruccion,
      tipo_celular,
      tipo_techo,
      tipo_pared,
      tipo_suelo,
      botiquin,
      implementos,
      poblacion_migrante,
      atencion_poblacion_mujeres,
      atencion_poblacion_varones,
      atencion_poblacion_ninos,
      involucramiento_migrante,
      numero_involucramiento_migrante,
      numero_iniciativas,
      numero_emprendimientos,
      numero_idioma_diferente,
      lenguas,
      quechua,
      shipibo,
      aymara,
      cual_cap,
      tipo_aplicativos,
      blanco14,
      updated_at,
      'NaN',
] 
# print(df_formulario)
# print(len(df_formulario.index))
writer = pd.ExcelWriter('converted-to-excel.xlsx')
df_royer.to_excel(writer)
writer.save()
# writer = pd.ExcelWriter('converted-to-excel.xlsx')
# df_formulario.to_excel(writer)
# writer.save()