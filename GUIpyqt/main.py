import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.button1 = QPushButton()
        self.button1.setIcon(QIcon("marcoAzul.png"))  # Ruta de la primera imagen
        self.button1.setIconSize(QSize(250, 250))  # Tamaño del icono
        self.button1.setObjectName("Marco azul")


        self.button2 = QPushButton()
        self.button2.setIcon(QIcon("marcoRojo.png"))  # Ruta de la segunda imagen
        self.button2.setIconSize(QSize(250, 250))  # Tamaño del icono
        self.button2.setObjectName("Marco rojo")


        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        self.button1.clicked.connect(self.button_clicked)
        self.button2.clicked.connect(self.button_clicked)

        self.setFixedSize(300, 600)  # Tamaño fijo de la ventana principal

    def button_clicked(self):
        sender = self.sender()  # Obtener el botón que generó el evento
        button_name = sender.objectName()  # Obtener el nombre del botón

        # Realizar acciones según el nombre del botón
        if button_name == "Marco azul":
            print("Se pulsó el Boton 1")
            # Acciones específicas para el Boton 1
        elif button_name == "Boton 2":
            print("Se pulsó el Marco rojo")
            # Acciones específicas para el Boton 2

        self.close()  # Cerrar la ventana

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())
