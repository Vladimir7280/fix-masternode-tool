# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/blogin/PycharmProjects/FIXMT-git/src/ui/ui_doc_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DocDlg(object):
    def setupUi(self, DocDlg):
        DocDlg.setObjectName("DocDlg")
        DocDlg.resize(714, 454)
        self.verticalLayout = QtWidgets.QVBoxLayout(DocDlg)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textMain = QtWidgets.QTextBrowser(DocDlg)
        self.textMain.setStyleSheet("")
        self.textMain.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textMain.setOpenExternalLinks(True)
        self.textMain.setObjectName("textMain")
        self.verticalLayout.addWidget(self.textMain)
        self.buttonBox = QtWidgets.QDialogButtonBox(DocDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DocDlg)
        self.buttonBox.accepted.connect(DocDlg.accept)
        self.buttonBox.rejected.connect(DocDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(DocDlg)

    def retranslateUi(self, DocDlg):
        _translate = QtCore.QCoreApplication.translate
        DocDlg.setWindowTitle(_translate("DocDlg", "Dialog"))
        self.textMain.setHtml(_translate("DocDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DocDlg = QtWidgets.QDialog()
    ui = Ui_DocDlg()
    ui.setupUi(DocDlg)
    DocDlg.show()
    sys.exit(app.exec_())

