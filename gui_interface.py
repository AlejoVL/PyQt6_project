from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QPropertyAnimation
from PyQt6.QtWidgets import QMainWindow, QApplication , QTableWidgetItem, QMessageBox
from PyQt6.uic import loadUi
from funciones import *
from  modules.consultas import *
from  modules.conzultaz import *

from PyQt6.QtWidgets import QMessageBox


class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('inventario.ui', self)        
        self.show()
        self.stackedWidget.setCurrentWidget(self.page)
        mostrar_produtos(self)
        mostrar_despachos(self)
        mostrar_proveedores(self)
        mostrar_reservas(self)
        mostrar_clientes(self)
        botones(self)
        
        # Eliminar barra de título de Windows
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setWindowOpacity(1)
        
        # Botones personalizados ventana principal
        self.btn_cerrar.clicked.connect(self.close)
        self.btn_minimizar.clicked.connect(self.showMinimized)
        self.btn_maximizar.clicked.connect(self.toggle_maximized)
        self.is_maximized = False

        #boton abrir menu principal
        self.btn_menu.clicked.connect(self.moverVentana)
        
        #botones dentro de la barra derecha  o menu secundario

        #Inventario
        self.agregarI.clicked.connect(self.crear_producto)
        self.btn_editarI.clicked.connect(self.actualizar_productos)
        self.eliminarI.clicked.connect(self.eliminar_Producto)
        #Despacho
        self.pushButton_8.clicked.connect(self.crear_despacho)
        self.pushButton_15.clicked.connect(self.actualizar_despachos)
        self.pushButton_29.clicked.connect(self.eliminar_despachos)
        #Proveedores
        self.pushButton_10.clicked.connect(self.crear_proveedores)
        self.pushButton_17.clicked.connect(self.actualizar_proveedores)
        self.pushButton_23.clicked.connect(self.eliminar_proveedores)
        #Reservas
        self.pushButton_12.clicked.connect(self.crear_reserva)
        self.pushButton_19.clicked.connect(self.actualizar_reserva)
        self.pushButton_25.clicked.connect(self.eliminar_reservas)
        #Clientes
        self.pushButton_14.clicked.connect(self.crear_cliente)
        self.pushButton_21.clicked.connect(self.actualizar_cliente)
        self.pushButton_27.clicked.connect(self.eliminar_cliente)


        #botones en la parte inferior para abrir el menu secundario en el lado derecho
        self.btn_agregar.clicked.connect(self.logica)
        self.btn_editar.clicked.connect(self.logica)
        self.btn_eliminar.clicked.connect(self.logica)
         
        self.btn_agregarD.clicked.connect(self.logica)
        self.btn_editarD.clicked.connect(self.logica)
        self.btn_eliminarD.clicked.connect(self.logica)
        
        self.btn_agregarP.clicked.connect(self.logica)
        self.btn_editarP.clicked.connect(self.logica)
        self.btn_eliminarP.clicked.connect(self.logica)
        
        self.btn_agregarR.clicked.connect(self.logica)
        self.btn_editarR.clicked.connect(self.logica)
        self.btn_eliminarR.clicked.connect(self.logica)
        
        self.btn_agregarC.clicked.connect(self.logica)
        self.btn_editarC.clicked.connect(self.logica)
        self.btn_eliminarC.clicked.connect(self.logica)


        
    def toggle_maximized(self):
        if self.is_maximized:
            self.showNormal()
            self.is_maximized = False
        else:
            self.showMaximized()
            self.is_maximized = True
            

            #Abre ventana izquierda
    def moverVentana(self):
        width = self.letfMenu.width()
        normal = 0
        extender = 300 if width == 0 else normal
        self.animacion = QPropertyAnimation(self.letfMenu, b'minimumWidth')
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animacion.start()
        
        #Abre ventana derecha
    def moverVentana2(self):
        width = self.rigthMenu.width()
        normal = 0
        extender = 350 if width == 0 else normal
        self.animacion = QPropertyAnimation(self.rigthMenu, b'minimumWidth')
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animacion.start()
    
    def logica(self):
        self.vent()

        #Ventanas inventario

        #Editar
        if self.btn_editar.clicked:
            self.btn_editar.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.editar))
            self.idd = cargar_datos(self)
        #Agregar
        if self.btn_agregar.clicked:
            self.btn_agregar.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.agregar))
        #Eliminar
        if self.btn_eliminar.clicked:
            self.btn_eliminar.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.eliminar))
            cargar_datos(self)

        #Ventanas despachos

        #Editar
        if self.btn_editarD.clicked:
            self.btn_editarD.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.editarD))
            self.idDesup = cargar_datos_despacho(self)
        #Agregar
        if self.btn_agregarD.clicked:
            self.btn_agregarD.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.agregarD))
             
        #Eliminar    
        if self.btn_eliminarD.clicked:
            self.btn_eliminarD.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.eliminarD))
            self.idDesdel = cargar_datos_despacho(self)
             
        #Ventanas proveedores

        #Editar
        if self.btn_editarP.clicked:
            self.btn_editarP.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.editarP))
            self.idProvup = cargar_datos_prov(self)
        #Agregar
        if self.btn_agregarP.clicked:
             self.btn_agregarP.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.agregarP))
        #Eliminar    
        if self.btn_eliminarP.clicked:
            self.btn_eliminarP.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.eliminarP))
            self.idProvdel = cargar_datos_prov(self)
 
        #Ventana Reservas

        #Editar
        if self.btn_editarR.clicked:
            self.btn_editarR.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.editarR))
            self.idRevup = cargar_datos_rev(self)
        #Agregar
        if self.btn_agregarR.clicked:
            self.btn_agregarR.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.agregarR))
        #Eliminar
        if self.btn_eliminarR.clicked:
            self.btn_eliminarR.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.eliminarR))
            self.idRevdel = cargar_datos_rev(self)
        
        #Ventana Clientes

        #Editar
        if self.btn_editarC.clicked:
            self.btn_editarC.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.editarC))
            self.idCliup = cargar_datos_clientes(self)

        #Agregar
        if self.btn_agregarC.clicked:
            self.btn_agregarC.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.agregarC)) 
        #Eliminar
        if self.btn_eliminarC.clicked:
            self.btn_eliminarC.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.eliminarC))
            self.idClidel =cargar_datos_clientes(self)


    def vent(self):
        #Al dar click se abre la ventana de la derecha
        self.btn_agregarP.clicked.connect(self.moverVentana2)  
        self.btn_editarP.clicked.connect(self.moverVentana2)  
        self.btn_eliminarP.clicked.connect(self.moverVentana2)
        
        self.btn_agregar.clicked.connect(self.moverVentana2)  
        self.btn_editar.clicked.connect(self.moverVentana2)  
        self.btn_eliminar.clicked.connect(self.moverVentana2)
        
        self.btn_agregarD.clicked.connect(self.moverVentana2)  
        self.btn_editarD.clicked.connect(self.moverVentana2)  
        self.btn_eliminarD.clicked.connect(self.moverVentana2)
        
        self.btn_agregarR.clicked.connect(self.moverVentana2)  
        self.btn_editarR.clicked.connect(self.moverVentana2)  
        self.btn_eliminarR.clicked.connect(self.moverVentana2)
        
        self.btn_agregarC.clicked.connect(self.moverVentana2)  
        self.btn_editarC.clicked.connect(self.moverVentana2)  
        self.btn_eliminarC.clicked.connect(self.moverVentana2)

        #Botones para cerrar ventana derecha
        #Todos agregar
        self.pushButton_5.clicked.connect(self.moverVentana2)
        self.pushButton_13.clicked.connect(self.moverVentana2)
        self.pushButton_7.clicked.connect(self.moverVentana2)
        self.pushButton_9.clicked.connect(self.moverVentana2)  
        self.pushButton_11.clicked.connect(self.moverVentana2)  
        #Todos Editar
        self.pushButton_4.clicked.connect(self.moverVentana2)
        self.pushButton_22.clicked.connect(self.moverVentana2)
        self.pushButton_16.clicked.connect(self.moverVentana2)
        self.pushButton_18.clicked.connect(self.moverVentana2)  
        self.pushButton_20.clicked.connect(self.moverVentana2)
        #Todos Eliminar
        self.pushButton_2.clicked.connect(self.moverVentana2)
        self.pushButton_28.clicked.connect(self.moverVentana2)  
        self.pushButton_30.clicked.connect(self.moverVentana2)  
        self.pushButton_24.clicked.connect(self.moverVentana2)
        self.pushButton_26.clicked.connect(self.moverVentana2)
    
    ##########################################Crear################################################################
    
    def crear_producto(self):
        try:
            nombre = self.reg_n.text()
            cantidad_en_stock= self.reg_s.text()
            precio = self.reg_p.text()
            categoria = self.reg_c.text()
            proveedor_id = self.reg_pro.text()
            precio_distintivo = self.reg_d.text()
            datos_producto = (nombre, cantidad_en_stock, precio, categoria, proveedor_id, precio_distintivo)
            crearProducto(datos_producto)
        except Exception as e:
                QMessageBox.information(self, 'Mensaje', 'No se puede crear el producto revise sus datos.')
        mostrar_produtos(self)

    def crear_despacho(self):
        try:
            if readProd2(self.lineEdit_21.text()) != 0: # comprueba si el producto existe en la base de datos
                ret = readProd2(self.lineEdit_21.text())[2] - (int(self.lineEdit_22.text())) # calculo de resta numero en stock - numero de cantidad
                if readProd2(self.lineEdit_21.text())[2] > 0 and ret >= 0: #comprobacion cantidad de producto existente
                    updProd2(self.lineEdit_21.text(), ret) # funcion actualizar cantidad producto en stock junto con la reduccion
                    insDesp(self.lineEdit_20.text(), self.lineEdit_21.text(), self.lineEdit_22.text(), self.lineEdit_23.text()) # Agregar el despacho
                else: print("Producto no esta disponible en Stock, no se puede crear el despacho")
            else: print("Producto no existe en base de datos, no se puede crear el despacho")
        except Exception as e:
                QMessageBox.information(self, 'Mensaje', 'No se puede crear el despacho revise sus datos.')
        mostrar_despachos(self)
        mostrar_produtos(self)

    def crear_proveedores(self):
        try:
            insProv(self.lineEdit_26.text(), self.lineEdit_27.text(), self.lineEdit_28.text())
        except Exception as e:
            QMessageBox.information(self, 'Mensaje', 'No se puede crear el proveedor revise sus datos.')

        mostrar_proveedores(self)

    def crear_reserva(self):
        try:
            if readProd2(self.lineEdit_33.text())[2] <= 0: # comprueba por id el valor de stock si esta en 0
                insRev(self.lineEdit_32.text(), self.lineEdit_33.text(), self.lineEdit_34.text(), self.lineEdit_35.text())
            else: print("Producto esta disponible en Stock, no se puede crear la reserva")
            mostrar_reservas(self)
        except Exception as e:
            QMessageBox.information(self, 'Mensaje', 'No se puede crear la reserva revise sus datos.')

    def crear_cliente(self):
        try:
            insCli(self.lineEdit_38.text(), self.lineEdit_39.text(), self.lineEdit_40.text(), self.lineEdit_41.text())
        except Exception as e:
            QMessageBox.information(self, 'Mensaje', 'No se puede crear el cliente revise sus datos.')
        mostrar_clientes(self)
   #############################################ACTUALIZAR#####################################################  
                          
    def actualizar_productos(self):
        try:
            items_seleccionados = self.tbl_productos.selectedItems()
            detalles = [item.text() for item in items_seleccionados]
            nombre = self.reg_nI.text()
            cantidad_en_stock= self.reg_sI.text()
            precio = self.reg_pI.text()
            categoria = self.reg_cI.text()
            proveedor_id = self.reg_proI.text()
            precio_distintivo = self.reg_dI.text()
            actProd(nombre,cantidad_en_stock,precio,categoria,proveedor_id,precio_distintivo ,detalles[0])
            chkrev =readRev2(detalles[0])
            print(detalles)
            print(chkrev, " Chkrev")
            if chkrev!=0 and int(cantidad_en_stock) >= chkrev[3]:
                ret = readProd2(detalles[0])[2] - int(chkrev[3]) # calculo de resta numero en stock - numero de cantidad
                updProd2(detalles[0], ret) # funcion actualizar cantidad producto en stock junto con la reduccion
                delRev(chkrev[0])
                insDesp(chkrev[1], chkrev[2], chkrev[3], "Fecha actual") # Agregar el despacho
            else: 
                    print("Producto no esta disponible en Stock, no se puede crear el despacho")
        except Exception as e:    
            QMessageBox.information(self, 'Mensaje', 'Debes Seleccionar una fila.')
        mostrar_reservas(self)
        mostrar_produtos(self)
        mostrar_despachos(self)


    def actualizar_despachos(self):
        try:
            updDesp(self.idDesup[0], self.lineEdit_44.text(), self.lineEdit_45.text(), self.lineEdit_46.text(), self.lineEdit_47.text())
            mostrar_despachos(self)
        except Exception as e:
            QMessageBox.information(self, 'Mensaje', 'Debes Seleccionar una fila.')

    def actualizar_proveedores(self):
        try:
            updProv(self.idProvup[0], self.lineEdit_50.text(), self.lineEdit_51.text(), self.lineEdit_52.text())
            mostrar_proveedores(self)
        except Exception as e:
            QMessageBox.information(self, 'Mensaje', 'Debes Seleccionar una fila.')

    
    def actualizar_reserva(self):
        try:
            updRev(self.idRevup[0], self.lineEdit_56.text(), self.lineEdit_57.text(), self.lineEdit_58.text(), self.lineEdit_59.text())
            mostrar_reservas(self)
        except Exception as e:
            QMessageBox.information(self, 'Mensaje', 'Debes Seleccionar una fila.')

    def actualizar_cliente(self):
        try:
            updCli(self.idCliup[0], self.lineEdit_62.text(), self.lineEdit_63.text(), self.lineEdit_64.text(), self.lineEdit_65.text())
            mostrar_clientes(self)
        except Exception as e:
            QMessageBox.information(self, 'Mensaje', 'Debes Seleccionar una fila.')

####################################################Elimianr#####################################################

    def eliminar_Producto(self):
        try:
            items_seleccionados = self.tbl_productos.selectedItems()
            detalles = [item.text() for item in items_seleccionados]
            eliminar_producto(detalles[0])
            mostrar_produtos(self)
        except Exception as e:
            QMessageBox.information(self, 'Mensaje', 'Debes Seleccionar una fila.')

    def eliminar_despachos(self):
        get = readDesp2(self.idDesdel[0]) # obtener datos del despacho por iddespacho idproducto y cantidad
        print(get)
        try:
            if get != 0 :
                updProd2(get[2], readProd2(get[2])[2] + get[3]) # funcion actualizar cantidad producto en stock junto con la adicion
            else:
                print("No existe el producto en base de datos")
        except Exception as e:
            print("solo se eliminara el producto, id no existe en base de datos")
        delDesp(self.idDesdel[0])
        mostrar_despachos(self)
        mostrar_produtos(self)

    def eliminar_proveedores(self):
        try:
            delProv(self.idProvdel[0])
            mostrar_proveedores(self)
        except Exception as e:
            QMessageBox.information(self, 'Mensaje', 'Debes Seleccionar una fila.')

    def eliminar_reservas(self):
        try:
            delRev(self.idRevdel[0])
            mostrar_reservas(self)
        except Exception as e:
            QMessageBox.information(self, 'Mensaje', 'Debes Seleccionar una fila.')
    
    def eliminar_cliente(self):
        try:
            delCli(self.idClidel[0])
            mostrar_clientes(self)
        except Exception as e:
            QMessageBox.information(self, 'Mensaje', 'Debes Seleccionar una fila.')



