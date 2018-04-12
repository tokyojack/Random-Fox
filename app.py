import requests
from flask import render_template, Flask

app = Flask(__name__)


def get_random_fox():
    return requests.get(
            "https://randomfox.ca/floof/",
            ).json()['image']


@app.route('/')
def index_template():
    return render_template('index.html', image_url=get_random_fox())


if __name__ == '__main__':
    app.run()
