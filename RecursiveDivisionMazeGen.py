"""
tkinter for graphics
    tkinter canvas

Node
    [x, y]
    walls associated with it [bottom, right]
    visited(boolean)
    and state (no walls = 0, 1 wall = 1,etc...)(optional for me)

Wall
    bottom and right side of node

Maze
    2D grid of nodes
    window = tk.Tk()

Recursive Division
    take maze of size n by n
    divide n by 2 until left with 16 individual squares
    start in the top left square, move down, then top/second from left square, move down
        repeat for each division and for entire maze
        chose 3 of 4 walls and create on opening for the 3 chosen walls
        continue recursively until complete

    grid of nodes
        nodes in list
    nodes have right and bottom walls
    perimeter nodes generated first
        maze split recursively until filled in

"""

import tkinter as tk
from tkinter import *
import random
import time

tk = Tk()
X, Y = 50, 50
width = X * 20
height = Y * 20
mult = width // X
nodeList = []
wallList = []
color = 'white'
tf = 0
count = []

class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coords = (x, y)

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def __repr__(self):
        return str(self.coords)

class Wall():
    def __init__(self, xx, yy, xx2, yy2, colorWX, colorWY):
        self.xx = xx
        self.yy = yy
        self.xx2 = xx2
        self.yy2 = yy2
        self.colorWX = color #will be white for off, black for on
        self.colorWY = color

    def getxx(self):
        return self.xx

    def getyy(self):
        return self.yy

    def getxx2(self):
        return self.xx2

    def getyy2(self):
        return self.yy2

    def getColorWX(self):
        return self.colorWX

    def setColorWX(self, newColor):
        self.colorWX = newColor

    def getColorWY(self):
        return self.colorWY

    def setColorWY(self, newColor):
        self.colorWY = newColor


    def __repr__(self):
        return "["+ str(self.xx) +", "+ str(self.yy) +", "+ str(self.xx2) +", "+ str(self.yy2) +", "+ str(self.colorWX) +", "+ str(self.colorWY) +"]"

def creatWalls(nodeList):
    wL = []
    horizontal = []
    vertical = []
    for n in nodeList:
        hw = Wall(n.getx(), n.gety(), n.getx() - mult, n.gety(), 'white', 'white')
        horizontal.append(hw)
        vw = Wall(n.getx(), n.gety(), n.getx(), n.gety() - mult, 'white', 'white')
        vertical.append(vw)

    for h in horizontal:
        wL.append(h)
    for v in vertical:
        wL.append(v)

    return wL

def createNodes():
    for i in range(X):
        for j in range(Y):
            # new node at [x, y]
            n = Node((i+1)*mult, (j+1)*mult)
            nodeList.append(n)

def buildMaze(walls):

    grid = Canvas(tk, width = 800, height = 800)
    grid.pack(expand = TRUE, fill = BOTH)

    '''creates horizontal then vertical walls'''
    for w in walls:
        grid.create_line(w.getxx()+1, w.getyy()+1, w.getxx2()+1, w.getyy()+1, fill = w.getColorWX())
        grid.create_line(w.getxx()+1, w.getyy()+1, w.getxx()+1, w.getyy2()+1, fill = w.getColorWY())

    grid.create_line(2+20, 2, height+1, 2)
    grid.create_line(2, 2, 2, height+1)
    grid.create_line(width+1, width+1, height+1, 2)
    grid.create_line(width+1, width+1, 2, height+1)

    grid.create_line(wallList[-1].getxx()+1, wallList[-1].getyy()+1, wallList[-1].getxx2()+1, wallList[-1].getyy2()+1, fill = 'white')

    tf = time.time()
    tim = tf - ti
    print(tim)
    grid.mainloop()

def recBuildV2(walls, width, height, widthx, heighty):
    count.append(1)

    onX = []
    onY = []

    dx = width - widthx
    dy = height - heighty

    # print(width, height, widthx, heighty)
    # print("walls "+ str(walls))
    if dx == 0 or dy == 0:
        return

    elif dx == dy:
        newList1 = [] #upper or left side
        newList2 = [] #lower or right side

        '''if 1, horizontal, if 2, vertical'''
        check = random.randint(1, 2)
        #print(check)
        '''horizontal'''
        if check == 1:
            choice = random.randrange(heighty, height, 20)
            #print(choice)
            for wx in walls:
                if wx.getyy() == choice and wx.getyy2() == choice:
                    wx.setColorWX('black')
                    onX.append(wx)
            wx = random.choice(onX)
            wx.setColorWX('white')
            onX.clear()

            '''creates new lists for upper/lower grids'''
            for w in walls:
                if w.getyy() <= choice and w.getyy2() <= choice:
                    newList1.append(w)
                if w.getyy() > choice and w.getyy2() > choice:
                    newList2.append(w)
            # print("newList1 " + str(newList1))
            # print("newList2 " + str(newList2))

            wid1 = []
            hei1 = []
            for nl1 in newList1:
                wid1.append(nl1.getxx())
                hei1.append(nl1.getyy())
            if wid1:
                newWidthMax10 = max(wid1)
                newWidthMin10 = min(wid1)
            if hei1:
                newHeightMax10 = max(hei1)
                newHeightMin10 = min(hei1)
            wid2 = []
            hei2 = []
            for nl2 in newList2:
                wid2.append(nl2.getxx())
                hei2.append(nl2.getyy())
            if wid2:
                newWidthMax20 = max(wid2)
                newWidthMin20 = min(wid2)
            if hei2:
                newHeightMax20 = max(hei2)
                newHeightMin20 = min(hei2)

        '''vertical'''
        if check == 2:
            choice = random.randrange(widthx, width, 20)
            #print(choice)
            for wy in walls:
                if wy.getxx() == choice and wy.getxx2() == choice:
                    wy.setColorWY('black')
                    onY.append(wy)
            wy = random.choice(onY)
            wy.setColorWY('white')
            onY.clear()

            '''creates new lists for left/right grids'''
            for w in walls:
                if w.getxx() <= choice and w.getxx2() <= choice:
                    newList1.append(w)
                if w.getxx() > choice and w.getxx2() > choice:
                    newList2.append(w)
            # print("newList1 " + str(newList1))
            # print("newList2 " + str(newList2))

            wid1 = []
            hei1 = []
            for nl1 in newList1:
                wid1.append(nl1.getxx())
                hei1.append(nl1.getyy())
            if wid1:
                newWidthMax10 = max(wid1)
                newWidthMin10 = min(wid1)
            if hei1:
                newHeightMax10 = max(hei1)
                newHeightMin10 = min(hei1)
            wid2 = []
            hei2 = []
            for nl2 in newList2:
                wid2.append(nl2.getxx())
                hei2.append(nl2.getyy())
            if wid2:
                newWidthMax20 = max(wid2)
                newWidthMin20 = min(wid2)
            if hei2:
                newHeightMax20 = max(hei2)
                newHeightMin20 = min(hei2)

        if wid1 or hei1:
            recBuildV2(newList1, newWidthMax10, newHeightMax10, newWidthMin10, newHeightMin10)
        if wid2 or hei2:
            recBuildV2(newList2, newWidthMax20, newHeightMax20, newWidthMin20, newHeightMin20)

    #if width > height create vertical line
    elif dx > dy:
        new1 = []
        new2 = []
        choice = random.randrange(widthx, width, 20)
        #print(choice)
        for wy in walls:
            if wy.getxx() == choice and wy.getxx2() == choice:
                wy.setColorWY('black')
                onY.append(wy)
        wy = random.choice(onY)
        wy.setColorWY('white')
        onY.clear()

        for w in walls:
            if w.getxx() <= choice and w.getxx2() <= choice:
                new1.append(w)
            if w.getxx() > choice and w.getxx2() > choice:
                new2.append(w)
        # print("new1 " + str(new1))
        # print("new2 " + str(new2))

        wid1 = []
        hei1 = []
        for nl1 in new1:
            wid1.append(nl1.getxx())
            hei1.append(nl1.getyy())
        if wid1:
            newWidthMax11 = max(wid1)
            newWidthMin11 = min(wid1)
        if hei1:
            newHeightMax11 = max(hei1)
            newHeightMin11 = min(hei1)
        wid2 = []
        hei2 = []
        for nl2 in new2:
            wid2.append(nl2.getxx())
            hei2.append(nl2.getyy())
        if wid2:
            newWidthMax21 = max(wid2)
            newWidthMin21 = min(wid2)
        if hei2:
            newHeightMax21 = max(hei2)
            newHeightMin21 = min(hei2)

        if wid1 or hei1:
            recBuildV2(new1, newWidthMax11, newHeightMax11, newWidthMin11, newHeightMin11)
        if wid2 or hei2:
            recBuildV2(new2, newWidthMax21, newHeightMax21, newWidthMin21, newHeightMin21)

    #if width < height create horizontal line
    elif dx < dy:
        n1 = []
        n2 = []
        choice = random.randrange(heighty, height, 20)
        #print(choice)
        for wx in walls:
            if wx.getyy() == choice and wx.getyy2() == choice:
                wx.setColorWX('black')
                onX.append(wx)
        wx = random.choice(onX)
        wx.setColorWX('white')
        onX.clear()

        for w in walls:
            if w.getyy() <= choice and w.getyy2() <= choice:
                n1.append(w)
            if w.getyy() > choice and w.getyy2() > choice:
                n2.append(w)
        # print("n1 " + str(n1))
        # print("n2 " + str(n2))

        wid1 = []
        hei1 = []
        for nl1 in n1:
            wid1.append(nl1.getxx())
            hei1.append(nl1.getyy())
        if wid1:
            newWidthMax12 = max(wid1)
            newWidthMin12 = min(wid1)
        if hei1:
            newHeightMax12 = max(hei1)
            newHeightMin12 = min(hei1)
        wid2 = []
        hei2 = []
        for nl2 in n2:
            wid2.append(nl2.getxx())
            hei2.append(nl2.getyy())
        if wid2:
            newWidthMax22 = max(wid2)
            newWidthMin22 = min(wid2)
        if hei2:
            newHeightMax22 = max(hei2)
            newHeightMin22 = min(hei2)

        if wid1 or hei1:
            recBuildV2(n1, newWidthMax12, newHeightMax12, newWidthMin12, newHeightMin12)
        if wid2 or hei2:
            recBuildV2(n2, newWidthMax22, newHeightMax22, newWidthMin22, newHeightMin22)

# def recBuild(walls, width, height, xStart, yStart, X, Y):
#     '''
#     iterate through wallList and find x and y values that equal half of the maze
#     create line that splits maze in quarters
#         select one random wall to open using an index
#
#     probs need some recursive call
#         so.....
#         divide x by 2 and y by 2 until cant anymore
#         base case:
#         rec call:
#     '''
#
#     '''find half width and height'''
#     wid = (width//2) + xStart
#     hei = (height//2) + yStart
#     ww1 = width - xStart
#     hh1 = height - yStart
#
#     '''quadrant lists'''
#     q1 = []
#     q2 = []
#     q3 = []
#     q4 = []
#
#     '''divide lists'''
#     onX = []
#     onY = []
#
#     '''base case'''
#     if X<3 or Y<3:
#         showMaze()
#
#     else:
#
#         '''for x and y at half width, height turn on all walls'''
#         '''choose random wall to turn off for each quadrant'''
#         '''vertical divide'''
#         for wy in walls:
#             if wy.getxx() == wid and wy.getxx2() == wid:
#                 wy.setColorWY('black')
#                 onY.append(wy)
#         '''vertical wall turn off'''
#         '''first half'''
#         yw1 = random.choice(onY[:(X//2)+1])
#         yw1.setColorWY('white')
#         '''second half'''
#         yw2 = random.choice(onY[(X//2)+1:])
#         yw2.setColorWY('white')
#
#         '''horizontal divide'''
#         for wx in walls:
#             if wx.getyy() == hei and wx.getyy2() == hei:
#                 wx.setColorWX('black')
#                 onX.append(wx)
#         '''horizontal wall turn off'''
#         '''first half'''
#         xw1 = random.choice(onX[:(Y//2)+1])
#         xw1.setColorWX('white')
#         '''second half'''
#         xw2 = random.choice(onX[(Y//2)+1:])
#         xw2.setColorWX('white')
#
#         print('round')
#
#         '''create q1, q2, q3, q4 lists'''
#         for W in walls:
#             '''where x1 > half width and y1 <= half height'''
#             if (W.getxx() > wid) and (W.getyy() <= hei):
#                 q1.append(W)
#
#             '''where x1 <= half width and y1 <= half height'''
#             if (W.getxx() <= wid) and (W.getyy() <= hei):
#                 q2.append(W)
#
#             '''where x1 <= half width and y1 > half height'''
#             if (W.getxx() <= wid) and (W.getyy() > hei):
#                 q3.append(W)
#
#             '''where x1 > half width and y1 > half height'''
#             if (W.getxx() > wid) and (W.getyy() > hei):
#                 q4.append(W)
#
#         recBuild(q1, width//2, height//2, wid, 0, X//2, Y//2)
#         recBuild(q2, width//2, height//2, 0, 0, X//2, Y//2)
        # recBuild(q3, width and height of q3: bottom left)
        # recBuild(q4, width and height of q4: bottom right)

        #return walls

i = 0
ti = time.time()
createNodes()
wallList = creatWalls(nodeList)
recBuildV2(wallList, width, height, 20, 20)
buildMaze(wallList)
#print(len(count))
