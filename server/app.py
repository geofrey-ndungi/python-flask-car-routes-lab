from flask import Flask

app = Flask(__name__)


# root route(home)
@app.route('/')
#the view function
def home():
    return "Welcome to Flatiron Cars"



#the variable route
@app.route('/<model>')

#the view function
def model(model):
    existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']
    if model in existing_models:
        return f"Flatiron {model} is in our fleet"
    else:
        return f"No models called {model} exists in our catalog"




if __name__ == "__main__": #means only run it as a script not a module...
    app.run(port = 5555, debug =  True)

