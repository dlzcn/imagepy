#from __future__ import absolute_import
import os.path as osp
import sys, os, wx

root_dir = osp.abspath(osp.dirname(__file__))
print(root_dir)
#sys.path.append(root_dir)

from .imageplus import ImagePlus
from .ui.imagepy import ImagePy


def show():
	app = wx.App(False)
	mainFrame = ImagePy(None)
	mainFrame.SetTitle('海冰影像分析软件')
	mainFrame.Show()
	app.MainLoop()