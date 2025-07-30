import time
import requests as requests
from flask import Flask, render_template

from sync_routes.routes import sync_bp
from async_routes.routes import async_bp

app = Flask(__name__)

app.register_blueprint(sync_bp, url_prefix="/sync")
app.register_blueprint(async_bp, url_prefix="/async")

app.config["NUMBER_OF_POKEMON"] = 20

@app.route('/') 
def index():
    start_time = time.perf_counter()
    end_time = time.perf_counter()

    return render_template('base.html'
                           , title="Pokemon"
                           , heading="Pokemon Flask"
                           , pokemon=[]
                           , end_time=end_time, start_time=start_time)

if __name__ == '__main__' :
    app.run(debug=True,port=50000)
