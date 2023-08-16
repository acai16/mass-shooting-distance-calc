from flask import Flask, render_template, request
from utils import webscraper as ws


app = Flask(__name__)
            
@app.route('/', methods= ["POST", "GET"])
def home():

    if request.method == "POST":
        city = request.form.get('city')
        state = request.form.get('state')
        distance = ws.find_nearest(f'{city, state}')
    else:
        distance = "input something"
    

    
        
    return render_template('home.html', distance = distance)

            
if __name__ == "__main__":
    app.run(debug=True)