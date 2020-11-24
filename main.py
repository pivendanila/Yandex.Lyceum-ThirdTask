import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageDraw
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 440, 500)
        self.setWindowTitle('Git')
        self.pushButton = QPushButton('OK', self)
        self.pushButton.resize(110, 30)
        self.pushButton.move(150, 410)
        self.label = QLabel(self)
        self.label.resize(150, 150)
        self.label.move(30, 10)
        self.label.setText('')
        self.label_2 = QLabel(self)
        self.label_2.resize(150, 150)
        self.label_2.move(210, 60)
        self.label_2.setText('')
        self.label_3 = QLabel(self)
        self.label_3.resize(150, 150)
        self.label_3.move(40, 180)
        self.label_3.setText('')
        self.label_4 = QLabel(self)
        self.label_4.resize(150, 150)
        self.label_4.move(240, 220)
        self.label_4.setText('')

        self.pushButton.clicked.connect(self.run)

    def run(self):
        new_image = Image.new('RGB', (150, 150), (240, 240, 240))
        x = 75
        y = 75
        new_image = Image.new('RGB', (150, 150), (240, 240, 240))
        radius = random.randint(10, 75)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        draw = ImageDraw.Draw(new_image)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(r, g, b))
        new_image.save('ellipse.jpeg')
        self.pixmap = QPixmap('ellipse.jpeg')
        self.label.setPixmap(self.pixmap)
        new_image = Image.new('RGB', (150, 150), (240, 240, 240))
        radius = random.randint(10, 75)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        draw = ImageDraw.Draw(new_image)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(r, g, b))
        new_image.save('ellipse.jpeg')
        self.pixmap = QPixmap('ellipse.jpeg')
        self.label_2.setPixmap(self.pixmap)
        new_image = Image.new('RGB', (150, 150), (240, 240, 240))
        radius = random.randint(10, 75)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        draw = ImageDraw.Draw(new_image)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(r, g, b))
        new_image.save('ellipse.jpeg')
        self.pixmap = QPixmap('ellipse.jpeg')
        self.label_3.setPixmap(self.pixmap)
        new_image = Image.new('RGB', (150, 150), (240, 240, 240))
        radius = random.randint(10, 75)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        draw = ImageDraw.Draw(new_image)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(r, g, b))
        new_image.save('ellipse.jpeg')
        self.pixmap = QPixmap('ellipse.jpeg')
        self.label_4.setPixmap(self.pixmap)

    def circle(self):
        new_image = Image.new('RGB', (150, 150), (240, 240, 240))
        radius = random.randint(10, 75)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        draw = ImageDraw.Draw(new_image)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(r, g, b))
        new_image.save('ellipse.jpeg')
        pixmap = QPixmap('ellipse.jpeg')
        return pixmap


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
