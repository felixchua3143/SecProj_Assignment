from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/detail')
def detail():
    return render_template('detail.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')


if __name__ == '__main__':
    app.run(debug=True)
