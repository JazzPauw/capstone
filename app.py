from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/streamlit')
def streamlit_app():
    return render_template('streamlit_app.html')

if __name__ == '__main__':
    app.run(debug=True)

