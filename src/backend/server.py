# Import flask and datetime module for showing date and time
from flask import Flask
from backendAPI import BackendAPI
from middlewareAPI import MiddlewareAPI

# Initializing flask app
app = Flask(__name__)
 
# Route for seeing a data
@app.route('/data')
def get_time():
    api = MiddlewareAPI()
    ex = api.get_next_game()

    # Returning to show in reactjs
    return {
        'Name':"geek",
        "Age":"22",
        "ex": str(ex),
        "programming":"python"
        }
     
# Running app
if __name__ == '__main__':
    app.run()