from flask import Flask, render_template, request, redirect, url_for
from views import views 

app = Flask(__name__, template_folder="templates")
app.register_blueprint(views, url_prefix="/")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
