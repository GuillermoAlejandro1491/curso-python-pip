import charts
import read_csv
import utils


def run():
  data = read_csv.read_csv('./data.csv')
  data = list(filter(lambda item : item['Continent'] == 'Asia', data))
  
  countries = list(map(lambda x:x['Country'], data))
  percentage = list(map(lambda x:x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentage)
  
 
  country = input('Type country ==> ')
  print(country)
  
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)
    
    
 
if __name__ == '__main__':
  run()