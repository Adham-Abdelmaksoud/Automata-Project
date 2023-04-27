from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import pydot
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import sys
from random import random
from PyQt5.QtWidgets import QMessageBox
import graphviz as gv
from matplotlib import image
import cv2

class GraphWidget(QWidget):
    def __init__(self):
        super(GraphWidget, self).__init__()
        
        self.figure = plt.figure()
        self.canvas = FigureCanvasQTAgg(self.figure)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.canvas)

def aspectResize(path, width, height):
    height -= 40
    width -= 40
    img = cv2.imread(path)
    h, w = img.shape[:2]
    aspect = w/h
    img = cv2.resize(img, (np.clip(int(aspect*height), 0, width), height))
    plt.imsave(path, img, cmap='gray')