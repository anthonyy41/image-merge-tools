from tempfile import template
from PIL import Image
import random
import glob
import sys
from io import BytesIO
import os
import shutil
import cv2
import threading
from tqdm import tqdm
import time
import tkinter as tk
from tkinter import ttk


def main():

    # tempPath = 'D:/USER/Desktop/combineTest/temp'
    # if os.path.exists(tempPath):
    #     shutil.rmtree(tempPath)

    # getImageSrc = sys.argv[1]ㄋ
    # getImageSrc = '388-200610170'
    # folder = 'UploadFolder'

    # get image array and random choice
    # list_im = ['Test1.jpg', 'Test2.jpg', 'Test3.jpg']

    # get image src(use PIL)
    # imagelist = sorted(
    #     # glob.glob('D:/USER/Desktop/combineTest/' + 'Test*.jpg'))
    #     # glob.glob('D:/USER/Desktop/combineTest/' + getImageSrc+'*' + '.jpg'))
    #     # glob.glob('D:/VisualStudioProject/Reality_CounselingCase/UploadFolder/' + getImageSrc+'*' + '.jpg'))
    #     glob.glob('D:/VisualStudioProject/Reality_CounselingCase/wwwroot/' + getImageSrc+'*' + '.jpg'))
    # print('imagelistlog', imagelist)

    # get image src(use os)

    imagelist = []
    sourcePath = 'D:/USER/Desktop/combineTest/04'

    # os.mkdir(sourcePath)
    for name in os.listdir(sourcePath):
        # if name.endswith(getImageSrc + ".jpg"):
        # shutil.copy(sourcePath + '/' + name, sourcePath)
        src = sourcePath + '/' + name
        imagelist.append(src)

    print('imagelistlog', imagelist)

    # Angle of rotation
    angles = [0, 90, 180, 270]

    # create a new empty image
    new_im = Image.new('RGB', (34016, 42520))

    for column in range(0, 34016, 8504):

        for row in range(0, 42520, 8504):

            choiceResult = random.choice(imagelist)
            rotateAngle = random.choice(angles)

            # open an image
            im = Image.open(choiceResult)
            print("choice log", choiceResult)

            # Resize image
            # im.thumbnail((1000, 8504))

            new_im.paste(im.rotate(rotateAngle), (column, row))
            print(rotateAngle)

    mergePath = 'D:/USER/Desktop/combineTest/mergeImage.jpg'
    # mergePath = 'D:/USER/Desktop/combineTest/mergePicasa.jpg'

    new_im.show()
    new_im.save(mergePath)

    # os.removedirs(tempPath)
    # shutil.rmtree(tempPath)





main()
