# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/blogin/Projects/fix-masternode-tool/src/ui/ui_upd_mn_registrar_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UpdMnRegistrarDlg(object):
    def setupUi(self, UpdMnRegistrarDlg):
        UpdMnRegistrarDlg.setObjectName("UpdMnRegistrarDlg")
        UpdMnRegistrarDlg.resize(671, 348)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(UpdMnRegistrarDlg.sizePolicy().hasHeightForWidth())
        UpdMnRegistrarDlg.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(UpdMnRegistrarDlg)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblDescription = QtWidgets.QLabel(UpdMnRegistrarDlg)
        self.lblDescription.setWordWrap(True)
        self.lblDescription.setOpenExternalLinks(True)
        self.lblDescription.setObjectName("lblDescription")
        self.verticalLayout.addWidget(self.lblDescription)
        self.line_2 = QtWidgets.QFrame(UpdMnRegistrarDlg)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.stackedWidget = QtWidgets.QStackedWidget(UpdMnRegistrarDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page0 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page0.sizePolicy().hasHeightForWidth())
        self.page0.setSizePolicy(sizePolicy)
        self.page0.setObjectName("page0")
        self.gridLayout = QtWidgets.QGridLayout(self.page0)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        self.layOperatorKey = QtWidgets.QHBoxLayout()
        self.layOperatorKey.setSpacing(8)
        self.layOperatorKey.setObjectName("layOperatorKey")
        self.edtOperatorKey = QtWidgets.QLineEdit(self.page0)
        self.edtOperatorKey.setClearButtonEnabled(True)
        self.edtOperatorKey.setObjectName("edtOperatorKey")
        self.layOperatorKey.addWidget(self.edtOperatorKey)
        self.btnGenerateOperatorKey = QtWidgets.QToolButton(self.page0)
        self.btnGenerateOperatorKey.setObjectName("btnGenerateOperatorKey")
        self.layOperatorKey.addWidget(self.btnGenerateOperatorKey)
        self.gridLayout.addLayout(self.layOperatorKey, 2, 1, 1, 1)
        self.lblVotingKey = QtWidgets.QLabel(self.page0)
        self.lblVotingKey.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblVotingKey.setObjectName("lblVotingKey")
        self.gridLayout.addWidget(self.lblVotingKey, 3, 0, 1, 1)
        self.layPayoutAddress = QtWidgets.QHBoxLayout()
        self.layPayoutAddress.setSpacing(8)
        self.layPayoutAddress.setObjectName("layPayoutAddress")
        self.edtPayoutAddress = QtWidgets.QLineEdit(self.page0)
        self.edtPayoutAddress.setClearButtonEnabled(True)
        self.edtPayoutAddress.setObjectName("edtPayoutAddress")
        self.layPayoutAddress.addWidget(self.edtPayoutAddress)
        self.gridLayout.addLayout(self.layPayoutAddress, 1, 1, 1, 1)
        self.lblOperatorKey = QtWidgets.QLabel(self.page0)
        self.lblOperatorKey.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblOperatorKey.setObjectName("lblOperatorKey")
        self.gridLayout.addWidget(self.lblOperatorKey, 2, 0, 1, 1)
        self.lblPayoutAddress = QtWidgets.QLabel(self.page0)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblPayoutAddress.setFont(font)
        self.lblPayoutAddress.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblPayoutAddress.setObjectName("lblPayoutAddress")
        self.gridLayout.addWidget(self.lblPayoutAddress, 1, 0, 1, 1)
        self.layVotingKey = QtWidgets.QHBoxLayout()
        self.layVotingKey.setSpacing(8)
        self.layVotingKey.setObjectName("layVotingKey")
        self.edtVotingKey = QtWidgets.QLineEdit(self.page0)
        self.edtVotingKey.setClearButtonEnabled(True)
        self.edtVotingKey.setObjectName("edtVotingKey")
        self.layVotingKey.addWidget(self.edtVotingKey)
        self.btnGenerateVotingKey = QtWidgets.QToolButton(self.page0)
        self.btnGenerateVotingKey.setObjectName("btnGenerateVotingKey")
        self.layVotingKey.addWidget(self.btnGenerateVotingKey)
        self.gridLayout.addLayout(self.layVotingKey, 3, 1, 1, 1)
        self.stackedWidget.addWidget(self.page0)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.line = QtWidgets.QFrame(UpdMnRegistrarDlg)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.lblManualCommands = QtWidgets.QLabel(UpdMnRegistrarDlg)
        self.lblManualCommands.setText("")
        self.lblManualCommands.setObjectName("lblManualCommands")
        self.verticalLayout.addWidget(self.lblManualCommands)
        self.edtManualCommands = QtWidgets.QTextBrowser(UpdMnRegistrarDlg)
        self.edtManualCommands.setOpenExternalLinks(True)
        self.edtManualCommands.setOpenLinks(True)
        self.edtManualCommands.setObjectName("edtManualCommands")
        self.verticalLayout.addWidget(self.edtManualCommands)
        self.lblMessage = QtWidgets.QLabel(UpdMnRegistrarDlg)
        self.lblMessage.setText("")
        self.lblMessage.setWordWrap(True)
        self.lblMessage.setOpenExternalLinks(True)
        self.lblMessage.setObjectName("lblMessage")
        self.verticalLayout.addWidget(self.lblMessage)
        self.frame = QtWidgets.QFrame(UpdMnRegistrarDlg)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(12, 12, 12, 12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCancel = QtWidgets.QPushButton(self.frame)
        self.btnCancel.setAutoDefault(False)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        self.lblDocumentation = QtWidgets.QLabel(self.frame)
        self.lblDocumentation.setText("")
        self.lblDocumentation.setOpenExternalLinks(True)
        self.lblDocumentation.setObjectName("lblDocumentation")
        self.horizontalLayout.addWidget(self.lblDocumentation)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnSendUpdateTx = QtWidgets.QPushButton(self.frame)
        self.btnSendUpdateTx.setAutoDefault(False)
        self.btnSendUpdateTx.setObjectName("btnSendUpdateTx")
        self.horizontalLayout.addWidget(self.btnSendUpdateTx)
        self.btnClose = QtWidgets.QPushButton(self.frame)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout.addWidget(self.btnClose)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(UpdMnRegistrarDlg)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(UpdMnRegistrarDlg)
        UpdMnRegistrarDlg.setTabOrder(self.edtPayoutAddress, self.edtOperatorKey)
        UpdMnRegistrarDlg.setTabOrder(self.edtOperatorKey, self.btnGenerateOperatorKey)
        UpdMnRegistrarDlg.setTabOrder(self.btnGenerateOperatorKey, self.edtVotingKey)
        UpdMnRegistrarDlg.setTabOrder(self.edtVotingKey, self.btnGenerateVotingKey)
        UpdMnRegistrarDlg.setTabOrder(self.btnGenerateVotingKey, self.btnSendUpdateTx)
        UpdMnRegistrarDlg.setTabOrder(self.btnSendUpdateTx, self.btnCancel)

    def retranslateUi(self, UpdMnRegistrarDlg):
        _translate = QtCore.QCoreApplication.translate
        UpdMnRegistrarDlg.setWindowTitle(_translate("UpdMnRegistrarDlg", "Update masternode registrar"))
        self.lblDescription.setText(_translate("UpdMnRegistrarDlg", "The transaction type associated with this action (ProUpRegTx) is used to update information relating to the owner (<a href=\"https://docs.fix.org/en/stable/masternodes/maintenance.html#proupregtx\">details</a>)."))
        self.edtOperatorKey.setPlaceholderText(_translate("UpdMnRegistrarDlg", "<unchanged>"))
        self.btnGenerateOperatorKey.setText(_translate("UpdMnRegistrarDlg", "Generate new"))
        self.lblVotingKey.setText(_translate("UpdMnRegistrarDlg", "<b>Voting private key</b>"))
        self.edtPayoutAddress.setPlaceholderText(_translate("UpdMnRegistrarDlg", "<unchanged>"))
        self.lblOperatorKey.setText(_translate("UpdMnRegistrarDlg", "<b>Operator private key</b> "))
        self.lblPayoutAddress.setText(_translate("UpdMnRegistrarDlg", "Payout address"))
        self.edtVotingKey.setPlaceholderText(_translate("UpdMnRegistrarDlg", "<unchanged>"))
        self.btnGenerateVotingKey.setText(_translate("UpdMnRegistrarDlg", "Generate new"))
        self.btnCancel.setText(_translate("UpdMnRegistrarDlg", "Cancel"))
        self.btnSendUpdateTx.setText(_translate("UpdMnRegistrarDlg", "Send Update Transaction"))
        self.btnClose.setText(_translate("UpdMnRegistrarDlg", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UpdMnRegistrarDlg = QtWidgets.QDialog()
    ui = Ui_UpdMnRegistrarDlg()
    ui.setupUi(UpdMnRegistrarDlg)
    UpdMnRegistrarDlg.show()
    sys.exit(app.exec_())

