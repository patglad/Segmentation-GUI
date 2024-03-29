# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yolact.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os

from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon, QIntValidator
from PyQt5.QtWidgets import QPushButton, QLabel, QRadioButton, QMenuBar, QMenu, QCheckBox, QWidget, QFileDialog, \
    QMainWindow, QMessageBox, QLineEdit

from gui_utils import yolact_video_segmentation, yolact_single_image_segmentation, yolact_images_segmentation
import shutil


class Ui_YolactWindow(QMainWindow):
    def see_film(self):
        os.system('python videowindow.py')

    def choose_model(self):
        model_path, _ = QFileDialog.getOpenFileName(self, 'Choose a model file', '', 'Model files | *.pth;')
        url = QUrl.fromLocalFile(model_path)
        print("Model: ", url.fileName())
        self.modelpath_label.setText('Model: ' + os.path.basename(model_path))
        self.model = model_path
        return model_path

    def choose_video(self):
        video_path, _ = QFileDialog.getOpenFileName(self, 'Choose a video file', '', 'Video files | *.avi;')
        url = QUrl.fromLocalFile(video_path)
        print("Video: ", url.fileName())
        self.videopath_label.setText('Video: ' + os.path.basename(video_path))
        shutil.copy(video_path, "D:/yolact/data/{}".format(os.path.basename(video_path)))
        output_path = "D:/yolact/data/output"
        os.makedirs(output_path, exist_ok=True)
        self.video = "data/" + os.path.basename(video_path)
        self.video_output = "data/output/" + os.path.basename(video_path)
        self.segmentation.setDisabled(False)
        return video_path

    def choose_images(self):
        if self.checkBox.isChecked():
            input_image, _ = QFileDialog.getOpenFileName(self, 'Choose an input image file', '', 'Image files | (*.jpg *.png);')
            url_input = QUrl.fromLocalFile(input_image)
            print("Input image: ", url_input.fileName())
            self.imagepath_label.setText("Image: " + os.path.basename(input_image))
            shutil.copy(input_image, "D:/yolact/data/{}".format(os.path.basename(input_image)))
            output_path = "D:/yolact/data/output"
            os.makedirs(output_path, exist_ok=True)
            self.input_image = "data/" + os.path.basename(input_image)
            self.output_image = "data/output/" + os.path.basename(input_image)
            self.segmentation.setDisabled(False)
            return input_image
        else:
            images_input_path = QFileDialog.getExistingDirectory(self, 'Choose an input folder')
            url_input = QUrl.fromLocalFile(images_input_path)
            print("Input images: ", url_input.fileName())
            self.imagepath_label.setText("Images: " + os.path.basename(images_input_path))
            if not os.path.exists("D:/yolact/data/{}".format(os.path.basename(images_input_path))):
                shutil.copytree(images_input_path, "D:/yolact/data/{}".format(os.path.basename(images_input_path)))
            output_path = os.path.join("D:/yolact/data/output", os.path.basename(images_input_path))
            os.makedirs(output_path, exist_ok=True)
            self.images_input_path = "data/" + os.path.basename(images_input_path)
            self.images_output_path = "data/output/" + os.path.basename(output_path)
            self.segmentation.setDisabled(False)
            return images_input_path

    def yolact_segmentation(self):
        if self.model and self.score_threshold.text() and self.topk.text():
            score_threshold = float(self.score_threshold.text())
            topk = int(self.topk.text())
            if self.video and self.video_multiframe.text():
                video_multiframe = int(self.video_multiframe.text())
                yolact_video_segmentation(self.video, self.video_output, self.model, score_threshold, topk, video_multiframe)
            elif self.input_image and self.imagepath_label.text():
                yolact_single_image_segmentation(self.input_image, self.output_image, self.model, score_threshold, topk)
            elif self.images_input_path and self.imagepath_label.text():
                yolact_images_segmentation(self.images_input_path, self.images_output_path, self.model, score_threshold, topk)
            else:
                QMessageBox.warning(self, 'Warning', 'Please provide all parameters', QMessageBox.Ok)
        else:
            QMessageBox.warning(self, 'Warning', 'Please provide all parameters', QMessageBox.Ok)

    def radio_images_clicked(self):
        self.video_multiframe_label.hide()
        self.video_multiframe.hide()
        self.upload_video_button.hide()
        self.videopath_label.hide()

        self.checkBox.show()
        self.upload_images.show()
        self.imagepath_label.show()

    def radio_video_clicked(self):
        self.checkBox.hide()
        self.upload_images.hide()
        self.imagepath_label.hide()

        self.video_multiframe_label.show()
        self.video_multiframe.show()
        self.upload_video_button.show()
        self.videopath_label.show()

    def setupUi(self, YolactWindow):
        self.model = ""
        self.video = ""
        self.input_image = ""
        self.images_input_path = ""
        self.output_image = ""
        self.images_output_path = ""
        self.video_output = ""

        YolactWindow.setObjectName("YolactWindow")
        YolactWindow.resize(600, 480)
        YolactWindow.setMinimumSize(600, 480)
        YolactWindow.setMaximumSize(600, 480)
        YolactWindow.setWindowTitle("YOLACT segmentation")
        YolactWindow.setWindowIcon(QIcon('ivf.png'))

        self.centralwidget = QWidget(YolactWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 1. Upload model
        self.upload_model_button = QPushButton("Upload model", self.centralwidget)
        self.upload_model_button.setGeometry(0, 30, 250, 41)
        self.upload_model_button.setObjectName("upload_model")
        self.upload_model_button.clicked.connect(self.choose_model)
        self.modelpath_label = QLabel("Model: ", self.centralwidget)
        self.modelpath_label.setWordWrap(True)
        self.modelpath_label.setGeometry(250, 30, 500, 41)
        self.modelpath_label.setObjectName("upload_model_label")

        # Score threshold
        self.score_threshold_label = QLabel("Score threshold:", self.centralwidget)
        self.score_threshold_label.setGeometry(30, 100, 130, 21)
        self.score_threshold_label.setObjectName("score_threshold_label")
        self.score_threshold = QLineEdit(self.centralwidget)
        self.score_threshold.setObjectName("score_threshold")
        self.score_threshold.setGeometry(170, 100, 91, 30)
        self.score_threshold.setValidator(QIntValidator())
        self.score_threshold.setText("0.15")

        # Top k
        self.topk_label = QLabel("Top k:", self.centralwidget)
        self.topk_label.setGeometry(30, 150, 130, 21)
        self.topk_label.setObjectName("topk_label")
        self.topk = QLineEdit(self.centralwidget)
        self.topk.setObjectName("topk")
        self.topk.setGeometry(170, 150, 91, 30)
        self.topk.setValidator(QIntValidator())
        self.topk.setText("15")

        # Images or video label
        self.images_or_video = QLabel("Images or video?", self.centralwidget)
        self.images_or_video.setGeometry(30, 200, 201, 21)
        self.images_or_video.setObjectName("images_or_video")


        # Radio Images
        self.radio_images = QRadioButton("images", self.centralwidget)
        self.radio_images.setGeometry(40, 230, 82, 30)
        self.radio_images.setObjectName("radio_images")
        self.radio_images.toggled.connect(self.radio_images_clicked)

        # Radio video
        self.radio_video = QRadioButton("video", self.centralwidget)
        self.radio_video.setGeometry(40, 260, 82, 30)
        self.radio_video.setObjectName("radio_video")
        self.radio_video.toggled.connect(self.radio_video_clicked)

        # Checkbox single image
        self.checkBox = QCheckBox("Single image", self.centralwidget)
        self.checkBox.setGeometry(30, 300, 120, 20)
        self.checkBox.setObjectName("checkBox")
        self.checkBox.hide()

        # Upload image(s)
        self.upload_images = QPushButton("Upload image(s)", self.centralwidget)
        self.upload_images.setGeometry(0, 345, 250, 41)
        self.upload_images.setObjectName("upload_images")
        self.upload_images.clicked.connect(self.choose_images)
        self.upload_images.hide()
        self.imagepath_label = QLabel("Image(s): ", self.centralwidget)
        self.imagepath_label.setWordWrap(True)
        self.imagepath_label.setGeometry(30, 410, 500, 21)
        self.imagepath_label.setObjectName("imagepath_label")
        self.imagepath_label.hide()

        # Video multiframe
        self.video_multiframe_label = QLabel("Video multiframe:", self.centralwidget)
        self.video_multiframe_label.setGeometry(30, 300, 120, 20)
        self.video_multiframe_label.setObjectName("video_multiframe_label")
        self.video_multiframe_label.hide()
        self.video_multiframe = QLineEdit(self.centralwidget)
        self.video_multiframe.setObjectName("video_multiframe")
        self.video_multiframe.setGeometry(170, 290, 91, 30)
        self.video_multiframe.setValidator(QIntValidator())
        self.video_multiframe.setText("4")
        self.video_multiframe.hide()

        # Upload video
        self.upload_video_button = QPushButton("Upload video", self.centralwidget)
        self.upload_video_button.setGeometry(0, 345, 250, 41)
        self.upload_video_button.setObjectName("upload_video")
        self.upload_video_button.clicked.connect(self.choose_video)
        self.upload_video_button.hide()
        self.videopath_label = QLabel("Video: ", self.centralwidget)
        self.videopath_label.setWordWrap(True)
        self.videopath_label.setGeometry(30, 410, 500, 21)
        self.videopath_label.setObjectName("videopath_label")
        self.videopath_label.hide()

        # Start segmentation
        self.segmentation = QPushButton("Start segmentation", self.centralwidget)
        self.segmentation.setGeometry(350, 150, 250, 41)
        self.segmentation.setObjectName("segmentation")
        self.segmentation.clicked.connect(self.yolact_segmentation)
        self.segmentation.setDisabled(True)

        # Visualisation
        self.visualisation = QPushButton("Visualisation", self.centralwidget)
        self.visualisation.setGeometry(350, 220, 250, 41)
        self.visualisation.setObjectName("visualisation")
        self.visualisation.clicked.connect(self.see_film)

        # Menu bar
        # self.menubar = QMenuBar(YolactWindow)
        # self.menubar.setGeometry(0, 0, 711, 21)
        # self.menubar.setObjectName("menubar")
        # YolactWindow.setMenuBar(self.menubar)

        # Menu help
        # self.menuHelp = QMenu("Help", self.menubar)
        # self.menuHelp.setObjectName("menuHelp")
        # self.menubar.addAction(self.menuHelp.menuAction())

        YolactWindow.setCentralWidget(self.centralwidget)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    style = """
        QWidget{
            background: #262D37;
            color: #fff;
        }
        QLabel{
            font: 15px;
        }
        QPushButton
        {
            background: #0577a8;
            border: 1px #DADADA solid;
            padding: 5px 10px;
            border-radius: 15px;
            font-weight: bold;
            font-size: 9pt;
            outline: none;
            margin-left: auto;
            margin-right: auto;
        }
        QPushButton:hover{
            border: 1px #C6C6C6 solid;
            background: #0892D0;
        }
        QPushButton:disabled {
            background-color:#989898;
        }
        QLineEdit {
            padding: 1px;
            border-style: solid;
            border: 2px solid #fff;
            border-radius: 8px;
            font-size: 12pt;
        }
        QMenuBar {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 lightgray, stop:1 darkgray);
        }
        QMenuBar::item {
            spacing: 3px;           
            padding: 2px 10px;
            background-color: rgb(210,105,30);
            color: rgb(255,255,255);  
            border-radius: 5px;
        }
        QMenuBar::item:selected {    
            background-color: rgb(244,164,96);
        }
        QMenuBar::item:pressed {
            background: rgb(128,0,0);
        }
        QRadioButton {
            font: 15px;
        }
        QCheckBox {
            font: 15px;
        }
    """
    app.setStyleSheet(style)
    YolactWindow = QtWidgets.QMainWindow()
    ui = Ui_YolactWindow()
    ui.setupUi(YolactWindow)
    YolactWindow.show()
    sys.exit(app.exec_())
