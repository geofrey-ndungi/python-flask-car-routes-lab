# Lab: Car Routes Lab


### App Routes:

- `/`  
  - Returns: `"Welcome to Flatiron Cars"`

- `/<model>`  
  - Takes `model` variable from the URL  
  - Uses the `model` variable to check against an `existing_models` array  
    - If model exists:  
      `"Flatiron {model} is in our fleet!"`  
    - If model doesn't exist:  
      `"No models called {model} exists in our catalog"`
