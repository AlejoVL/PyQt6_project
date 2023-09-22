from modules.conexion import ConexionDB


################################################PRODUCTOS########################################################

def mostrarProductos():
    con = ConexionDB()
    sql = """SELECT * FROM  Productos"""
    try:
        listo = con.cursor.execute(sql).fetchall()
        con.closeConexion()
    except:
        ti = 'Error de conexión'
        tex = 'La tabla Vuelos no es accesible en este momento en la base de datos'
        print('error al mostrar productos')
    return listo

def actProd(nombre, cantidad_en_stock, precio, categoria, proveedor_id, precio_distintivo,idP):
    con = ConexionDB()
    try:
        sql = "UPDATE Productos SET nombre=?, cantidad_en_stock=?, precio=?, categoria=?, proveedor_id=?, precio_distintivo=? WHERE id=?"
        data = (nombre, cantidad_en_stock, precio, categoria, proveedor_id, precio_distintivo, idP)
        con.cursor.execute(sql, data)
        print("Producto actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar producto: {e}")
        return e
    con.closeConexion()
    
def eliminar_producto(id_producto):
    con = ConexionDB()
    try:
        sql = "DELETE FROM Productos WHERE id=?"
        data = (id_producto,)
        con.cursor.execute(sql, data)
        print("Producto eliminado correctamente.")
    except Exception as e:
        print(f"Error al eliminar producto: {e}")
    finally:
        con.closeConexion()

def crearProducto(datos_producto):
    con = ConexionDB()
    try:
        con.cursor.execute("INSERT INTO productos (nombre, cantidad_en_stock, precio, categoria, proveedor_id, precio_distintivo) VALUES (?, ?, ?,?,?,?)", (datos_producto))
        con.conexion.commit()
        con.closeConexion()
        return True
    except:
        con.conexion.rollback()
        ti = 'Error al crear el Usuario'
        tex = 'No se pudo crear el producto en este momento en la base de datos'
        print('error al crear producto')
        return False
    

################################################despachos########################################################    
def mostrarDespachos():
    con = ConexionDB()
    sql = """SELECT * FROM  Despachos"""
    listo = []
    try:
        listo = con.cursor.execute(sql).fetchall()
        con.closeConexion()
    except:
        ti = 'Error de conexión'
        tex = 'La tabla Vuelos no es accesible en este momento en la base de datos'
        print('error al mostrar productos')
    return listo

def crearProveedor(datos_proveedor):
    con = ConexionDB()
    try:
        con.cursor.execute("INSERT INTO proveedores (nombre, contacto, direccion) VALUES (?, ?, ?)", (datos_proveedor))
        con.conexion.commit()
        con.closeConexion()
        return True
    except:
        con.conexion.rollback()
        ti = 'Error al crear el Proveedor'
        tex = 'No se pudo crear el proveedor en este momento en la base de datos'
        print('error al crear proveedor')
        return False

def actualizarD(idp, cliente_id, producto_id, cantidad_despachada, fecha):
    con = ConexionDB()
    try:
        sql = "UPDATE Despachos SET cliente_id=?, producto_id=?, cantidad_despachada=?, fecha=? WHERE id=?"
        data = (cliente_id, producto_id, cantidad_despachada, fecha, idp)
        con.cursor.execute(sql, data)
        print("Despacho actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar despacho: {e}")
        return e
    con.closeConexion()
 
 
################################################PROVEEEDORES########################################################     
def mostrarProveedores():
    con = ConexionDB()
    sql = """SELECT * FROM  Proveedores"""
    listo = []
    try:
        listo = con.cursor.execute(sql).fetchall()
        con.closeConexion()
    except:
        ti = 'Error de conexión'
        tex = 'La tabla Vuelos no es accesible en este momento en la base de datos'
        print('error al mostrar productos')
    return listo

def crearProveedor(datos_producto):
    con = ConexionDB()
    try:
        con.cursor.execute("INSERT INTO Proveedor (nombre, cantidad_en_stock, precio, categoria, proveedor_id, precio_distintivo) VALUES (?, ?, ?,?,?,?)", (datos_producto))
        con.conexion.commit()
        con.closeConexion()
        return True
    except:
        con.conexion.rollback()
        ti = 'Error al crear el Usuario'
        tex = 'No se pudo crear el producto en este momento en la base de datos'
        print('error al crear producto')
        return False

################################################CLIENTES########################################################  
def mostrarClientes():
    con = ConexionDB()
    sql = """SELECT * FROM  Clientes"""
    listo = []
    try:
        listo = con.cursor.execute(sql).fetchall()
        con.closeConexion()
    except:
        ti = 'Error de conexión'
        tex = 'La tabla Vuelos no es accesible en este momento en la base de datos'
        print('error al mostrar productos')
    return listo

def actualizarClientes(idp, nombre, direccion, email, telefono):
    con = ConexionDB()
    try:
        sql = "UPDATE Clientes SET nombre=?, direccion=?, email=?, telefono=? WHERE id=?"
        data = (nombre, direccion, email, telefono, idp)
        con.cursor.execute(sql, data)
        print("Cliente actualizado correctamente.")
    except Exception as e:
        print(f"Error al actualizar cliente: {e}")
        return e
    con.closeConexion()

def crearCliente(datos_cliente):
    con = ConexionDB()
    try:
        con.cursor.execute("INSERT INTO clientes (nombre, direccion, email, telefono) VALUES (?, ?, ?, ?)", (datos_cliente))
        con.conexion.commit()
        con.closeConexion()
        return True
    except:
        con.conexion.rollback()
        ti = 'Error al crear el Cliente'
        tex = 'No se pudo crear el cliente en este momento en la base de datos'
        print('error al crear cliente')
        return False


################################################Reservas########################################################  
def mostrarReservas():
    con = ConexionDB()
    sql = """SELECT * FROM  Reservas"""
    listo = []
    try:
        listo = con.cursor.execute(sql).fetchall()
        con.closeConexion()
    except:
        ti = 'Error de conexión'
        tex = 'La tabla Vuelos no es accesible en este momento en la base de datos'
        print('error al mostrar productos')
    return listo

def crearReserva(datos_producto):
    con = ConexionDB()
    try:
        con.cursor.execute("INSERT INTO Reserva (nombre, cantidad_en_stock, precio, categoria, proveedor_id, precio_distintivo) VALUES (?, ?, ?,?,?,?)", (datos_producto))
        con.conexion.commit()
        con.closeConexion()
        return True
    except:
        con.conexion.rollback()
        ti = 'Error al crear el Usuario'
        tex = 'No se pudo crear el producto en este momento en la base de datos'
        print('error al crear producto')
        return False

def actualizarReserva(idp, cliente_id, producto_id, cantidad_reservada, estado):
    con = ConexionDB()
    try:
        sql = "UPDATE Reservas SET cliente_id=?, producto_id=?, cantidad_reservada=?, estado=? WHERE id=?"
        data = (cliente_id, producto_id, cantidad_reservada, estado, idp)
        con.cursor.execute(sql, data)
        print("Reserva actualizada correctamente.")
    except Exception as e:
        print(f"Error al actualizar reserva: {e}")
        return e
    con.closeConexion()

