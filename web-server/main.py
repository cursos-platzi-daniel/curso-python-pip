import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return[1,2,3,]

@app.get('/contacts')
def get_list():
    return {'name':'Platzi'}


@app.get('/html', response_class = HTMLResponse)
def get_list():
    return """
        <h1> Hola soy un codigo HTML </h1>
    """

def run():
    store.get_categories()
    
if __name__=='__main__':
    run()