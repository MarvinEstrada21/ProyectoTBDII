import sys
import redis

redisClient = redis.StrictRedis(host='localhost', port=6379, db=0)

from PyQt5 import uic, QtWidgets

qtCreatorFile = "Quinielas.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btnAgregarJugador.clicked.connect(self.addjugador)
        self.btnAgregarEntrenador.clicked.connect(self.addEntrenador)
        self.btnAgregarArbitro.clicked.connect(self.addArbitro)
        self.btnAgregarClub.clicked.connect(self.addClub)

    def addjugador(self):
        id = self.idjugador.text()
        nombre = self.nombrejugador.text()
        apellido = self.apellidojugador.text()
        edad = self.edadjugador.text()
        posicion = self.posicionjugador.text()
        peso = self.pesojugador.text()
        redisClient.hset("Nombre_Jugador", id, nombre)
        redisClient.hset("Apellido_Jugador", id, apellido)
        redisClient.hset("Edad_Jugador", id, edad)
        redisClient.hset("Posicion_Jugador", id, posicion)
        redisClient.hset("Peso_Jugador", id, peso)

    def eliminarjugador(self):
        redisClient.hgetall(self.handelactivad(

        ))

    def addEntrenador(self):
        id = self.identrenador.text()
        nombre = self.nombreentrenador.text()
        apellido = self.apellidoentrenador.text()
        edad = self.edadentrenador.text()
        peso = self.pesoentrenador.text()

        redisClient.hset("Nombre_Entrenador", id, nombre)
        redisClient.hset("Apellido_Entrenador", id, apellido)
        redisClient.hset("Edad_Entrenador", id, edad)
        redisClient.hset("Peso_Entrenador", id, peso)

    def addArbitro(self):
        id = self.idarbitro.text()
        nombre = self.nombrearbitro.text()
        apellido = self.apellidoarbitro.text()
        edad = self.edadarbitro.text()
        peso = self.pesoarbitro.text()
        redisClient.hset("Nombre_Arbitro", id, nombre)
        redisClient.hset("Apellido_Arbitro", id, apellido)
        redisClient.hset("Edad_Arbitro", id, edad)
        redisClient.hset("Peso_Arbitro", id, peso)

    def addEquipo(self):
        id = self.idequipo.text()
        nombre = self.nombreequipo.text()
        jugador = self.txtEquipoJugador.text()
        entrenador = self.txtEquipoEntrenador.text()
        club = self.txtEquipoClub.text()
        redisClient.hset("Nombre_Equipo", id, nombre)
        redisClient.hset("Jugadores_Equipo", id, jugador)
        redisClient.hset("Entrenador_Equipo", id, entrenador)
        redisClient.hset("Club_Equipo", id, club)

    def addClub(self):
        id = self.idclub.text()
        nombre = self.nombreclub.text()
        redisClient.hset("Nombre_Club", id, nombre)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())