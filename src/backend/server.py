# Import flask and datetime module for showing date and time
from flask import Flask
from backendAPI import BackendAPI
from middlewareAPI import MiddlewareAPI

from Shared.State import State

# Initializing flask app
app = Flask(__name__)
 
# Route for seeing a data
@app.route('/data')
def get_time():
    api = MiddlewareAPI()
    franchiseState = api.get_franchise()[1]
    state = State(franchiseState)
    print(state.value)

    # Returning to show in reactjs
    return {
        'state':state.value
        }
     
# Running app
if __name__ == '__main__':
    app.run()