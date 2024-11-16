import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader) #Iteramos solo la primera linea para obtener encabezados
    #print(header)
    
    data = []
    for row in reader:
      iterable = zip(header, row) #nos permite unir dos listas en una sola, como una cremallera
      #print(list(iterable))
      country_dict = {key: value for key, value in iterable} # Creamos diccionario a partir de la lista de tuplas key, value
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./data.csv')
  print(data[0])