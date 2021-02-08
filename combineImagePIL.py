from tempfile import template
from tkinter import ttk
from PIL import Image
from io import BytesIO
import random
import glob
import sys
import os
import shutil
import cv2
import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter import filedialog

# 正方形拼接邏輯


def squareMerge():

    imagelist = []
    # sourcePath = 'D:/livingroompic/01'
    sourcePath = sourcePath_entry.get()

    print(sourcePath_entry.get())

    # os.mkdir(sourcePath)
    for name in os.listdir(sourcePath):
        # if name.endswith(getImageSrc + ".jpg"):
        # shutil.copy(sourcePath + '/' + name, sourcePath)
        src = sourcePath + '/' + name
        imagelist.append(src)

    print('imagelistlog', imagelist)

    # Angle of rotation
    angles = [0, 90, 180, 270]

    mergeHeight = int(specifyHeight_entry.get())
    mergeWidth = int(specifyWidth_entry.get())

    print('合併後高度', mergeHeight)
    print('合併後寬度', mergeWidth)

    # create a new empty image
    new_im = Image.new(
        'RGB', (mergeWidth, mergeHeight))

    # get single image size
    singleHeight = int(singleHeight_entry.get())
    singleWidth = int(singleWidth_entry.get())

    print('單張高度', singleHeight)
    print('單張寬度', singleWidth)

    for column in range(0, mergeWidth, singleHeight):

        for row in range(0, mergeHeight, singleWidth):

            choiceResult = random.choice(imagelist)
            rotateAngle = random.choice(angles)

            # open an image
            im = Image.open(choiceResult)
            print("choice log", choiceResult)

            # Resize image
            im.thumbnail((singleHeight, singleWidth))

            new_im.paste(im.rotate(rotateAngle), (column, row))
            print(rotateAngle)

    # mergePath = 'D:/USER/Desktop/mergeImage1.jpg'
    mergePath = specifyPath_entry.get() + "/mergeImage1.jpg"
    # mergePath = 'D:/USER/Desktop/combineTest/mergePicasa.jpg'

    new_im.show()
    new_im.save(mergePath)

    # os.removedirs(tempPath)
    # shutil.rmtree(tempPath)


def rectangleMerge():

    imagelist = []
    # sourcePath = 'D:/livingroompic/01'
    sourcePath = sourcePath_entry.get()

    print(sourcePath_entry.get())

    # os.mkdir(sourcePath)
    for name in os.listdir(sourcePath):
        # if name.endswith(getImageSrc + ".jpg"):
        # shutil.copy(sourcePath + '/' + name, sourcePath)
        src = sourcePath + '/' + name
        imagelist.append(src)

    print('imagelistlog', imagelist)

    # Angle of rotation
    angles = [0, 180]

    mergeHeight = int(specifyHeight_entry.get())
    mergeWidth = int(specifyWidth_entry.get())

    print('合併後高度', mergeHeight)
    print('合併後寬度', mergeWidth)

    # create a new empty image
    new_im = Image.new(
        'RGB', (mergeWidth, mergeHeight))

    # get single image size
    singleHeight = int(singleHeight_entry.get())
    singleWidth = int(singleWidth_entry.get())

    print('單張高度', singleHeight)
    print('單張寬度', singleWidth)

    for column in range(0, mergeWidth, singleWidth):

        for row in range(0, mergeHeight, singleHeight):

            choiceResult = random.choice(imagelist)
            rotateAngle = random.choice(angles)

            # open an image
            im = Image.open(choiceResult)
            print("choice log", choiceResult)

            # Resize image
            im.thumbnail((singleHeight, singleWidth))

            new_im.paste(im.rotate(rotateAngle), (column, row))
            print(rotateAngle)

    # mergePath = 'D:/USER/Desktop/mergeImage1.jpg'
    mergePath = specifyPath_entry.get() + "/mergeImage.jpg"
    # mergePath = 'D:/USER/Desktop/combineTest/mergePicasa.jpg'

    new_im.show()
    new_im.save(mergePath)

    # os.removedirs(tempPath)
    # shutil.rmtree(tempPath)


window = tk.Tk()

window.title('拼接程式(測試版)')
window.geometry('500x400')
window.configure(background='white')

header_label = tk.Label(window, text='拼接輸入欄位')
header_label.pack()

# 以下為 height_frame 群組
source_src = tk.Frame(window)

# 向上對齊父元件
# source_src.pack(side=tk.TOP)
# source_label = tk.Label(source_src, text='來源資料夾路徑')
# source_label.pack(side=tk.LEFT)
# source_entry = tk.Entry(source_src)
# source_entry.pack(side=tk.LEFT)

# 以下為 specifyWidth_frame 群組

# specify_frame = tk.Frame(window)
# specify_frame.pack(side=tk.TOP)
# specify_label = tk.Label(specify_frame, text='拼接完成路徑')
# specify_label.pack(side=tk.LEFT)
# specify_entry = tk.Entry(specify_frame)
# specify_entry.pack(side=tk.LEFT)

# 以下為 specifyWidth_frame 群組
specifyWidth_frame = tk.Frame(window)
specifyWidth_frame.pack(side=tk.TOP)
specifyWidth_label = tk.Label(specifyWidth_frame, text='拼接後圖片尺寸(寬度)')
specifyWidth_label.pack(side=tk.LEFT)
specifyWidth_entry = tk.Entry(specifyWidth_frame)
specifyWidth_entry.pack(side=tk.LEFT)

# 以下為 specifyWidth_frame 群組
specifyHeight_frame = tk.Frame(window)
specifyHeight_frame.pack(side=tk.TOP)
specifyHeight_label = tk.Label(specifyHeight_frame, text='拼接後圖片尺寸(長度)')
specifyHeight_label.pack(side=tk.LEFT)
specifyHeight_entry = tk.Entry(specifyHeight_frame)
specifyHeight_entry.pack(side=tk.LEFT)

# 以下為 specifyWidth_frame 群組
singleHeight_frame = tk.Frame(window)
singleHeight_frame.pack(side=tk.TOP)
singleHeight_label = tk.Label(singleHeight_frame, text='拼接單張圖片尺寸(長度)')
singleHeight_label.pack(side=tk.LEFT)
singleHeight_entry = tk.Entry(singleHeight_frame)
singleHeight_entry.pack(side=tk.LEFT)

# 以下為 specifyWidth_frame 群組
singleWidth_frame = tk.Frame(window)
singleWidth_frame.pack(side=tk.TOP)
singleWidth_label = tk.Label(singleWidth_frame, text='拼接單張圖片尺寸(寬度)')
singleWidth_label.pack(side=tk.LEFT)
singleWidth_entry = tk.Entry(singleWidth_frame)
singleWidth_entry.pack(side=tk.LEFT)

result_label = tk.Label(window)
result_label.pack()


# source path select
def sourceFolder_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global sourceFolder_path
    filename = filedialog.askdirectory()
    sourceFolder_path.set(filename)
    print(filename)

# specify path select


def specifyFolder_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global specifyFolder_path
    filename = filedialog.askdirectory()
    specifyFolder_path.set(filename)
    print(filename)


# source path logic
v = tk.StringVar()
sourceFolder_path = tk.StringVar()

sourcePath_frame = tk.Frame(window)
sourcePath_frame.pack(side=tk.TOP)
sourcelbl = tk.Label(sourcePath_frame, text='來源路徑資料夾')

sourcelbl.pack(side=tk.LEFT)
sourcePath_entry = tk.Entry(sourcePath_frame, textvariable=sourceFolder_path)
sourcePath_entry.pack(side=tk.LEFT)

sourceButton = tk.Button(text="Browse", command=sourceFolder_button)
sourcePath_entry.pack(side=tk.LEFT)
sourceButton.pack()

# specify path logic
v = tk.StringVar()
specifyFolder_path = tk.StringVar()

specifyPath_frame = tk.Frame(window)
specifyPath_frame.pack(side=tk.TOP)
sourcelbl = tk.Label(specifyPath_frame, text='合併完成路徑資料夾')

sourcelbl.pack(side=tk.LEFT)
specifyPath_entry = tk.Entry(
    specifyPath_frame, textvariable=specifyFolder_path)
specifyPath_entry.pack(side=tk.LEFT)

sourceButton = tk.Button(text="Browse", command=specifyFolder_button)
sourceButton.pack()


squareMerge = tk.Button(
    window, text='正方形拼接', command=squareMerge)
squareMerge.pack()

rectangleMerge = tk.Button(
    window, text='長方形拼接', command=rectangleMerge)
rectangleMerge.pack()

window.mainloop()
