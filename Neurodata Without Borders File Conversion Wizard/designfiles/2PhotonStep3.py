# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2PhotonStep3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1500, 1000)
        self.step2_gb = QtWidgets.QGroupBox(Dialog)
        self.step2_gb.setGeometry(QtCore.QRect(10, 240, 341, 321))
        self.step2_gb.setObjectName("step2_gb")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.step2_gb)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 331, 291))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.step2_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.step2_grid.setContentsMargins(0, 0, 0, 0)
        self.step2_grid.setObjectName("step2_grid")
        self.image_stacks_cb_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.image_stacks_cb_lbl.setObjectName("image_stacks_cb_lbl")
        self.step2_grid.addWidget(self.image_stacks_cb_lbl, 2, 0, 1, 1)
        self.image_stacks_cb = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.image_stacks_cb.setObjectName("image_stacks_cb")
        self.step2_grid.addWidget(self.image_stacks_cb, 2, 1, 1, 1)
        self.name2_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.name2_le.setObjectName("name2_le")
        self.step2_grid.addWidget(self.name2_le, 0, 1, 1, 1)
        self.description2_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.description2_lbl.setObjectName("description2_lbl")
        self.step2_grid.addWidget(self.description2_lbl, 1, 0, 1, 1)
        self.name2_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.name2_lbl.setObjectName("name2_lbl")
        self.step2_grid.addWidget(self.name2_lbl, 0, 0, 1, 1)
        self.id_lbl = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.id_lbl.setObjectName("id_lbl")
        self.step2_grid.addWidget(self.id_lbl, 3, 0, 1, 1)
        self.id_le = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.id_le.setObjectName("id_le")
        self.step2_grid.addWidget(self.id_le, 3, 1, 1, 1)
        self.description2_pte = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_2)
        self.description2_pte.setMinimumSize(QtCore.QSize(0, 100))
        self.description2_pte.setMaximumSize(QtCore.QSize(16777215, 80))
        self.description2_pte.setObjectName("description2_pte")
        self.step2_grid.addWidget(self.description2_pte, 1, 1, 1, 1)
        self.step4_gb = QtWidgets.QGroupBox(Dialog)
        self.step4_gb.setGeometry(QtCore.QRect(360, 40, 481, 771))
        self.step4_gb.setObjectName("step4_gb")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.step4_gb)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(50, 30, 431, 731))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.roi_response_series_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.roi_response_series_grid.setContentsMargins(0, 0, 0, 0)
        self.roi_response_series_grid.setObjectName("roi_response_series_grid")
        self.comments_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.comments_lbl.setObjectName("comments_lbl")
        self.roi_response_series_grid.addWidget(self.comments_lbl, 7, 0, 1, 1)
        self.name3_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.name3_lbl.setObjectName("name3_lbl")
        self.roi_response_series_grid.addWidget(self.name3_lbl, 0, 0, 1, 1)
        self.name3_le = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.name3_le.setObjectName("name3_le")
        self.roi_response_series_grid.addWidget(self.name3_le, 0, 1, 1, 1)
        self.description3_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.description3_lbl.setObjectName("description3_lbl")
        self.roi_response_series_grid.addWidget(self.description3_lbl, 1, 0, 1, 1)
        self.rate_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.rate_lbl.setObjectName("rate_lbl")
        self.roi_response_series_grid.addWidget(self.rate_lbl, 6, 0, 1, 1)
        self.starting_time_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.starting_time_lbl.setObjectName("starting_time_lbl")
        self.roi_response_series_grid.addWidget(self.starting_time_lbl, 5, 0, 1, 1)
        self.resolution_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.resolution_lbl.setObjectName("resolution_lbl")
        self.roi_response_series_grid.addWidget(self.resolution_lbl, 3, 0, 1, 1)
        self.conversion_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.conversion_lbl.setObjectName("conversion_lbl")
        self.roi_response_series_grid.addWidget(self.conversion_lbl, 4, 0, 1, 1)
        self.unit_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.unit_lbl.setObjectName("unit_lbl")
        self.roi_response_series_grid.addWidget(self.unit_lbl, 2, 0, 1, 1)
        self.control_description_le = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.control_description_le.setObjectName("control_description_le")
        self.roi_response_series_grid.addWidget(self.control_description_le, 9, 1, 1, 1)
        self.rate_le = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.rate_le.setObjectName("rate_le")
        self.roi_response_series_grid.addWidget(self.rate_le, 6, 1, 1, 1)
        self.unit_le = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.unit_le.setObjectName("unit_le")
        self.roi_response_series_grid.addWidget(self.unit_le, 2, 1, 1, 1)
        self.starting_time_le = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.starting_time_le.setObjectName("starting_time_le")
        self.roi_response_series_grid.addWidget(self.starting_time_le, 5, 1, 1, 1)
        self.conversion_le = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.conversion_le.setObjectName("conversion_le")
        self.roi_response_series_grid.addWidget(self.conversion_le, 4, 1, 1, 1)
        self.resolution_le = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.resolution_le.setObjectName("resolution_le")
        self.roi_response_series_grid.addWidget(self.resolution_le, 3, 1, 1, 1)
        self.control_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.control_lbl.setObjectName("control_lbl")
        self.roi_response_series_grid.addWidget(self.control_lbl, 8, 0, 1, 1)
        self.control_le = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.control_le.setObjectName("control_le")
        self.roi_response_series_grid.addWidget(self.control_le, 8, 1, 1, 1)
        self.control_description_lbl = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.control_description_lbl.setObjectName("control_description_lbl")
        self.roi_response_series_grid.addWidget(self.control_description_lbl, 9, 0, 1, 1)
        self.description3_pte = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_5)
        self.description3_pte.setMinimumSize(QtCore.QSize(0, 100))
        self.description3_pte.setMaximumSize(QtCore.QSize(16777215, 80))
        self.description3_pte.setObjectName("description3_pte")
        self.roi_response_series_grid.addWidget(self.description3_pte, 1, 1, 1, 1)
        self.comments_pte = QtWidgets.QPlainTextEdit(self.gridLayoutWidget_5)
        self.comments_pte.setMinimumSize(QtCore.QSize(0, 100))
        self.comments_pte.setMaximumSize(QtCore.QSize(16777215, 80))
        self.comments_pte.setObjectName("comments_pte")
        self.roi_response_series_grid.addWidget(self.comments_pte, 7, 1, 1, 1)
        self.add_roi_gb = QtWidgets.QGroupBox(Dialog)
        self.add_roi_gb.setGeometry(QtCore.QRect(0, 20, 851, 900))
        self.add_roi_gb.setMinimumSize(QtCore.QSize(0, 900))
        self.add_roi_gb.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.add_roi_gb.setObjectName("add_roi_gb")
        self.update_btn = QtWidgets.QPushButton(self.add_roi_gb)
        self.update_btn.setGeometry(QtCore.QRect(690, 800, 150, 30))
        self.update_btn.setMinimumSize(QtCore.QSize(150, 30))
        self.update_btn.setObjectName("update_btn")
        self.step3_gb = QtWidgets.QGroupBox(self.add_roi_gb)
        self.step3_gb.setGeometry(QtCore.QRect(10, 560, 341, 231))
        self.step3_gb.setObjectName("step3_gb")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.step3_gb)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(10, 30, 331, 141))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.roi_type_grid = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.roi_type_grid.setContentsMargins(0, 0, 0, 0)
        self.roi_type_grid.setObjectName("roi_type_grid")
        self.mask_upload_tool = QtWidgets.QToolButton(self.gridLayoutWidget_6)
        self.mask_upload_tool.setMinimumSize(QtCore.QSize(100, 0))
        self.mask_upload_tool.setObjectName("mask_upload_tool")
        self.roi_type_grid.addWidget(self.mask_upload_tool, 0, 1, 1, 1)
        self.mask_upload_lbl = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.mask_upload_lbl.setObjectName("mask_upload_lbl")
        self.roi_type_grid.addWidget(self.mask_upload_lbl, 0, 0, 1, 1)
        self.mask_selector_lbl = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.mask_selector_lbl.setObjectName("mask_selector_lbl")
        self.roi_type_grid.addWidget(self.mask_selector_lbl, 1, 0, 1, 1)
        self.mask_selector_cb = QtWidgets.QComboBox(self.gridLayoutWidget_6)
        self.mask_selector_cb.setMinimumSize(QtCore.QSize(100, 24))
        self.mask_selector_cb.setObjectName("mask_selector_cb")
        self.mask_selector_cb.addItem("")
        self.mask_selector_cb.addItem("")
        self.mask_selector_cb.addItem("")
        self.roi_type_grid.addWidget(self.mask_selector_cb, 1, 1, 1, 1)
        self.dff_upload_tool = QtWidgets.QToolButton(self.gridLayoutWidget_6)
        self.dff_upload_tool.setMinimumSize(QtCore.QSize(100, 0))
        self.dff_upload_tool.setObjectName("dff_upload_tool")
        self.roi_type_grid.addWidget(self.dff_upload_tool, 2, 1, 1, 1)
        self.dff_label = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.dff_label.setObjectName("dff_label")
        self.roi_type_grid.addWidget(self.dff_label, 2, 0, 1, 1)
        self.step1_gb = QtWidgets.QGroupBox(self.add_roi_gb)
        self.step1_gb.setGeometry(QtCore.QRect(10, 30, 341, 181))
        self.step1_gb.setObjectName("step1_gb")
        self.gridLayoutWidget = QtWidgets.QWidget(self.step1_gb)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 331, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.step1_grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.step1_grid.setContentsMargins(0, 0, 0, 0)
        self.step1_grid.setObjectName("step1_grid")
        self.name1_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.name1_lbl.setObjectName("name1_lbl")
        self.step1_grid.addWidget(self.name1_lbl, 0, 0, 1, 1)
        self.description1_lbl = QtWidgets.QLabel(self.gridLayoutWidget)
        self.description1_lbl.setObjectName("description1_lbl")
        self.step1_grid.addWidget(self.description1_lbl, 1, 0, 1, 1)
        self.description1_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.description1_le.setObjectName("description1_le")
        self.step1_grid.addWidget(self.description1_le, 1, 1, 1, 1)
        self.name1_le = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name1_le.setObjectName("name1_le")
        self.step1_grid.addWidget(self.name1_le, 0, 1, 1, 1)
        self.create_btn = QtWidgets.QPushButton(self.step1_gb)
        self.create_btn.setGeometry(QtCore.QRect(210, 150, 75, 23))
        self.create_btn.setObjectName("create_btn")
        self.file_contents_gb = QtWidgets.QGroupBox(Dialog)
        self.file_contents_gb.setGeometry(QtCore.QRect(890, 30, 511, 1000))
        self.file_contents_gb.setMinimumSize(QtCore.QSize(0, 900))
        self.file_contents_gb.setObjectName("file_contents_gb")
        self.roi_table = QtWidgets.QTableWidget(self.file_contents_gb)
        self.roi_table.setGeometry(QtCore.QRect(20, 60, 450, 202))
        self.roi_table.setMinimumSize(QtCore.QSize(450, 200))
        self.roi_table.setMaximumSize(QtCore.QSize(16777211, 16777215))
        self.roi_table.setRowCount(5)
        self.roi_table.setColumnCount(3)
        self.roi_table.setObjectName("roi_table")
        item = QtWidgets.QTableWidgetItem()
        self.roi_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.roi_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.roi_table.setHorizontalHeaderItem(2, item)
        self.save_btn = QtWidgets.QPushButton(self.file_contents_gb)
        self.save_btn.setGeometry(QtCore.QRect(350, 790, 150, 30))
        self.save_btn.setMinimumSize(QtCore.QSize(150, 30))
        self.save_btn.setObjectName("save_btn")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(870, 30, 20, 811))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.add_roi_gb.raise_()
        self.step2_gb.raise_()
        self.step4_gb.raise_()
        self.file_contents_gb.raise_()
        self.line.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.step2_gb.setTitle(_translate("Dialog", "Step 2: Image and Plane Segmentation"))
        self.image_stacks_cb_lbl.setText(_translate("Dialog", "Image Stacks your \n"
"ROI applies to:"))
        self.description2_lbl.setText(_translate("Dialog", "Description"))
        self.name2_lbl.setText(_translate("Dialog", "Name"))
        self.id_lbl.setText(_translate("Dialog", "ID (Table Identifiers)"))
        self.step4_gb.setTitle(_translate("Dialog", "Step 4: ROI Response Series"))
        self.comments_lbl.setText(_translate("Dialog", "Comments"))
        self.name3_lbl.setText(_translate("Dialog", "Name"))
        self.description3_lbl.setText(_translate("Dialog", "Description"))
        self.rate_lbl.setText(_translate("Dialog", "Rate"))
        self.starting_time_lbl.setText(_translate("Dialog", "Starting Time"))
        self.resolution_lbl.setText(_translate("Dialog", "Resolution"))
        self.conversion_lbl.setText(_translate("Dialog", "Conversion"))
        self.unit_lbl.setText(_translate("Dialog", "Unit"))
        self.control_lbl.setText(_translate("Dialog", "Control"))
        self.control_description_lbl.setText(_translate("Dialog", "Control Desciption"))
        self.add_roi_gb.setTitle(_translate("Dialog", "Add ROIs"))
        self.update_btn.setText(_translate("Dialog", "Update/Verify"))
        self.step3_gb.setTitle(_translate("Dialog", "Step 3: Upload Mask and dF/F"))
        self.mask_upload_tool.setText(_translate("Dialog", "..."))
        self.mask_upload_lbl.setText(_translate("Dialog", "Upload  ROI Pixel, Voxel, Image Mask"))
        self.mask_selector_lbl.setText(_translate("Dialog", "Select Mask Type:"))
        self.mask_selector_cb.setItemText(0, _translate("Dialog", "Image Mask"))
        self.mask_selector_cb.setItemText(1, _translate("Dialog", "Voxel Mask"))
        self.mask_selector_cb.setItemText(2, _translate("Dialog", "Pixel Mask"))
        self.dff_upload_tool.setText(_translate("Dialog", "..."))
        self.dff_label.setText(_translate("Dialog", "Upload dF/F Trace:"))
        self.step1_gb.setTitle(_translate("Dialog", "Step 1: Create Processing Module"))
        self.name1_lbl.setText(_translate("Dialog", "Name"))
        self.description1_lbl.setText(_translate("Dialog", "Description"))
        self.create_btn.setText(_translate("Dialog", "Create"))
        self.file_contents_gb.setTitle(_translate("Dialog", "File Contents"))
        item = self.roi_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID (region)"))
        item = self.roi_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Name"))
        item = self.roi_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Description"))
        self.save_btn.setText(_translate("Dialog", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
