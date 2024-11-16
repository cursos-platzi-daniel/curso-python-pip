import csv

def read_csv(path):
   total = 0
   with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      for row in reader:
         total = int(row[1]) + total   
   return total

response = read_csv('./data_empresa.csv')
print(response)