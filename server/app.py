from flask import Flask

app = Flask(__name__)


# root route(home)
@app.route('/')
#the view function
def home():
    return "<h1>Welcome to Flatiron Cars</h1>"



#the variable route
@app.route('/<model>')

#the view function
def model(model):
    existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']
    if model in existing_models:
        return f"<h1>Flatiron {model} is in our fleet</h1>"
    else:
        return f"<h1>No models called {model} exists in our catalog</h1>"




if __name__ == "__main__": #means only run it as a script not a module...
    app.run(port = 5555, debug =  True)

