from flask import Flask, render_template,request
import requests

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
    return render_template("weather_result.html", data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
