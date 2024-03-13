from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        url = request.form.get('url')
        return render_template('index.html', url=url)

if __name__ == '__main__':
    app.run(debug=True, port=8000)