from PyQt5 import QtWidgets
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow
from controller import Controller


class ClickableLabel(QtWidgets.QLabel):
    def __init__(self, widget):
        super(ClickableLabel, self).__init__(widget)
        self.main = widget

    def mousePressEvent(self, event):
        self.main.show_details(event.pos())


class Gui(QMainWindow):

    def __init__(self):
        super().__init__()

        self.controller = Controller()

        self.setFixedSize(1800, 800)
        self.setWindowTitle("Viewer")

        self.shape_selector = QtWidgets.QComboBox(self)
        self.shape_selector.addItems(['bench', 'chair'])
        self.refresh_button = QtWidgets.QPushButton(self)
        self.refresh_button.setText('Refresh')
        self.refresh_button.setIcon(QIcon('assets/refresh.png'))
        self.summary_pane = ClickableLabel(self)
        self.true_img_pane = QtWidgets.QLabel(self)
        self.pred_img_pane = QtWidgets.QLabel(self)
        self.true_legend = QtWidgets.QLabel(self)
        self.pred_legend = QtWidgets.QLabel(self)

        self.shape_selector.move(50, 50)
        self.refresh_button.move(970, 50)
        self.summary_pane.move(1090, 50)
        self.true_img_pane.move(50, 130)
        self.pred_img_pane.move(570, 130)
        self.true_legend.move(280, 650)
        self.pred_legend.move(790, 650)

        self.shape_selector.activated[str].connect(self.show_summary)
        self.refresh_button.clicked.connect(self.refresh)

        self.show()
        self.show_summary()

    def __pil_to_pixmap(self, img):
        data = img.tobytes('raw', 'RGB')
        qim = QImage(data, img.size[0], img.size[1], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qim)
        return pixmap

    def refresh(self):
        self.controller.initialize()
        self.show_summary()

    def show_summary(self):
        shape_name = self.shape_selector.currentText()
        summary_img = self.controller.get_summary(shape_name)
        pixmap = self.__pil_to_pixmap(summary_img)
        self.summary_pane.setPixmap(pixmap)
        self.summary_pane.adjustSize()
        self.true_img_pane.clear()
        self.true_legend.clear()
        self.pred_img_pane.clear()
        self.pred_legend.clear()

    def show_details(self, pos):
        shape_name = self.shape_selector.currentText()
        index = str(pos.y()//128) + str(pos.x()//64)
        true_img, pred_img = self.controller.get_details(shape_name, int(index))
        true_pixmap = self.__pil_to_pixmap(true_img)
        pred_pixmap = self.__pil_to_pixmap(pred_img)
        self.true_img_pane.setPixmap(true_pixmap)
        self.pred_img_pane.setPixmap(pred_pixmap)
        self.true_img_pane.adjustSize()
        self.pred_img_pane.adjustSize()
        self.true_legend.setText('Original')
        self.pred_legend.setText('Procedural')
