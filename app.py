from flask import Flask, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = 'your-very-secret-key-here'

UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    """Return True if filename has an allowed image extension."""
    return (
        '.' in filename
        and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    )

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

@app.route('/upload', methods=['GET', 'POST'])
def upload_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        files = request.files.getlist('images')

        # Basic validation
        if not name or not description or not price:
            flash('All text fields are required.', 'warning')
            return redirect(request.url)

        # Save each image
        saved_filenames = []
        for f in files:
            if f and allowed_file(f.filename):
                filename = secure_filename(f.filename)
                dest = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                f.save(dest)
                saved_filenames.append(filename)

        # TODO: save `name`, `description`, `price`, and `saved_filenames`
        #       to your database here.

        flash('Product uploaded successfully!', 'success')
        return redirect(url_for('shop'))

    # GET request
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
