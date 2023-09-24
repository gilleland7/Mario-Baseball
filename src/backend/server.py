# Import flask and datetime module for showing date and time
from flask import Flask
from backendAPI import BackendAPI
from middlewareAPI import MiddlewareAPI

from Shared.Character import Character

# Initializing flask app
app = Flask(__name__)
 
# Route for seeing a data
@app.route('/data')
def get_time():
    api = MiddlewareAPI()
    ch = Character()
    ch.name = "Luigi"
    ch.stats.defensiveStats.errors = 1

    ex = api.update_character_stats(ch)

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