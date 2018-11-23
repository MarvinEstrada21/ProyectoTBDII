import sys
import redis
from PyQt5.QtGui import QIcon

redisClient = redis.StrictRedis(host='localhost', port=6379, db=0)

from PyQt5 import uic, QtWidgets

qtCreatorFile = "Quinielas.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

Jugador = []
Equipo = []
Club = []


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btnAgregarJugador.clicked.connect(self.addjugador)
        self.btnAgregarEntrenador.clicked.connect(self.addEntrenador)
        self.btnAgregarArbitro.clicked.connect(self.addArbitro)
        self.btnAgregarClub.clicked.connect(self.addClub)
        self.btneliminarjugador.clicked.connect(self.hdelJugador)
        #Cargar combobox de Clubes
        self.btnAgregarClub.clicked.connect(self.loadClubes)

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
        Club = [nombre]
        #Club = [self.tr(id), self.tr(nombre)]
        print(Club)
        #self.cbClubEquipo.clear()
        #self.cbClubEquipo.addItems(Club)
        self.cbClubEquipo.clear()
        for e in Club:
            self.cbClubEquipo.addItem(e.str)


    def hdelJugador(self):
        id = self.idjugador.text()
        nombre = self.nombrejugador.text()
        apellido = self.apellidojugador.text()
        edad = self.edadjugador.text()
        posicion = self.posicionjugador.text()
        peso = self.pesojugador.text()
        redisClient.hdel("Nombre_Jugador", id, nombre)
        redisClient.hdel("Apellido_Jugador", id, apellido)
        redisClient.hdel("Edad_Jugador", id, edad)
        redisClient.hdel("Posicion_Jugador", id, posicion)
        redisClient.hdel("Peso_Jugador", id, peso)

    #def asignarClub(self):
    #    Club.append(self.cbClubEquipo.currentText())
    #    index = self.cbClubEquipo.currentIndex()
    #    self.cbCLubEquipo.removeItem(index)

    def loadClubes(self):
        #self.cbClubEquipo.clear()
        #for e in redisClient.hget("Nombre_Club", self.idclub.text()):
            #self.cbClubEquipo.addItem(e.get('value'))
        self.cbClubEquipo.clear()
        self.cbClubEquipo.addItems(Club)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())