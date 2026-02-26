from config import get_connection
from dto.producto_dto import ProductoDTO

class ProductoDAO:

    @staticmethod
    def listar():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM producto")
        filas = cursor.fetchall()
        conn.close()

        productos = []
        for f in filas:
            productos.append(ProductoDTO(*f))
        return productos

    @staticmethod
    def guardar(producto):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO producto (nombre, descripcion, precio, stock) VALUES (?, ?, ?, ?)",
            (producto.nombre, producto.descripcion, producto.precio, producto.stock)
        )
        conn.commit()
        conn.close()
    
    @staticmethod
    def obtener_por_id(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM producto WHERE id = ?", (id,))
        fila = cursor.fetchone()
        conn.close()

        if fila:
            return ProductoDTO(*fila)
        return None

    @staticmethod
    def actualizar(producto):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE producto
            SET nombre = ?, descripcion = ?, precio = ?, stock = ?
            WHERE id = ?
        """, (producto.nombre, producto.descripcion, producto.precio, producto.stock, producto.id))
        conn.commit()
        conn.close()

    @staticmethod
    def eliminar(id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM producto WHERE id = ?", (id,))
        conn.commit()
        conn.close()