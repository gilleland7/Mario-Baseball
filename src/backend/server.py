# Import flask and datetime module for showing date and time
from flask import Flask
from middlewareAPI import MiddlewareAPI

from Shared.State import State
from Shared.Team import Team

# Initializing flask app
app = Flask(__name__)
 
# Route for seeing state data
@app.route('/state')
def get_state():
    api = MiddlewareAPI()
    franchiseState = api.get_franchise()[1]
    state = State(franchiseState)
   
    userTeam = api.get_user_team()
    team = Team()
    team.setup(userTeam, api)

    # Returning to show in reactjs
    return {
        'state':state.value,
        }

# Route for seeing userteam data
@app.route('/userteam')
def get_team():
    api = MiddlewareAPI()
   
    userTeam = api.get_user_team()
    team = Team()
    team.setup(userTeam, api)

    # Returning to show in reactjs
    return {
        'teamLogo':team.logo,
        'teamName':team.name
    }

#Route for seeing teams data
@app.route('/teams')
def get_teams():
    api = MiddlewareAPI()
   
    teams = api.get_all_teams()   
    teamList = []

    for teamData in teams:
        team = Team()
        team.setup(teamData, api)
        teamList.append(team.name)

    # Returning to show in reactjs
    return {
        'teams':teamList
    }
     
# Running app
if __name__ == '__main__':
    app.run()