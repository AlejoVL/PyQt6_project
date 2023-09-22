from modules.conexion import ConexionDB

################################################PROVEEDOR########################################################

def insProv(nombre, contacto, direccion):
    con = ConexionDB()
    try:
        sql = "INSERT INTO Proveedores (nombre, contacto, direccion) VALUES (?, ?, ?)"
        data = (nombre, contacto, direccion)
        con.cursor.execute(sql, data)
        print("Proveedor insertado correctamente.")
    except Exception as e:
        print(f"Error al insertar proveedor: {e}")
        return e
    con.closeConexion()


def readProv():
    con = ConexionDB()
    try:
        sql = "SELECT * FROM Proveedores"
        res = con.cursor.execute(sql).fetchall()
        print("Lectura exitosa")
        con.closeConexion()
        return res
    except Exception as e:
        print(f"Error al obtener proveedores: {e}")
        con.closeConexion()
        return e


def updProv(id, nombre, contacto, direccion):
    con = ConexionDB()
    try:
        sql = "UPDATE Proveedores SET nombre=?, contacto=?, direccion=? WHERE id=?"
        data = (nombre, contacto, direccion, id)
        con.cursor.execute(sql, data)
        print("Proveedor actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar proveedor: {e}")
        return e
    con.closeConexion()


def delProv(id):
    con = ConexionDB()
    try:
        sql = "DELETE FROM Proveedores WHERE id=?"
        data = (id,)
        con.cursor.execute(sql, data)
        con.closeConexion()
        print("Proveedor eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar proveedor: {e}")
        con.closeConexion()
        return e

################################################PRODUCTOS########################################################

def insProd(nombre, cantidad_en_stock, precio, categoria, proveedor_id, precio_distintivo):
    con = ConexionDB()
    try:
        sql = "INSERT INTO Productos (nombre, cantidad_en_stock, precio, categoria, proveedor_id, precio_distintivo) VALUES (?, ?, ?, ?, ?, ?)"
        data = (nombre, cantidad_en_stock, precio, categoria, proveedor_id, precio_distintivo)
        con.cursor.execute(sql, data)
        print("Producto insertado correctamente.")
    except Exception as e:
        print(f"Error al insertar producto: {e}")
        return e
    con.closeConexion()


def readProd():
    con = ConexionDB()
    try:
        sql = "SELECT * FROM Productos"
        res = con.cursor.execute(sql).fetchall()
        print("Lectura de productos exitosa")
        con.closeConexion()
    except Exception as e:
        print(f"Error al obtener productos: {e}")
        con.closeConexion()
    return res

def readProd2(id):
    con = ConexionDB()
    try:
        sql = f"SELECT * FROM Productos WHERE id ={id}"
        res = con.cursor.execute(sql).fetchall()[0]
        con.closeConexion()
        print("Lectura de productos exitosa")
        return res
    except Exception as e:
        con.closeConexion()
        print(f"Error al obtener productos: {e}")
        return 0

def updProd(id, nombre, cantidad_en_stock, precio, categoria, proveedor_id, precio_distintivo):
    con = ConexionDB()
    try:
        sql = "UPDATE Productos SET nombre=?, cantidad_en_stock=?, precio=?, categoria=?, proveedor_id=?, precio_distintivo=? WHERE id=?"
        data = (nombre, cantidad_en_stock, precio, categoria, proveedor_id, precio_distintivo, id)
        con.cursor.execute(sql, data)
        print("Producto actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar producto: {e}")
        return e
    con.closeConexion()

def updProd2(id, cant):
    con = ConexionDB()
    try:
        sql = "UPDATE Productos SET cantidad_en_stock=? WHERE id=?"
        data = (cant, id)
        con.cursor.execute(sql, data)
        print("Producto actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar producto: {e}")
        return e
    con.closeConexion()


def delProd(id):
    con = ConexionDB()
    try:
        sql = "DELETE FROM Productos WHERE id=?"
        data = (id,)
        con.cursor.execute(sql, data)
        print("Producto eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar producto: {e}")
        return e
    con.closeConexion()

################################################CLIENTES########################################################

def insCli(nombre, direccion, email, telefono):
    con = ConexionDB()
    try:
        sql = "INSERT INTO Clientes (nombre, direccion, email, telefono) VALUES (?, ?, ?, ?)"
        data = (nombre, direccion, email, telefono)
        con.cursor.execute(sql, data)
        print("Cliente insertado correctamente.")
    except Exception as e:
        print(f"Error al insertar cliente: {e}")
        return e
    con.closeConexion()


def readCli():
    con = ConexionDB()
    try:
        sql = "SELECT * FROM Clientes"
        res = con.cursor.execute(sql).fetchall()
        print("Lectura de clientes exitosa")
        con.closeConexion()
    except Exception as e:
        print(f"Error al obtener clientes: {e}")
        con.closeConexion()
    return res


def updCli(id, nombre, direccion, email, telefono):
    con = ConexionDB()
    try:
        sql = "UPDATE Clientes SET nombre=?, direccion=?, email=?, telefono=? WHERE id=?"
        data = (nombre, direccion, email, telefono, id)
        con.cursor.execute(sql, data)
        print("Cliente actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar cliente: {e}")
        return e
    con.closeConexion()


def delCli(id):
    con = ConexionDB()
    try:
        sql = "DELETE FROM Clientes WHERE id=?"
        data = (id,)
        con.cursor.execute(sql, data)
        print("Cliente eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar cliente: {e}")
        return e
    con.closeConexion()

################################################DESPACHOS########################################################

def insDesp(cliente_id, producto_id, cantidad_despachada, fecha):
    con = ConexionDB()
    try:
        sql = "INSERT INTO Despachos (cliente_id, producto_id, cantidad_despachada, fecha) VALUES (?, ?, ?, ?)"
        data = (cliente_id, producto_id, cantidad_despachada, fecha)
        con.cursor.execute(sql, data)
        print("Despacho insertado correctamente.")
    except Exception as e:
        print(f"Error al insertar despacho: {e}")
        return e
    con.closeConexion()


def readDesp():
    con = ConexionDB()
    try:
        sql = "SELECT * FROM Despachos"
        res = con.cursor.execute(sql).fetchall()
        print("Lectura de despachos exitosa")
        con.closeConexion()
    except Exception as e:
        print(f"Error al obtener despachos: {e}")
        con.closeConexion()
    return res

def readDesp2(id):
    con = ConexionDB()
    try:
        sql = f"SELECT * FROM Despachos WHERE id ={id}"
        res = con.cursor.execute(sql).fetchall()[0]
        con.closeConexion()
        byu=res[2]
        byu2=res[3]
        print(byu, " ", byu2, " " , res, "buy res")
        if type(byu) == int and type(byu2) == int:
            print("Lectura de productos exitosa")
            return res
        else:
            return 0
    except Exception as e:
        con.closeConexion()
        print(f"Error al obtener productos: {e}")
        return 0


def updDesp(id, cliente_id, producto_id, cantidad_despachada, fecha):
    con = ConexionDB()
    try:
        sql = "UPDATE Despachos SET cliente_id=?, producto_id=?, cantidad_despachada=?, fecha=? WHERE id=?"
        data = (cliente_id, producto_id, cantidad_despachada, fecha, id)
        con.cursor.execute(sql, data)
        print("Despacho actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar despacho: {e}")
        return e
    con.closeConexion()


def delDesp(id):
    con = ConexionDB()
    try:
        sql = "DELETE FROM Despachos WHERE id=?"
        data = (id,)
        con.cursor.execute(sql, data)
        print("Despacho eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar despacho: {e}")
        return e
    con.closeConexion()

################################################RESERVAS########################################################

def insRev(cliente_id, producto_id, cantidad_reservada, estado):
    con = ConexionDB()
    try:
        sql = "INSERT INTO Reservas (cliente_id, producto_id, cantidad_reservada, estado) VALUES (?, ?, ?, ?)"
        data = (cliente_id, producto_id, cantidad_reservada, estado)
        con.cursor.execute(sql, data)
        print("Reserva insertada correctamente.")
    except Exception as e:
        print(f"Error al insertar reserva: {e}")
        return e
    con.closeConexion()


def readRev():
    con = ConexionDB()
    try:
        sql = "SELECT * FROM Reservas"
        res = con.cursor.execute(sql).fetchall()
        print("Lectura de reservas exitosa")
        con.closeConexion()
    except Exception as e:
        print(f"Error al obtener reservas: {e}")
        con.closeConexion()
    return res

def readRev2(pd):
    con = ConexionDB()
    try:
        sql = f"SELECT * FROM Reservas WHERE producto_id ={pd}"
        res = con.cursor.execute(sql).fetchall()[0]
        con.closeConexion()
        byu=res[3]
        print(byu, " " , res, "buy res")
        if type(byu) == int:
            print("Lectura de productos exitosa")
            return res
        else:
            return 0
    except Exception as e:
        con.closeConexion()
        print(f"Error al obtener productos: {e}")
        return 0



def updRev(id, cliente_id, producto_id, cantidad_reservada, estado):
    con = ConexionDB()
    try:
        sql = "UPDATE Reservas SET cliente_id=?, producto_id=?, cantidad_reservada=?, estado=? WHERE id=?"
        data = (cliente_id, producto_id, cantidad_reservada, estado, id)
        con.cursor.execute(sql, data)
        print("Reserva actualizada correctamente.")
    except Exception as e:
        print(f"Error al actualizar reserva: {e}")
        return e
    con.closeConexion()


def delRev(id):
    con = ConexionDB()
    try:
        sql = "DELETE FROM Reservas WHERE id=?"
        data = (id,)
        con.cursor.execute(sql, data)
        print("Reserva eliminada correctamente.")
    except Exception as e:
        print(f"Error al eliminar reserva: {e}")
        return e
    con.closeConexion()
