from flask import Flask, render_template
import dao

app = Flask(__name__)

@app.route('/')
def index():
    cate = dao.load_categories()
    prod = dao.load_products()

    return render_template('index.html', msg = 'BM142', categories = cate, products = prod)

if __name__ == '__main__':
    app.run(debug=True)