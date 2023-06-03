from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application
app = Flask(__name__)

# Create home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ai')
def ai():
    return render_template('ai.html')

@app.route('/data-engineering')
def data_engineering():
    return render_template('data_engineering.html')

@app.route('/cloud')
def cloud():
    return render_template('cloud.html')

@app.route('/python')
def python():
    return render_template('python.html')


# Define a route for processing form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return render_template('result.html', name=name)


# Run the application if executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
