import utils
import read_csv
import charts
import pandas as pd

# Este codigo muestra lo realizado en main.py pero esta vez apoyados en la librería pandas.
# Nota: Es recomendable conocer como se puede realizar el proceso en una capa inferior tal como lo hicimos en main.py 
# antes de avanzar con esta librería pandas
 
def run():
  df = pd.read_csv('data.csv')
  df = df[df['Continent']=='Africa']
  countries = df['Country'].values
  percentages = df['World Population Percentage'].values
  
  charts.generate_pie_chart(countries, percentages)
 
  country = input('Type Country => ')
  data = read_csv.read_csv('./data.csv')
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country_dict = result[0]
    labels, values = utils.get_population(country_dict)
    charts.generate_bar_chart(country,labels, values)
  

if __name__ == '__main__':
  run()