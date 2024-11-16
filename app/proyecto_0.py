import mimodulo
import utils

def run():
    keys, values = mimodulo.get_population()
    print(keys, values)

    data = [
    {
        'Country': 'Colombia',
        'Population': 500
    },
    {
        'Country': 'Bolivia',
        'Population': 300
    }
    ]
    keys, values = mimodulo.get_population()
    print(keys, values)

    country = input('Type Country => ')
    utils.population_by_country(data, country)

#Todo archivo .py es un modulo del cual podemos invocar y ejecutar sus funciones.
#El problema es que en ocasiones queremos invocar funciones del archivo principal,
#pero esto no quiere decir que queramos ejecutar todo el archivo principal.
#Para separar esto, entonces, se utiliza __name__ == '__main__' para especificar 
#que ese archivo contiene una funcion principal por ejemplo run().
#Y desde otros modulos podemos invocar otras funciones del archivo pricipal sin 
#que se ejecuta nuestra función principal run() a menos que la invoquemos 
#desde otro modulo, por ejemplo en example.py colocamos main.run()
if __name__ == '__main__':
  run()
