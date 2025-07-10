
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/shop.html')
def shop():
    return render_template('shop.html')

@app.route('/cart.html')
def cart():
    return render_template('cart.html')

@app.route('/checkout.html')
def checkout():
    return render_template('checkout.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/detail.html')
def detail():
    return render_template('detail.html')

if __name__ == '__main__':
    app.run(debug=True)
