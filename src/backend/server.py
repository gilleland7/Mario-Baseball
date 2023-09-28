# Import flask and datetime module for showing date and time
from flask import Flask
from backendAPI import BackendAPI
from middlewareAPI import MiddlewareAPI

from Shared.Game import Game
from Shared.Team import Team
from Shared.Division import Division
from Shared.Character import Character

# Initializing flask app
app = Flask(__name__)
 
# Route for seeing a data
@app.route('/data')
def get_time():
    api = MiddlewareAPI()
    g = Game()

    div = Division()
    div.name = "Mushroom"

    ch = Character()
    ch.name = "Luigi"

    t1 = Team()
    t2 = Team()
    t1.name = "Luigi Knights"
    t2.name = "Wario Muscles"

    g.setup(1, "Wario City", t2, t1, 5, 10)

    awards_dict = {ch:"Silver Slugger"}

    ex = api.get_all_character_names()

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