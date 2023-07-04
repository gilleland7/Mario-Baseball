# Import flask and datetime module for showing date and time
from flask import Flask
from api import API

# Initializing flask app
app = Flask(__name__)
 
# Route for seeing a data
@app.route('/data')
def get_time():
    api = API()
    character_names = api.get_all_character_names()

    # Returning to show in reactjs
    return {
        'Name':"geek",
        "Age":"22",
        "Date": str(character_names[0][0]),
        "programming":"python"
        }
 
     
# Running app
if __name__ == '__main__':
    app.run()