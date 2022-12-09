import pandas as pd
import os
import requests
# import urllib
from bs4 import BeautifulSoup as bs
from datetime import datetime

#0abrir data localmente
df_formulario = pd.read_excel (
      os.path.join("C:/Users/avill/Downloads","UP Ollas Comunes - Municipalidad de Lima (Respuestas).xlsx"),
      engine='openpyxl',
 )
#print(df_formulario)

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

#eliminar celulares duplicados (elimina los primeros duplicados, se mantiene con el ultimo celular duplicado que se agregó en el excel del formulario)
df_formulario.drop_duplicates(keep='last', subset=[11], inplace=True)

#identificador celular, buscar valores diferentes y crear df que solo tenga estos valores
#columna en formulario: 11, royer: 13
df_formulario = df_formulario.dropna(subset=[11]) 

for y in df_formulario[11]:
      if y in set(df_royer[13]):
            df_formulario.drop(df_formulario.loc[df_formulario[11]==y].index, inplace=True) 

#guardar en un dataframe distinto las ollas desactivadas (columna 35 = 3):
df_royer_desactivadas = df_royer[df_royer['Unnamed: 34'] == 3]

#transcribir los valores nuevos al excel de royer
#crear lista con valores en el orden deseado y ordenar los valores necesarios:
#antes de realizar esta lista, se debe diferenciar si es una olla activada o desactivada, para ver si solo se agrega el celular y el 3. 
#hallar id:
df_royer = df_royer.dropna(subset=[1]) 
for x in range(1,len(df_formulario.axes[0])):
      id1 = int(df_royer.iloc[len(df_royer.index) - 1][1]) + 1
      correo = "---"
      distrito = int(df_formulario.iloc[x][4].split('-')[0])
      zona = df_formulario.iloc[x][5]
      AAHH = df_formulario.iloc[x][6]
      ubicacion_exacta = df_formulario.iloc[x][7]
      agua = df_formulario.iloc[x][24]
      fecha_creacion_olla = "---"
      luz = df_formulario.iloc[x][25]
      nombre_olla = df_formulario.iloc[x][8]
      nombrecompleto_contacto = df_formulario.iloc[x][9]
      cargo_contacto = df_formulario.iloc[x][10]
      celular_contacto = df_formulario.iloc[x][11]
      apoyo_municipalidad = df_formulario.iloc[x][41]
      insumos = df_formulario.iloc[x][34]
      nombre_org_ayuda = df_formulario.iloc[x][35]
      equipos = "---"
      dias_semana = "---"
      comidas_por_dia = df_formulario.iloc[x][36]
      raciones_por_dia = df_formulario.iloc[x][37]
      precio_racion = df_formulario.iloc[x][38]
      raciones_no_pagadas = df_formulario.iloc[x][40]
      zonas_beneficiadas = "---"
      familias_beneficiadas = df_formulario.iloc[x][42]
      niños_beneficiados = df_formulario.iloc[x][43]
      adultos_mayores_beneficiados = df_formulario.iloc[x][44]
      discapacidades_beneficiados = df_formulario.iloc[x][45]
      blanco1 = "---"
      cronicas_beneficiadas = df_formulario.iloc[x][46]
      blanco2 = "---"
      total_beneficiadas = df_formulario.iloc[x][37] 
      blanco3 = df_formulario.iloc[x][68]
      blanco4 = df_formulario.iloc[x][70]
      blanco5 = df_formulario.iloc[x][71]
      blanco6 = 2
      padrones = df_formulario.iloc[x][12]
      blanco7 = "---"
      blanco8 = "---"
      blanco9 = "---"
      blanco10 = "---"
      blanco11 = "---"
      espacio = df_formulario.iloc[x][16]
      estado_espacio = "---"
      combustible = df_formulario.iloc[x][30]
      techo = df_formulario.iloc[x][26]
      lavado = df_formulario.iloc[x][29]
      higiene = df_formulario.iloc[x][32]
      interes_huerto = df_formulario.iloc[x][60]
      implementacion_huerto = df_formulario.iloc[x][61]
      liderazgo_huerto = df_formulario.iloc[x][62]
      blanco12 = "---"
      capacitaciones_protocolos_sanitarios = df_formulario.iloc[x][64]
      blanco13 = "---"
      migrante_atencion = df_formulario.iloc[x][47]
      otro_cap = df_formulario.iloc[x][66]
      ajustar_padron = df_formulario.iloc[x][13]
      estado_olla = df_formulario.iloc[x][3]
      razones_inactividad = df_formulario.iloc[x][14]
      dias_atencion = df_formulario.iloc[x][15]
      funcionamiento_ollas = df_formulario.iloc[x][16]
      registro_ruos = df_formulario.iloc[x][17]
      tipo_registro_ruos = df_formulario.iloc[x][18]
      nivel_instruccion = df_formulario.iloc[x][19]
      tipo_celular = df_formulario.iloc[x][20]
      tipo_techo = df_formulario.iloc[x][26]
      tipo_pared = df_formulario.iloc[x][27]
      tipo_suelo = df_formulario.iloc[x][28]
      botiquin = df_formulario.iloc[x][31]
      implementos = df_formulario.iloc[x][33]
      poblacion_migrante = df_formulario.iloc[x][47]
      atencion_poblacion_mujeres = df_formulario.iloc[x][48]
      atencion_poblacion_varones = df_formulario.iloc[x][49]
      atencion_poblacion_ninos = df_formulario.iloc[x][50]
      involucramiento_migrante = df_formulario.iloc[x][51]
      numero_involucramiento_migrante = int(df_formulario.iloc[x][52])
      numero_iniciativas = df_formulario.iloc[x][53]
      numero_emprendimientos = df_formulario.iloc[x][54]
      numero_idioma_diferente = df_formulario.iloc[x][55]
      lenguas = df_formulario.iloc[x][56]
      quechua = df_formulario.iloc[x][57]
      shipibo = df_formulario.iloc[x][58]
      aymara = df_formulario.iloc[x][59]
      cual_cap = df_formulario.iloc[x][66]
      tipo_aplicativos = df_formulario.iloc[x][22]
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
            'NaN', #cambiar a 2 o 3,  depende de la base madre
      ] 
      
#Agregar las ollas desactivadas:
df_royer = df_royer.append(df_royer_desactivadas,ignore_index=True)
# print(df_formulario)
# print(len(df_formulario.index))
writer = pd.ExcelWriter('converted-to-excel-royer.xlsx')
df_royer.to_excel(writer)
writer.save()
writer = pd.ExcelWriter('converted-to-excel-formulario.xlsx')
df_formulario.to_excel(writer)
writer.save()