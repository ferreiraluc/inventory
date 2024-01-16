class TiendaRopa:
    def __init__(self):
        self.productos = []
        self.producto_id_counter = 0  # Renomeie para algo mais claro

    def agregar_producto(self, nombre, precio, categoria, stock_por_color_y_tamano):
        self.producto_id_counter += 1  # Incrementar ID
        producto = {
            'producto_id': self.producto_id_counter,  # Alterado de 'id' para 'producto_id'
            'nombre': nombre,
            'precio': precio,
            'categoria': categoria,
            'stock': stock_por_color_y_tamano,
        }
        self.productos.append(producto)


    def realizar_venta(self, nombre, cantidad, color, tamano):
        for producto in self.productos:
            if producto['nombre'] == nombre:
                if producto['stock'].get(color, {}).get(tamano, 0) >= cantidad:
                    producto['stock'][color][tamano] -= cantidad
                    return True  # Venta realizada con éxito
                else:
                    return False  # No hay suficiente stock
        return False  # Producto no encontrado
