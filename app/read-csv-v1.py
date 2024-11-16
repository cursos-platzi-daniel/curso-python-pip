#En este ejemplo estamos leyendo cada unoa de las lineas del csv
#Vemos que cada linea o registro viene como una lista y 
#los elementos son los valores de cada columna
#Sin embargo, esto no es tan facil de utilizar.
#La forma más optima de almacenar los datos no es como una lista sino 
#como un diccionario. Asi que el reto será transformar estas listas en diccionarios.
#donde la llave de los diccionarios será el nombre o encabezado de las columnas.

"""
[
  {
    'Country':'Colombia',
    'Capital':'Bogota',
    '2022 Population':3000,
    'World Population Percent':0.12
  },
  {
    'Country':'Bolivia',
    'Capital':'Sucre',
    '2022 Population':500,
    'World Population Percent':0.12
  }
]  

ver read-csv.py

"""

import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
      print('***'*5)
      print(row)
      

if __name__ == '__main__':
  read_csv('./data.csv')
