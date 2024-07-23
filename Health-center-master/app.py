# from flask import Flask, render_template

# app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/news')
# def news_detail():
#     return render_template('news.html')

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news-detail')
def news_detail():
    return render_template('news-detail.html')

if __name__ == '__main__':
    app.run(debug=True)
