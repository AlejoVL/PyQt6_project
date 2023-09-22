from PyQt6.QtCore import QPropertyAnimation
from PyQt6 import QtCore, QtWidgets
from modules.consultas import *
from PyQt6.QtWidgets import QMainWindow, QApplication , QTableWidgetItem


#funciones de os botones principales para mostrar las ventanas
def botones(self):
        self.btn_reservas.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.reservas))
        self.btn_despacho.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.despacho))
        self.btn_proveedores.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.proveedores))
        self.btn_inventario.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.inventario))
        self.btn_clientes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.clientes))
        
        
def abrirVentana(self):
        width = self.rigthMenu.width()
        normal = 0
        extender = 0 if width == 350 else normal
        self.animacion = QPropertyAnimation(self.rigthMenu, b'minimumWidth')
        self.animacion.setDuration(300)
        self.animacion.setStartValue(width)
        self.animacion.setEndValue(extender)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuart)
        self.animacion.start()


#funciones para mostrar y seleccionar los datos en la tabla 

###################################################Productos###################################################################

def mostrar_produtos(self):
        datos = mostrarProductos()
        self.tbl_productos.setRowCount(0)  # Limpiar la tabla antes de agregar nuevos datos
        for fila_num, fila_datos in enumerate(datos):
         self.tbl_productos.insertRow(fila_num)
         for col_num, valor in enumerate(fila_datos):
            item = QTableWidgetItem(str(valor))
            self.tbl_productos.setItem(fila_num, col_num, item)

def cargar_datos(self):
        items_seleccionados = self.tbl_productos.selectedItems()
        detalles = [item.text() for item in items_seleccionados]
        if len(detalles) == 7:
            self.reg_eliminarI.setText(detalles[0]) 
            self.reg_nI.setText(detalles[1]) 
            self.reg_sI.setText(detalles[2]) 
            self.reg_pI.setText(detalles[3]) 
            self.reg_cI.setText(detalles[4]) 
            self.reg_proI.setText(detalles[5]) 
            self.reg_dI.setText(detalles[6]) 
            return detalles


###################################################Despachos###################################################################


def mostrar_despachos(self):
        datos = mostrarDespachos()
        self.tbl_despacho.setRowCount(0)  # Limpiar la tabla antes de agregar nuevos datos
        for fila_num, fila_datos in enumerate(datos):
         self.tbl_despacho.insertRow(fila_num)
         for col_num, valor in enumerate(fila_datos):
            item = QTableWidgetItem(str(valor))
            self.tbl_despacho.setItem(fila_num, col_num, item)

def cargar_datos_despacho(self):
        items_seleccionados = self.tbl_despacho.selectedItems()
        detalles = [item.text() for item in items_seleccionados]
        if len(detalles) == 5:
            self.lineEdit_71.setText(detalles[0]) 
            self.lineEdit_44.setText(detalles[1]) 
            self.lineEdit_45.setText(detalles[2]) 
            self.lineEdit_46.setText(detalles[3]) 
            self.lineEdit_47.setText(detalles[4])
            return detalles


###################################################Proveedores###################################################################


def mostrar_proveedores(self):
        datos =  mostrarProveedores()
        self.tbl_proveedores.setRowCount(0)  # Limpiar la tabla antes de agregar nuevos datos
        for fila_num, fila_datos in enumerate(datos):
         self.tbl_proveedores.insertRow(fila_num)
         for col_num, valor in enumerate(fila_datos):
            item = QTableWidgetItem(str(valor))
            self.tbl_proveedores.setItem(fila_num, col_num, item)
            
def cargar_datos_prov(self):
        items_seleccionados = self.tbl_proveedores.selectedItems()
        detalles = [item.text() for item in items_seleccionados]
        if len(detalles) == 4:
            self.lineEdit_68.setText(detalles[0]) 
            self.lineEdit_50.setText(detalles[1]) 
            self.lineEdit_51.setText(detalles[2]) 
            self.lineEdit_52.setText(detalles[3]) 
            return detalles


 ###################################################Despachos###################################################################

###################################################Reservas###################################################################


def mostrar_reservas(self):
        datos = mostrarReservas()
        self.tbl_reservas.setRowCount(0)  # Limpiar la tabla antes de agregar nuevos datos
        for fila_num, fila_datos in enumerate(datos):
         self.tbl_reservas.insertRow(fila_num)
         for col_num, valor in enumerate(fila_datos):
            item = QTableWidgetItem(str(valor))
            self.tbl_reservas.setItem(fila_num, col_num, item)
 
def cargar_datos_rev(self):
        items_seleccionados = self.tbl_reservas.selectedItems()
        detalles = [item.text() for item in items_seleccionados]
        if len(detalles) == 5:
            self.lineEdit_69.setText(detalles[0]) 
            self.lineEdit_56.setText(detalles[1]) 
            self.lineEdit_57.setText(detalles[2]) 
            self.lineEdit_58.setText(detalles[3])
            self.lineEdit_59.setText(detalles[3]) 
            return detalles



def mostrar_clientes(self):
        datos = mostrarClientes()
        self.tbl_clientes.setRowCount(0)  # Limpiar la tabla antes de agregar nuevos datos
        for fila_num, fila_datos in enumerate(datos):
         self.tbl_clientes.insertRow(fila_num)
         for col_num, valor in enumerate(fila_datos):
            item = QTableWidgetItem(str(valor))
            self.tbl_clientes.setItem(fila_num, col_num, item)
       
def cargar_datos_clientes(self):
        items_seleccionados = self.tbl_clientes.selectedItems()
        detalles = [item.text() for item in items_seleccionados]
        if len(detalles) == 5:
            self.lineEdit_70.setText(detalles[0]) 
            self.lineEdit_62.setText(detalles[1]) 
            self.lineEdit_63.setText(detalles[2]) 
            self.lineEdit_64.setText(detalles[3])
            self.lineEdit_65.setText(detalles[4]) 
            return detalles