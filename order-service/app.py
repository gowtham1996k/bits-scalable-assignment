from flask import Flask, render_template

app = Flask(__name__)

@app.route('/orders')
def index():
    return render_template('index.html', service_name='Order service')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
