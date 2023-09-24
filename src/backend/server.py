# Import flask and datetime module for showing date and time
from flask import Flask
from backendAPI import BackendAPI
from middlewareAPI import MiddlewareAPI

from Shared.Game import Game
from Shared.Team import Team

# Initializing flask app
app = Flask(__name__)
 
# Route for seeing a data
@app.route('/data')
def get_time():
    api = MiddlewareAPI()
    g = Game()

    t1 = Team()
    t2 = Team()
    t1.name = "Luigi Knights"
    t2.name = "Wario Monstars"
    
    g.setup(1, "Wario City", t2, t1, 5, 10)

    ex = api.set_game_results(g)

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