
from flask import Flask, render_template, request, redirect, url_for, flash
from tienda import TiendaRopa

app = Flask(__name__)
app.secret_key = 'your_secret_key'

tienda = TiendaRopa()

@app.route('/')
def index():
    return render_template('index.html', productos=tienda.productos)

@app.route('/agregar_producto', methods=['POST'])
def agregar_producto():
    nombre = request.form['nombre']
    colores = request.form.getlist('color[]')
    tamanhos = request.form.getlist('size[]')
    precio = request.form['precio']
    categoria = request.form['categoria']
    quantidades = request.form.getlist('quantity[]')
    stock = {}
    for i, color in enumerate(colores):
        if color not in stock:
            stock[color] = {}
        stock[color][tamanhos[i]] = int(quantidades[i])

    tienda.agregar_producto(nombre, precio, categoria, stock)  # Removido o 'id' da chamada
    flash(f"Producto '{nombre}' agregado al catálogo.")
    return redirect(url_for('index'))

@app.route('/editar_producto/<int:producto_id>', methods=['POST'])
def editar_producto(producto_id):
    nombre = request.form['nombre']
    colores = request.form.getlist('color[]')
    tamanhos = request.form.getlist('size[]')
    precio = request.form['precio']
    categoria = request.form['categoria']
    quantidades = request.form.getlist('quantity[]')
    stock = {}
    for i, color in enumerate(colores):
        if color not in stock:
            stock[color] = {}
        stock[color][tamanhos[i]] = int(quantidades[i])

    # Encontrar e atualizar o produto
    for producto in tienda.productos:
        if producto['producto_id'] == producto_id:
            producto['nombre'] = nombre
            producto['precio'] = precio
            producto['categoria'] = categoria
            producto['stock'] = stock
            break

    flash(f"Producto '{nombre}' atualizado com sucesso.")
    return redirect(url_for('index'))



@app.route('/realizar_venta', methods=['POST'])
def realizar_venta():
    nombre = request.form['nombre']
    cantidad = int(request.form['cantidad'])
    if tienda.realizar_venta(nombre, cantidad):
        flash(f"Venta realizada: {cantidad} x {nombre}")
    else:
        flash(f"No hay suficiente stock de {nombre} para realizar la venta.")
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
