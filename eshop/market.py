from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/products')
def products_page():
    return render_template('products.html', item_name = 'Phone')

if __name__ == '__main__':
    app.run(debug=True)