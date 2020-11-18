from flask import Flask

from weather import weather_by_city

app = Flask(__name__)


@app.route('/')
def index():
    weather = weather_by_city('Moscow, Russia')
    if weather:
        weather_string = f"Сейчас {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"
    else:
        weather_string = 'Сервис погоды не работает'
    return f"""<html>
        <head>
            <title>Прогноз погоды</title>
        </head>
        <body>
        <h1>{weather_string}</h1>
        </body>
    </html>"""


if __name__ == '__main__':
    app.run(debug=True)
