import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/V1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    
    