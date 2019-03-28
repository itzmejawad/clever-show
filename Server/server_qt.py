import glob

from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import QModelIndex
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtWidgets import QFileDialog

# Importing gui form
from server_gui import Ui_MainWindow

from server import *
class CopterView(QStandardItemModel):
    pass

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        self.show()

    def initUI(self):
        #Connecting
        self.ui.check_button.clicked.connect(self.check_selected)
        self.ui.start_button.clicked.connect(self.send_starttime)
        self.ui.pause_button.clicked.connect(self.pause_all)
        self.ui.stop_button.clicked.connect(self.stop_all)

        self.ui.leds_button.clicked.connect(self.test_leds)
        self.ui.takeoff_button.clicked.connect(self.takeoff_selected)
        self.ui.land_button.clicked.connect(self.land_all)
        self.ui.disarm_button.clicked.connect(self.disarm_all)

        self.ui.action_send_animations.triggered.connect(self.send_animations)
        self.ui.action_send_configurations.triggered.connect(self.send_configurations)
        self.ui.action_send_Aruco_map.triggered.connect(self.send_aruco)

        #Initing table and table model
        self.ui.tableView.setModel(model)
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)

    @pyqtSlot()
    def check_selected(self):
        for row_num in range(model.rowCount()):
            item = model.item(row_num, 0)
            if item.isCheckable() and item.checkState() == Qt.Checked:
                print("Copter {} checked".format(model.item(row_num, 0).text()))
                batt_total = Client.get_by_id(item.text()).get_response("batt_voltage")
                batt_cell = Client.get_by_id(item.text()).get_response("cell_voltage")
                selfcheck = Client.get_by_id(item.text()).get_response("selfcheck")

                batt_percent = (batt_cell-3.2)/(4.2-3.2)

                model.setData(model.index(0, 2), "{} V.".format(round(batt_total, 3)))
                model.setData(model.index(0, 3), "{} %".format(round(batt_percent, 3)))
                model.setData(model.index(0, 3), selfcheck)

        self.ui.start_button.setEnabled(True)
        self.ui.takeoff_button.setEnabled(True)


    @pyqtSlot()
    def send_starttime(self):
        dt = self.ui.start_delay_spin.value()
        server.send_starttime(dt)

    @pyqtSlot()
    def stop_all(self):
        Client.broadcast(Client.form_message("stop"))

    @pyqtSlot()
    def pause_all(self):
        if self.ui.pause_button.text() == 'Pause':
            Client.broadcast(Client.form_message('pause'))
            self.ui.pause_button.setText('Resume')
        else:
            Client.broadcast(Client.form_message('resume'))
        self.ui.pause_button.setText('Pause')

    @pyqtSlot()
    def test_leds(self):
        Client.send_to_selected(Client.form_message("led_test"))

    @pyqtSlot()
    def takeoff_selected(self):
        Client.send_to_selected(Client.form_message("takeoff"))

    @pyqtSlot()
    def land_all(self):
        Client.broadcast(Client.form_message("land"))

    @pyqtSlot()
    def disarm_all(self):
        Client.broadcast(Client.form_message("disarm"))

    @pyqtSlot()
    def send_animations(self):
        path = str(QFileDialog.getExistingDirectory(self, "Select Animation Directory"))
        if path:
            print("Selected directory:", path)
            files = [file for file in glob.glob(path + '/*.csv')]
            names = [os.path.basename(file).split(".")[0] for file in files]
            print(files)
            for file, name in zip(files, names):
                for copter in Client.clients.values():
                    if name == copter.copter_id:
                        copter.send_file(file, "animation.csv")  # TODO config
                    else:
                        print("Filename not matches with any drone connected")

    @pyqtSlot()
    def send_configurations(self):
        path = QFileDialog.getOpenFileName(self, "Select configuration file", filter="Configs (*.ini *.txt .cfg)")[0]
        if path:
            print("Selected file:", path)
            sendable_config = configparser.ConfigParser()
            sendable_config.read(path)
            options = []
            for section in sendable_config.sections():
                for option in dict(sendable_config.items(section)):
                    value = sendable_config[section][option]
                    print("Got item from config:", section, option, value)
                    options.append(ConfigOption(section, option, value))
            Client.send_config_options(*options)

    @pyqtSlot()
    def send_aruco(self):
        path = QFileDialog.getOpenFileName(self, "Select aruco map configuration file", filter="Configs (*.txt)")[0]
        if path:
            filename = os.path.basename(path)
            print("Selected file:", path, filename)
            for copter in Client.clients.values():
                copter.send_file(path, "/home/pi/catkin_ws/src/clever/aruco_pose/map/animation_map.txt")


model = QStandardItemModel()
model.setHorizontalHeaderLabels(
    ('copter ID', 'animation ID', 'battery V', 'battery %', 'selfcheck', 'time UTC')
)
model.setColumnCount(6)
model.setRowCount(0)


def client_connected(self: Client):
    copter_id_item = QStandardItem(self.copter_id)
    copter_id_item.setCheckable(True)
    model.appendRow((copter_id_item, ))  # TODO: get responses for another columns


Client.on_connect = client_connected


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()

    server = Server()
    server.start()

    app.exec_()
    server.stop()
    sys.exit()
