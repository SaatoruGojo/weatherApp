from flask import Flask, render_template,request
import requests

#url = "https://api.openweathermap.org/data/2.5/weather"
#apikey = "0f0432f6b23fa71d90a64e6bdb432a32"


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/get_weather',methods=['GET', 'POST'])
def getWeather():
    url = "https://api.openweathermap.org/data/2.5/weather"
    param = {
        'q' : request.form.get("city"),
        'appid' : request.form.get("appid"),
        'units' : request.form.get("unit")
    }
    response = requests.get(url,params=param)
    data = response.json()
    return f"data : {data}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
