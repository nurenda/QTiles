# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtilesdialogbase.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 703)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(480, 680))
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setEnabled(True)
        self.groupBox_4.setGeometry(QtCore.QRect(9, 314, 462, 341))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QtCore.QSize(0, 325))
        self.groupBox_4.setBaseSize(QtCore.QSize(0, 330))
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.chkTMSConvention = QtWidgets.QCheckBox(self.groupBox_4)
        self.chkTMSConvention.setGeometry(QtCore.QRect(10, 220, 371, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkTMSConvention.sizePolicy().hasHeightForWidth())
        self.chkTMSConvention.setSizePolicy(sizePolicy)
        self.chkTMSConvention.setObjectName("chkTMSConvention")
        self.chkWriteMapurl = QtWidgets.QCheckBox(self.groupBox_4)
        self.chkWriteMapurl.setGeometry(QtCore.QRect(220, 280, 221, 17))
        self.chkWriteMapurl.setObjectName("chkWriteMapurl")
        self.chkMsgDialogs = QtWidgets.QCheckBox(self.groupBox_4)
        self.chkMsgDialogs.setGeometry(QtCore.QRect(10, 320, 441, 17))
        self.chkMsgDialogs.setChecked(True)
        self.chkMsgDialogs.setObjectName("chkMsgDialogs")
        self.chkMBTilesCompression = QtWidgets.QCheckBox(self.groupBox_4)
        self.chkMBTilesCompression.setGeometry(QtCore.QRect(10, 260, 201, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkMBTilesCompression.sizePolicy().hasHeightForWidth())
        self.chkMBTilesCompression.setSizePolicy(sizePolicy)
        self.chkMBTilesCompression.setObjectName("chkMBTilesCompression")
        self.chkWriteOverview = QtWidgets.QCheckBox(self.groupBox_4)
        self.chkWriteOverview.setGeometry(QtCore.QRect(220, 260, 221, 17))
        self.chkWriteOverview.setObjectName("chkWriteOverview")
        self.chkWriteJson = QtWidgets.QCheckBox(self.groupBox_4)
        self.chkWriteJson.setGeometry(QtCore.QRect(220, 240, 221, 17))
        self.chkWriteJson.setObjectName("chkWriteJson")
        self.chkWriteViewer = QtWidgets.QCheckBox(self.groupBox_4)
        self.chkWriteViewer.setGeometry(QtCore.QRect(220, 300, 221, 17))
        self.chkWriteViewer.setObjectName("chkWriteViewer")
        self.chkAntialiasing = QtWidgets.QCheckBox(self.groupBox_4)
        self.chkAntialiasing.setEnabled(True)
        self.chkAntialiasing.setGeometry(QtCore.QRect(10, 200, 421, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkAntialiasing.sizePolicy().hasHeightForWidth())
        self.chkAntialiasing.setSizePolicy(sizePolicy)
        self.chkAntialiasing.setChecked(True)
        self.chkAntialiasing.setObjectName("chkAntialiasing")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 421, 166))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_5.setContentsMargins(0, 8, 0, 0)
        self.gridLayout_5.setVerticalSpacing(4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.cmbFormat = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbFormat.sizePolicy().hasHeightForWidth())
        self.cmbFormat.setSizePolicy(sizePolicy)
        self.cmbFormat.setMinimumSize(QtCore.QSize(60, 0))
        self.cmbFormat.setObjectName("cmbFormat")
        self.cmbFormat.addItem("")
        self.cmbFormat.addItem("")
        self.gridLayout_5.addWidget(self.cmbFormat, 1, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 2, 0, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setStyleSheet("margin-left:2")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_10.addWidget(self.label_15)
        self.chkLockRatio = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkLockRatio.sizePolicy().hasHeightForWidth())
        self.chkLockRatio.setSizePolicy(sizePolicy)
        self.chkLockRatio.setObjectName("chkLockRatio")
        self.verticalLayout_10.addWidget(self.chkLockRatio)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setStyleSheet("margin-left:2")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_10.addWidget(self.label_16)
        self.gridLayout_5.addLayout(self.verticalLayout_10, 0, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setObjectName("label_17")
        self.gridLayout_5.addWidget(self.label_17, 3, 0, 1, 1)
        self.spnTransparency = QtWidgets.QSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spnTransparency.sizePolicy().hasHeightForWidth())
        self.spnTransparency.setSizePolicy(sizePolicy)
        self.spnTransparency.setMinimumSize(QtCore.QSize(60, 0))
        self.spnTransparency.setMaximum(255)
        self.spnTransparency.setProperty("value", 255)
        self.spnTransparency.setObjectName("spnTransparency")
        self.gridLayout_5.addWidget(self.spnTransparency, 2, 1, 1, 1)
        self.spnQuality = QtWidgets.QSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spnQuality.sizePolicy().hasHeightForWidth())
        self.spnQuality.setSizePolicy(sizePolicy)
        self.spnQuality.setMinimumSize(QtCore.QSize(60, 0))
        self.spnQuality.setMaximum(100)
        self.spnQuality.setObjectName("spnQuality")
        self.gridLayout_5.addWidget(self.spnQuality, 3, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setObjectName("label_18")
        self.gridLayout_5.addWidget(self.label_18, 3, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setObjectName("label_19")
        self.gridLayout_5.addWidget(self.label_19, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem, 0, 3, 1, 1)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_11.setContentsMargins(-1, 5, -1, 5)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.spnTileWidth = QtWidgets.QSpinBox(self.layoutWidget)
        self.spnTileWidth.setMinimumSize(QtCore.QSize(60, 20))
        self.spnTileWidth.setMinimum(128)
        self.spnTileWidth.setMaximum(2048)
        self.spnTileWidth.setProperty("value", 256)
        self.spnTileWidth.setObjectName("spnTileWidth")
        self.verticalLayout_11.addWidget(self.spnTileWidth)
        self.spnTileHeight = QtWidgets.QSpinBox(self.layoutWidget)
        self.spnTileHeight.setEnabled(True)
        self.spnTileHeight.setMinimumSize(QtCore.QSize(60, 20))
        self.spnTileHeight.setMinimum(128)
        self.spnTileHeight.setMaximum(2048)
        self.spnTileHeight.setProperty("value", 256)
        self.spnTileHeight.setObjectName("spnTileHeight")
        self.verticalLayout_11.addWidget(self.spnTileHeight)
        self.gridLayout_5.addLayout(self.verticalLayout_11, 0, 1, 1, 1)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_12.setSpacing(4)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_20 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_12.addWidget(self.label_20)
        self.lblHeight = QtWidgets.QLabel(self.layoutWidget)
        self.lblHeight.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblHeight.sizePolicy().hasHeightForWidth())
        self.lblHeight.setSizePolicy(sizePolicy)
        self.lblHeight.setObjectName("lblHeight")
        self.verticalLayout_12.addWidget(self.lblHeight)
        self.gridLayout_5.addLayout(self.verticalLayout_12, 0, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget)
        self.label_21.setObjectName("label_21")
        self.gridLayout_5.addWidget(self.label_21, 2, 2, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget)
        self.label_22.setObjectName("label_22")
        self.gridLayout_5.addWidget(self.label_22, 4, 0, 1, 1)
        self.spnMacroTile = QtWidgets.QSpinBox(self.layoutWidget)
        self.spnMacroTile.setMinimum(1)
        self.spnMacroTile.setMaximum(20)
        self.spnMacroTile.setObjectName("spnMacroTile")
        self.gridLayout_5.addWidget(self.spnMacroTile, 4, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_23 = QtWidgets.QLabel(self.layoutWidget)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_3.addWidget(self.label_23)
        self.lInfoIconMacroTile = QtWidgets.QLabel(self.layoutWidget)
        self.lInfoIconMacroTile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lInfoIconMacroTile.setOpenExternalLinks(False)
        self.lInfoIconMacroTile.setObjectName("lInfoIconMacroTile")
        self.horizontalLayout_3.addWidget(self.lInfoIconMacroTile)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 4, 2, 1, 1)
        self.chkSkipBlankTiles = QtWidgets.QCheckBox(self.groupBox_4)
        self.chkSkipBlankTiles.setGeometry(QtCore.QRect(10, 240, 201, 17))
        self.chkSkipBlankTiles.setChecked(True)
        self.chkSkipBlankTiles.setObjectName("chkSkipBlankTiles")
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 461, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("margin-left:24")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.leRootDir = QtWidgets.QLineEdit(self.layoutWidget1)
        self.leRootDir.setObjectName("leRootDir")
        self.horizontalLayout.addWidget(self.leRootDir)
        self.layoutWidget2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 660, 461, 31))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget2)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_5.addWidget(self.progressBar)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_5.addWidget(self.buttonBox)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 236, 461, 68))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setContentsMargins(0, 4, 0, 4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(24, 0, 5, 0)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.spnZoomMin = QtWidgets.QSpinBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spnZoomMin.sizePolicy().hasHeightForWidth())
        self.spnZoomMin.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spnZoomMin.setFont(font)
        self.spnZoomMin.setMaximum(40)
        self.spnZoomMin.setObjectName("spnZoomMin")
        self.gridLayout_3.addWidget(self.spnZoomMin, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.spnZoomMax = QtWidgets.QSpinBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spnZoomMax.sizePolicy().hasHeightForWidth())
        self.spnZoomMax.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.spnZoomMax.setFont(font)
        self.spnZoomMax.setMinimum(0)
        self.spnZoomMax.setMaximum(40)
        self.spnZoomMax.setProperty("value", 18)
        self.spnZoomMax.setObjectName("spnZoomMax")
        self.gridLayout_3.addWidget(self.spnZoomMax, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 2, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_3)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 137, 461, 93))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setContentsMargins(0, 4, 0, 4)
        self.verticalLayout_7.setSpacing(3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(6, -1, -1, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.rbExtentCanvas = QtWidgets.QRadioButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbExtentCanvas.sizePolicy().hasHeightForWidth())
        self.rbExtentCanvas.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rbExtentCanvas.setFont(font)
        self.rbExtentCanvas.setObjectName("rbExtentCanvas")
        self.verticalLayout_9.addWidget(self.rbExtentCanvas)
        self.rbExtentFull = QtWidgets.QRadioButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbExtentFull.sizePolicy().hasHeightForWidth())
        self.rbExtentFull.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rbExtentFull.setFont(font)
        self.rbExtentFull.setObjectName("rbExtentFull")
        self.verticalLayout_9.addWidget(self.rbExtentFull)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.rbExtentLayer = QtWidgets.QRadioButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbExtentLayer.sizePolicy().hasHeightForWidth())
        self.rbExtentLayer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rbExtentLayer.setFont(font)
        self.rbExtentLayer.setObjectName("rbExtentLayer")
        self.horizontalLayout_4.addWidget(self.rbExtentLayer)
        self.cmbLayers = QtWidgets.QComboBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbLayers.sizePolicy().hasHeightForWidth())
        self.cmbLayers.setSizePolicy(sizePolicy)
        self.cmbLayers.setObjectName("cmbLayers")
        self.horizontalLayout_4.addWidget(self.cmbLayers)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)
        self.verticalLayout_7.addLayout(self.verticalLayout_9)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 38, 461, 93))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setContentsMargins(0, 4, 0, 4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(6, -1, -1, -1)
        self.gridLayout_4.setVerticalSpacing(3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.leTilesFroNGM = QtWidgets.QLineEdit(self.groupBox)
        self.leTilesFroNGM.setToolTip("")
        self.leTilesFroNGM.setPlaceholderText("")
        self.leTilesFroNGM.setObjectName("leTilesFroNGM")
        self.gridLayout_4.addWidget(self.leTilesFroNGM, 2, 2, 1, 1)
        self.lInfoIconOutputNGM = QtWidgets.QLabel(self.groupBox)
        self.lInfoIconOutputNGM.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lInfoIconOutputNGM.setOpenExternalLinks(False)
        self.lInfoIconOutputNGM.setObjectName("lInfoIconOutputNGM")
        self.gridLayout_4.addWidget(self.lInfoIconOutputNGM, 2, 1, 1, 1)
        self.rbOutputDir = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbOutputDir.sizePolicy().hasHeightForWidth())
        self.rbOutputDir.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rbOutputDir.setFont(font)
        self.rbOutputDir.setObjectName("rbOutputDir")
        self.gridLayout_4.addWidget(self.rbOutputDir, 1, 0, 1, 1)
        self.lInfoIconOutputZip = QtWidgets.QLabel(self.groupBox)
        self.lInfoIconOutputZip.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lInfoIconOutputZip.sizePolicy().hasHeightForWidth())
        self.lInfoIconOutputZip.setSizePolicy(sizePolicy)
        self.lInfoIconOutputZip.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lInfoIconOutputZip.setText("<a href=\"infoOutpuZip\"><img src=\":/icons/info.png\"/></a>")
        self.lInfoIconOutputZip.setTextFormat(QtCore.Qt.RichText)
        self.lInfoIconOutputZip.setOpenExternalLinks(False)
        self.lInfoIconOutputZip.setObjectName("lInfoIconOutputZip")
        self.gridLayout_4.addWidget(self.lInfoIconOutputZip, 0, 1, 1, 1)
        self.rbOutputNGM = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbOutputNGM.sizePolicy().hasHeightForWidth())
        self.rbOutputNGM.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rbOutputNGM.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/ngm_index_24x24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rbOutputNGM.setIcon(icon)
        self.rbOutputNGM.setObjectName("rbOutputNGM")
        self.gridLayout_4.addWidget(self.rbOutputNGM, 2, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.leDirectoryName = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leDirectoryName.sizePolicy().hasHeightForWidth())
        self.leDirectoryName.setSizePolicy(sizePolicy)
        self.leDirectoryName.setObjectName("leDirectoryName")
        self.horizontalLayout_7.addWidget(self.leDirectoryName)
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 1, 2, 1, 1)
        self.rbOutputZip = QtWidgets.QRadioButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rbOutputZip.sizePolicy().hasHeightForWidth())
        self.rbOutputZip.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.rbOutputZip.setFont(font)
        self.rbOutputZip.setStyleSheet("")
        self.rbOutputZip.setObjectName("rbOutputZip")
        self.gridLayout_4.addWidget(self.rbOutputZip, 0, 0, 1, 1)
        self.lInfoIconOutputDir = QtWidgets.QLabel(self.groupBox)
        self.lInfoIconOutputDir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lInfoIconOutputDir.setOpenExternalLinks(False)
        self.lInfoIconOutputDir.setObjectName("lInfoIconOutputDir")
        self.gridLayout_4.addWidget(self.lInfoIconOutputDir, 1, 1, 1, 1)
        self.leZipFileName = QtWidgets.QLineEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leZipFileName.sizePolicy().hasHeightForWidth())
        self.leZipFileName.setSizePolicy(sizePolicy)
        self.leZipFileName.setObjectName("leZipFileName")
        self.gridLayout_4.addWidget(self.leZipFileName, 0, 2, 1, 1)
        self.btnBrowse = QtWidgets.QToolButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBrowse.sizePolicy().hasHeightForWidth())
        self.btnBrowse.setSizePolicy(sizePolicy)
        self.btnBrowse.setObjectName("btnBrowse")
        self.gridLayout_4.addWidget(self.btnBrowse, 1, 3, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.groupBox)
        self.label_41.setStyleSheet("margin-left:2")
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.gridLayout_4.addWidget(self.label_41, 0, 3, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.groupBox)
        self.label_42.setStyleSheet("margin-left:2")
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.gridLayout_4.addWidget(self.label_42, 2, 3, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout_4)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "QTiles"))
        self.groupBox_4.setTitle(_translate("Dialog", "Parameters"))
        self.chkTMSConvention.setText(_translate("Dialog", "Use TMS tiles convention (Slippy Map / XYZTiles by default)"))
        self.chkWriteMapurl.setText(_translate("Dialog", "Write .mapurl file"))
        self.chkMsgDialogs.setText(_translate("Dialog", "MessageBox on process end or abort"))
        self.chkMBTilesCompression.setText(_translate("Dialog", "Use MBTiles compression"))
        self.chkWriteOverview.setText(_translate("Dialog", "Write overview image file"))
        self.chkWriteJson.setText(_translate("Dialog", "Write .json metadata"))
        self.chkWriteViewer.setText(_translate("Dialog", "Write Leaflet-based viewer"))
        self.chkAntialiasing.setText(_translate("Dialog", "Make lines appear less jagged at the expense of some drawing performance"))
        self.cmbFormat.setItemText(0, _translate("Dialog", "PNG"))
        self.cmbFormat.setItemText(1, _translate("Dialog", "JPG"))
        self.label_14.setText(_translate("Dialog", "Background opacity"))
        self.label_15.setText(_translate("Dialog", "╮"))
        self.chkLockRatio.setToolTip(_translate("Dialog", "Lock 1:1 ratio"))
        self.label_16.setText(_translate("Dialog", "╯"))
        self.label_17.setText(_translate("Dialog", "Quality"))
        self.label_18.setText(_translate("Dialog", "(0-100)"))
        self.label_19.setText(_translate("Dialog", "Format"))
        self.label_20.setText(_translate("Dialog", "Tile width"))
        self.lblHeight.setText(_translate("Dialog", "Tile height"))
        self.label_21.setText(_translate("Dialog", "(0: Transparent\n"
"255: Opaque)"))
        self.label_22.setText(_translate("Dialog", "Render sets of up to"))
        self.label_23.setText(_translate("Dialog", "tiles at once"))
        self.lInfoIconMacroTile.setText(_translate("Dialog", "<a href=\"infoOutpuZip\"><img src=\":/icons/info.png\"/></a>"))
        self.chkSkipBlankTiles.setText(_translate("Dialog", "Skip blank tiles"))
        self.label_4.setText(_translate("Dialog", "Tileset name"))
        self.groupBox_3.setTitle(_translate("Dialog", "Zoom"))
        self.label_2.setText(_translate("Dialog", "Maximum zoom"))
        self.label.setText(_translate("Dialog", "Minimum zoom"))
        self.groupBox_2.setTitle(_translate("Dialog", "Extent"))
        self.rbExtentCanvas.setText(_translate("Dialog", "Canvas extent"))
        self.rbExtentFull.setText(_translate("Dialog", "Full extent"))
        self.rbExtentLayer.setText(_translate("Dialog", "Layer extent"))
        self.groupBox.setTitle(_translate("Dialog", "Output"))
        self.lInfoIconOutputNGM.setText(_translate("Dialog", "<a href=\"infoOutpuZip\"><img src=\":/icons/info.png\"/></a>"))
        self.rbOutputDir.setText(_translate("Dialog", "Directory"))
        self.rbOutputNGM.setText(_translate("Dialog", "NGM"))
        self.rbOutputZip.setText(_translate("Dialog", "File"))
        self.lInfoIconOutputDir.setText(_translate("Dialog", "<a href=\"infoOutpuZip\"><img src=\":/icons/info.png\"/></a>"))
        self.btnBrowse.setText(_translate("Dialog", "..."))
        self.label_41.setText(_translate("Dialog", "╮"))
        self.label_42.setText(_translate("Dialog", "╯"))


