# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1360, 761)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableView.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableView.setSortingEnabled(True)
        self.tableView.setWordWrap(True)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setCascadingSectionResizes(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(50)
        self.tableView.horizontalHeader().setMinimumSectionSize(50)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.tableView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setObjectName("formLayout")
        self.music_text = QtWidgets.QLabel(self.centralwidget)
        self.music_text.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.music_text.setObjectName("music_text")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.music_text)
        self.music_delay_spin = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.music_delay_spin.setDecimals(1)
        self.music_delay_spin.setMaximum(1000.0)
        self.music_delay_spin.setObjectName("music_delay_spin")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.music_delay_spin)
        self.music_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.music_checkbox.sizePolicy().hasHeightForWidth())
        self.music_checkbox.setSizePolicy(sizePolicy)
        self.music_checkbox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.music_checkbox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.music_checkbox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.music_checkbox.setAutoFillBackground(False)
        self.music_checkbox.setText("")
        self.music_checkbox.setChecked(False)
        self.music_checkbox.setObjectName("music_checkbox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.music_checkbox)
        self.music_play_text = QtWidgets.QLabel(self.centralwidget)
        self.music_play_text.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.music_play_text.setObjectName("music_play_text")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.music_play_text)
        self.start_delay_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.start_delay_spin.setObjectName("start_delay_spin")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.start_delay_spin)
        self.start_text = QtWidgets.QLabel(self.centralwidget)
        self.start_text.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.start_text.setAlignment(QtCore.Qt.AlignCenter)
        self.start_text.setObjectName("start_text")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.start_text)
        self.verticalLayout.addLayout(self.formLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setObjectName("stop_button")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.stop_button)
        self.pause_button = QtWidgets.QPushButton(self.centralwidget)
        self.pause_button.setObjectName("pause_button")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.pause_button)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setEnabled(True)
        self.start_button.setFlat(False)
        self.start_button.setObjectName("start_button")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.start_button)
        self.check_button = QtWidgets.QPushButton(self.centralwidget)
        self.check_button.setEnabled(True)
        self.check_button.setObjectName("check_button")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.check_button)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_3.setVerticalSpacing(6)
        self.formLayout_3.setObjectName("formLayout_3")
        self.disarm_all_button = QtWidgets.QPushButton(self.centralwidget)
        self.disarm_all_button.setObjectName("disarm_all_button")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.disarm_all_button)
        self.disarm_button = QtWidgets.QPushButton(self.centralwidget)
        self.disarm_button.setObjectName("disarm_button")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.disarm_button)
        self.emergency_button = QtWidgets.QPushButton(self.centralwidget)
        self.emergency_button.setObjectName("emergency_button")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.emergency_button)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_4.setObjectName("formLayout_4")
        self.land_button = QtWidgets.QPushButton(self.centralwidget)
        self.land_button.setObjectName("land_button")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.land_button)
        self.flip_button = QtWidgets.QPushButton(self.centralwidget)
        self.flip_button.setObjectName("flip_button")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.flip_button)
        self.takeoff_button = QtWidgets.QPushButton(self.centralwidget)
        self.takeoff_button.setEnabled(True)
        self.takeoff_button.setObjectName("takeoff_button")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.takeoff_button)
        self.leds_button = QtWidgets.QPushButton(self.centralwidget)
        self.leds_button.setObjectName("leds_button")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leds_button)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.z_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.z_checkbox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.z_checkbox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.z_checkbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.z_checkbox.setObjectName("z_checkbox")
        self.horizontalLayout_2.addWidget(self.z_checkbox)
        self.z_spin = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.z_spin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.z_spin.setDecimals(1)
        self.z_spin.setProperty("value", 1.0)
        self.z_spin.setObjectName("z_spin")
        self.horizontalLayout_2.addWidget(self.z_spin)
        self.formLayout_4.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.formLayout_4)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_6.setObjectName("formLayout_6")
        self.reboot_fcu = QtWidgets.QPushButton(self.centralwidget)
        self.reboot_fcu.setObjectName("reboot_fcu")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.reboot_fcu)
        self.calibrate_gyro = QtWidgets.QPushButton(self.centralwidget)
        self.calibrate_gyro.setObjectName("calibrate_gyro")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.calibrate_gyro)
        self.calibrate_level = QtWidgets.QPushButton(self.centralwidget)
        self.calibrate_level.setObjectName("calibrate_level")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.calibrate_level)
        self.verticalLayout.addLayout(self.formLayout_6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1360, 25))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuDeveloper_mode = QtWidgets.QMenu(self.menuOptions)
        self.menuDeveloper_mode.setObjectName("menuDeveloper_mode")
        self.menuAnimation = QtWidgets.QMenu(self.menubar)
        self.menuAnimation.setObjectName("menuAnimation")
        self.menuDrone = QtWidgets.QMenu(self.menubar)
        self.menuDrone.setObjectName("menuDrone")
        self.menuDeveloper_mode_2 = QtWidgets.QMenu(self.menuDrone)
        self.menuDeveloper_mode_2.setObjectName("menuDeveloper_mode_2")
        self.menuMusic = QtWidgets.QMenu(self.menubar)
        self.menuMusic.setObjectName("menuMusic")
        MainWindow.setMenuBar(self.menubar)
        self.action_send_animations = QtWidgets.QAction(MainWindow)
        self.action_send_animations.setObjectName("action_send_animations")
        self.action_send_configurations = QtWidgets.QAction(MainWindow)
        self.action_send_configurations.setObjectName("action_send_configurations")
        self.action_send_Aruco_map = QtWidgets.QAction(MainWindow)
        self.action_send_Aruco_map.setObjectName("action_send_Aruco_map")
        self.action_update_client_repo = QtWidgets.QAction(MainWindow)
        self.action_update_client_repo.setObjectName("action_update_client_repo")
        self.actionSend_launch_file_for_clever = QtWidgets.QAction(MainWindow)
        self.actionSend_launch_file_for_clever.setObjectName("actionSend_launch_file_for_clever")
        self.action_send_launch_file = QtWidgets.QAction(MainWindow)
        self.action_send_launch_file.setObjectName("action_send_launch_file")
        self.action_restart_clever = QtWidgets.QAction(MainWindow)
        self.action_restart_clever.setObjectName("action_restart_clever")
        self.action_restart_clever_show = QtWidgets.QAction(MainWindow)
        self.action_restart_clever_show.setObjectName("action_restart_clever_show")
        self.action_select_all_rows = QtWidgets.QAction(MainWindow)
        self.action_select_all_rows.setObjectName("action_select_all_rows")
        self.action_set_start_to_current_position = QtWidgets.QAction(MainWindow)
        self.action_set_start_to_current_position.setObjectName("action_set_start_to_current_position")
        self.action_reset_start = QtWidgets.QAction(MainWindow)
        self.action_reset_start.setObjectName("action_reset_start")
        self.action_set_z_offset_to_ground = QtWidgets.QAction(MainWindow)
        self.action_set_z_offset_to_ground.setObjectName("action_set_z_offset_to_ground")
        self.action_reset_z_offset = QtWidgets.QAction(MainWindow)
        self.action_reset_z_offset.setObjectName("action_reset_z_offset")
        self.action_select_music_file = QtWidgets.QAction(MainWindow)
        self.action_select_music_file.setObjectName("action_select_music_file")
        self.action_play_music = QtWidgets.QAction(MainWindow)
        self.action_play_music.setObjectName("action_play_music")
        self.action_test_music_after = QtWidgets.QAction(MainWindow)
        self.action_test_music_after.setObjectName("action_test_music_after")
        self.actionFill = QtWidgets.QAction(MainWindow)
        self.actionFill.setObjectName("actionFill")
        self.action_send_any_file = QtWidgets.QAction(MainWindow)
        self.action_send_any_file.setObjectName("action_send_any_file")
        self.actionSend_any_command = QtWidgets.QAction(MainWindow)
        self.actionSend_any_command.setObjectName("actionSend_any_command")
        self.action_stop_music = QtWidgets.QAction(MainWindow)
        self.action_stop_music.setObjectName("action_stop_music")
        self.action_remove_row = QtWidgets.QAction(MainWindow)
        self.action_remove_row.setObjectName("action_remove_row")
        self.action_send_calibrations = QtWidgets.QAction(MainWindow)
        self.action_send_calibrations.setObjectName("action_send_calibrations")
        self.action_reboot_all = QtWidgets.QAction(MainWindow)
        self.action_reboot_all.setObjectName("action_reboot_all")
        self.action_restart_chrony = QtWidgets.QAction(MainWindow)
        self.action_restart_chrony.setObjectName("action_restart_chrony")
        self.menuDeveloper_mode.addAction(self.action_send_any_file)
        self.menuDeveloper_mode.addAction(self.actionSend_any_command)
        self.menuOptions.addAction(self.action_send_animations)
        self.menuOptions.addAction(self.action_send_configurations)
        self.menuOptions.addAction(self.action_send_launch_file)
        self.menuOptions.addAction(self.action_send_Aruco_map)
        self.menuOptions.addAction(self.action_send_calibrations)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.menuDeveloper_mode.menuAction())
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.action_select_all_rows)
        self.menuAnimation.addAction(self.action_set_start_to_current_position)
        self.menuAnimation.addAction(self.action_reset_start)
        self.menuDeveloper_mode_2.addAction(self.action_restart_clever)
        self.menuDeveloper_mode_2.addAction(self.action_restart_clever_show)
        self.menuDeveloper_mode_2.addAction(self.action_update_client_repo)
        self.menuDeveloper_mode_2.addAction(self.action_reboot_all)
        self.menuDrone.addAction(self.action_set_z_offset_to_ground)
        self.menuDrone.addAction(self.action_reset_z_offset)
        self.menuDrone.addSeparator()
        self.menuDrone.addAction(self.action_restart_chrony)
        self.menuDrone.addAction(self.action_remove_row)
        self.menuDrone.addSeparator()
        self.menuDrone.addAction(self.menuDeveloper_mode_2.menuAction())
        self.menuMusic.addAction(self.action_select_music_file)
        self.menuMusic.addAction(self.action_play_music)
        self.menuMusic.addAction(self.action_stop_music)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuDrone.menuAction())
        self.menubar.addAction(self.menuAnimation.menuAction())
        self.menubar.addAction(self.menuMusic.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.start_delay_spin, self.tableView)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clever Drone Show"))
        self.music_text.setText(_translate("MainWindow", "  Music after"))
        self.music_delay_spin.setSuffix(_translate("MainWindow", " s"))
        self.music_play_text.setText(_translate("MainWindow", "  Play music"))
        self.start_delay_spin.setSuffix(_translate("MainWindow", " s"))
        self.start_text.setText(_translate("MainWindow", "  Start after"))
        self.stop_button.setText(_translate("MainWindow", "Stop and land all"))
        self.pause_button.setText(_translate("MainWindow", "Pause"))
        self.start_button.setText(_translate("MainWindow", "Start animation"))
        self.check_button.setText(_translate("MainWindow", "Preflight check"))
        self.disarm_all_button.setText(_translate("MainWindow", "Disarm ALL"))
        self.disarm_button.setText(_translate("MainWindow", "Disarm selected"))
        self.emergency_button.setText(_translate("MainWindow", "Emergency land"))
        self.land_button.setText(_translate("MainWindow", "Land"))
        self.flip_button.setText(_translate("MainWindow", "Flip"))
        self.takeoff_button.setText(_translate("MainWindow", "Takeoff"))
        self.leds_button.setText(_translate("MainWindow", "Test leds"))
        self.z_checkbox.setText(_translate("MainWindow", "  Z     ="))
        self.z_spin.setSuffix(_translate("MainWindow", " m"))
        self.reboot_fcu.setText(_translate("MainWindow", "Reboot FCU"))
        self.calibrate_gyro.setText(_translate("MainWindow", "Calibrate gyro"))
        self.calibrate_level.setText(_translate("MainWindow", "Calibrate level"))
        self.menuOptions.setTitle(_translate("MainWindow", "Server"))
        self.menuDeveloper_mode.setTitle(_translate("MainWindow", "Developer mode"))
        self.menuAnimation.setTitle(_translate("MainWindow", "Animation"))
        self.menuDrone.setTitle(_translate("MainWindow", "Drone"))
        self.menuDeveloper_mode_2.setTitle(_translate("MainWindow", "Developer mode"))
        self.menuMusic.setTitle(_translate("MainWindow", "Music"))
        self.action_send_animations.setText(_translate("MainWindow", "Send animations"))
        self.action_send_configurations.setText(_translate("MainWindow", "Send configurations"))
        self.action_send_Aruco_map.setText(_translate("MainWindow", "Send aruco map"))
        self.action_update_client_repo.setText(_translate("MainWindow", "Update clever-show git"))
        self.actionSend_launch_file_for_clever.setText(_translate("MainWindow", "Send launch file for clever"))
        self.action_send_launch_file.setText(_translate("MainWindow", "Send launch files"))
        self.action_restart_clever.setText(_translate("MainWindow", "Restart clever service"))
        self.action_restart_clever_show.setText(_translate("MainWindow", "Restart clever-show service"))
        self.action_select_all_rows.setText(_translate("MainWindow", "Select all drones"))
        self.action_select_all_rows.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.action_set_start_to_current_position.setText(_translate("MainWindow", "Set start X Y to current position"))
        self.action_reset_start.setText(_translate("MainWindow", "Reset start position"))
        self.action_set_z_offset_to_ground.setText(_translate("MainWindow", "Set Z offset to ground"))
        self.action_reset_z_offset.setText(_translate("MainWindow", "Reset Z offset"))
        self.action_select_music_file.setText(_translate("MainWindow", "Select music file"))
        self.action_play_music.setText(_translate("MainWindow", "Play music"))
        self.action_test_music_after.setText(_translate("MainWindow", "Test music after"))
        self.actionFill.setText(_translate("MainWindow", "fill"))
        self.action_send_any_file.setText(_translate("MainWindow", "Send any file"))
        self.actionSend_any_command.setText(_translate("MainWindow", "Send any command"))
        self.action_stop_music.setText(_translate("MainWindow", "Stop music"))
        self.action_remove_row.setText(_translate("MainWindow", "Remove from table"))
        self.action_send_calibrations.setText(_translate("MainWindow", "Send camera calibrations"))
        self.action_reboot_all.setText(_translate("MainWindow", "Reboot all"))
        self.action_restart_chrony.setText(_translate("MainWindow", "Restart chrony"))
