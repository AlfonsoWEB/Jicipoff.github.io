from flask import Flask, render_template

app = Flask(__name__)

# Datos de ejemplo de artículos
items = [
    {'id': 1, 'name': 'Tenis', 'price': 0, 'info': 'tenis diseñados por JICIP ', 'image': 'jicip.png'},
    {'id': 2, 'name': 'Sudaderas', 'price': 0, 'info': 'Sudaderas diseñadas por JICIP', 'image': 'item2.jpg'},
    {'id': 3, 'name': 'Playeras', 'price': 0, 'info': 'Playeras diseñadas por JICIP', 'image': 'item3.jpg'},
]

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/item/<int:item_id>')
def item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return render_template('item.html', item=item)
    else:
        return "Artículo no encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)
