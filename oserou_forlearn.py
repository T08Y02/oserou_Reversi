import tkinter as tk
import csv
import os
import time
import random

class Tkgui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(u"oserou")
        self.root.geometry("500x500")
        self.canvas = tk.Canvas(self.root, width = 500, height = 500)
        self.canvas.place(x=0, y=0)
        self.canvas.bind('<ButtonPress-1>', self.click_upload)
        self.clk_ok = True

    def ban_image(self,ban):
        self.canvas.delete("all")
        self.canvas.create_rectangle(50, 50, 450, 450, fill = 'green')
        for i in range(8):
            self.canvas.create_line(50+50*i, 50, 50+50*i, 450, fill='black', width = '1')
        for i in range(8):
            self.canvas.create_line(50,50+50*i, 450, 50+50*i, fill='black', width = '1')
        for i in range(8):
            for j in range(8):
                if ban[i][j] == 1:
                    self.canvas.create_oval(50 + 50*j, 50 + 50*i, 100 + 50*j, 100 + 50*i, fill = 'black')
                elif ban[i][j] == 2:
                    self.canvas.create_oval(50 + 50*j, 50 + 50*i, 100 + 50*j, 100 + 50*i, fill = 'white')
                else:
                    continue
        self.root.update()


    def click_upload(self, event):
        if self.clk_ok:
            global gyoudayo
            global retudayo
            gyoudayo = event.y // 50 - 1
            retudayo = event.x // 50 - 1
            self.canvas.delete('oval')
            self.canvas.create_oval(50 + 50*retudayo, 50 + 50*gyoudayo, 100 + 50*retudayo, 100 + 50*gyoudayo, fill = 'red', tag = 'oval')

    def clkok(self):
        self.clk_ok = False

    def wait_click(self,a):
        self.clk_ok = True
        a = int(a)
        self.root.after(a * 1000, self.clkok)
        while self.clk_ok:
            self.root.update()

def osero_initialize(ban):
    #0 = blank
    #1 = black
    #2 = white
    ban[3][3] = 2
    ban[4][4] = 2
    ban[3][4] = 1
    ban[4][3] = 1
    return ban

def ban_place(ban, gyou, retsu, color):
    ban[gyou][retsu] = color
    return ban

def ban_reverse(ban, gyou, retsu):
    if ban[gyou][retsu] == 1:
        ban[gyou][retsu] = 2
    elif ban[gyou][retsu] == 2:
        ban[gyou][retsu] = 1
    else:
        print("error")
    return ban

def ban_reverse_onestone(ban, gyou, retsu, color):
    before_c = 0
    after_c = 0
    if color == 2:
        before_c = 1
        after_c = 2
    else:
        before_c = 2
        after_c = 1
    ue = 0
    migiue = 0
    migi = 0
    migisita = 0
    sita = 0
    hidarisita = 0
    hidari = 0
    hidariue = 0

    for i in range(gyou+1):
        if i == 0:
            if gyou-i == 0:
                break
            else:
                continue
        else:
            if gyou - i == 0:
                if ban[gyou-i][retsu] == after_c:
                    break
                else:
                    ue = 0
                    break
            else:
                if ban[gyou-i][retsu] == before_c:
                    ue += 1
                elif ban[gyou-i][retsu] == after_c:
                #print(gyou-i)
                    break
                else:
                    ue = 0
                    break
    for i in range(ue):
        ban = ban_reverse(ban, gyou - i - 1, retsu)

    for i in range(7 - retsu + 1):
        if i==0:
            if retsu + i == 7:
                break
            else:
                continue
        else:
            if retsu + i == 7:
                if ban[gyou][retsu + i] == after_c:
                    break
                else:
                    migi = 0
                    break
            else:
                if ban[gyou][retsu + i] == before_c:
                    migi += 1
                elif ban[gyou][retsu + i] == after_c:
                    break
                else:
                    migi = 0
                    break
    for i in range(migi):
        ban = ban_reverse(ban, gyou, retsu + i + 1)

    for i in range(7 - gyou + 1):
        if i==0:
            if gyou + i == 7:
                break
            else:
                continue
        else:
            if gyou + i == 7:
                if ban[gyou+i][retsu] == after_c:
                    break
                else:
                    sita = 0
                    break
            else:
                if ban[gyou+i][retsu] == before_c:
                    sita += 1
                elif ban[gyou + i][retsu] == after_c:
                    break
                else:
                    sita = 0
                    break
    for i in range(sita):
        ban = ban_reverse(ban, gyou + i + 1, retsu)


    for i in range(retsu+1):
        if i == 0:
            if retsu - i == 0:
                break
            else:
                continue
        else:
            if retsu - i == 0:
                if ban[gyou][retsu - i] == after_c:
                    break
                else:
                    hidari = 0
                    break
            else:
                if ban[gyou][retsu-i] == before_c:
                    hidari += 1
                elif ban[gyou][retsu-i] == after_c:
                    #print(gyou-i)
                    break
                else:
                    hidari = 0
                    break

    for i in range(hidari):
        ban = ban_reverse(ban, gyou, retsu - i - 1)

    for i in range(gyou+1):
        if i==0:
            if retsu + i == 7 or gyou - i == 0:
                break
            else:
                continue
        else:
            if retsu + i == 7:
                if ban[gyou - i][retsu + i] == after_c:
                    break
                else:
                    migiue = 0
                    break
            elif gyou - i == 0:
                if ban[gyou - i][retsu + i] == after_c:
                    break
                else:
                    migiue = 0
                    break
            else:
                if ban[gyou - i][retsu + i] == before_c:
                    migiue += 1
                elif ban[gyou - i][retsu + i] == after_c:
                    break
                else:
                    migiue = 0
                    break
    for i in range(migiue):
        ban = ban_reverse(ban, gyou - i - 1, retsu + i + 1)


    for i in range(7- gyou +1):
        if i==0:
            if retsu + i == 7 or gyou + i == 7:
                break
            else:
                continue
        else:
            if retsu + i == 7:
                if ban[gyou + i][retsu + i] == after_c:
                    break
                else:
                    migisita = 0
                    break
            elif gyou + i == 7:
                if ban[gyou + i][retsu + i] == after_c:
                    break
                else:
                    migisita = 0
                    break
            else:
                if ban[gyou + i][retsu + i] == before_c:
                    migisita += 1
                elif ban[gyou + i][retsu + i] == after_c:
                    break
                else:
                    migisita = 0
                    break
    for i in range(migisita):
        ban = ban_reverse(ban, gyou + i + 1, retsu + i + 1)


    for i in range(7- gyou +1):
        if i==0:
            if retsu - i == 0 or gyou + i == 7:
                break
            else:
                continue
        else:
            if retsu - i == 0:
                if ban[gyou + i][retsu - i] == after_c:
                    break
                else:
                    hidarisita = 0
                    break
            elif gyou + i == 7:
                if ban[gyou + i][retsu - i] == after_c:
                    break
                else:
                    hidarisita = 0
                    break
            else:
                if ban[gyou + i][retsu - i] == before_c:
                    hidarisita += 1
                elif ban[gyou + i][retsu - i] == after_c:
                    break
                else:
                    hidarisita = 0
                    break
    for i in range(hidarisita):
        ban = ban_reverse(ban, gyou + i + 1, retsu - i - 1)


    for i in range(gyou+1):
        if i==0:
            if retsu - i == 0 or gyou - i == 0:
                break
            else:
                continue
        else:
            if retsu - i == 0:
                if ban[gyou - i][retsu - i] == after_c:
                    break
                else:
                    hidariue = 0
                    break
            elif gyou - i == 0:
                if ban[gyou - i][retsu - i] == after_c:
                    break
                else:
                    hidariue = 0
                    break
            else:
                if ban[gyou - i][retsu - i] == before_c:
                    hidariue += 1
                elif ban[gyou - i][retsu - i] == after_c:
                    break
                else:
                    hidariue = 0
                    break
    for i in range(hidariue):
        ban = ban_reverse(ban, gyou - i - 1, retsu - i - 1)

    return ban

def ban_placestone(ban, gyou, retsu, color):
    ban = ban_place(ban, gyou, retsu, color)
    ban = ban_reverse_onestone(ban, gyou, retsu, color)
    return ban

def score_initialize(vrhi, hi, mid, lw, vrlw):
    score =   [[vrhi, mid, hi, hi, hi, hi, mid, vrhi],
             [mid, vrlw, lw, lw, lw, lw, vrlw, mid],
             [hi, lw, hi, mid, mid, hi, lw, hi],
             [hi, lw, mid, mid, mid, mid, lw, hi],
             [hi, lw, mid, mid, mid, mid, lw, hi],
             [hi, lw, hi, mid, mid, hi, lw, hi],
             [mid, vrlw, lw, lw, lw, lw, vrlw, mid],
             [vrhi, mid, hi, hi, hi, hi, mid, vrhi]]
    return score

def score_count(ban, gyou, retsu, color):
    before_c = 0
    after_c = 0
    if color == 2:
        before_c = 1
        after_c = 2
    else:
        before_c = 2
        after_c = 1

    ue = 0
    migiue = 0
    migi = 0
    migisita = 0
    sita = 0
    hidarisita = 0
    hidari = 0
    hidariue = 0
    scoreall = 0

    for i in range(gyou+1):
        if i == 0:
            if gyou-i == 0:
                break
            else:
                continue
        else:
            if gyou - i == 0:
                if ban[gyou-i][retsu] == after_c:
                    break
                else:
                    ue = 0
                    break
            else:
                if ban[gyou-i][retsu] == before_c:
                    ue += 1
                elif ban[gyou-i][retsu] == after_c:
                #print(gyou-i)
                    break
                else:
                    ue = 0
                    break

    for i in range(7 - retsu + 1):
        if i==0:
            if retsu + i == 7:
                break
            else:
                continue
        else:
            if retsu + i == 7:
                if ban[gyou][retsu + i] == after_c:
                    break
                else:
                    migi = 0
                    break
            else:
                if ban[gyou][retsu + i] == before_c:
                    migi += 1
                elif ban[gyou][retsu + i] == after_c:
                    break
                else:
                    migi = 0
                    break

    for i in range(7 - gyou + 1):
        if i==0:
            if gyou + i == 7:
                break
            else:
                continue
        else:
            if gyou + i == 7:
                if ban[gyou+i][retsu] == after_c:
                    break
                else:
                    sita = 0
                    break
            else:
                if ban[gyou+i][retsu] == before_c:
                    sita += 1
                elif ban[gyou + i][retsu] == after_c:
                    break
                else:
                    sita = 0
                    break


    for i in range(retsu+1):
        if i == 0:
            if retsu - i == 0:
                break
            else:
                continue
        else:
            if retsu - i == 0:
                if ban[gyou][retsu - i] == after_c:
                    break
                else:
                    hidari = 0
                    break
            else:
                if ban[gyou][retsu-i] == before_c:
                    hidari += 1
                elif ban[gyou][retsu-i] == after_c:
                    #print(gyou-i)
                    break
                else:
                    hidari = 0
                    break


    for i in range(gyou+1):
        if i==0:
            if retsu + i == 7 or gyou - i == 0:
                break
            else:
                continue
        else:
            if retsu + i == 7:
                if ban[gyou - i][retsu + i] == after_c:
                    break
                else:
                    migiue = 0
                    break
            elif gyou - i == 0:
                if ban[gyou - i][retsu + i] == after_c:
                    break
                else:
                    migiue = 0
                    break
            else:
                if ban[gyou - i][retsu + i] == before_c:
                    migiue += 1
                elif ban[gyou - i][retsu + i] == after_c:
                    break
                else:
                    migiue = 0
                    break


    for i in range(7- gyou +1):
        if i==0:
            if retsu + i == 7 or gyou + i == 7:
                break
            else:
                continue
        else:
            if retsu + i == 7:
                if ban[gyou + i][retsu + i] == after_c:
                    break
                else:
                    migisita = 0
                    break
            elif gyou + i == 7:
                if ban[gyou + i][retsu + i] == after_c:
                    break
                else:
                    migisita = 0
                    break
            else:
                if ban[gyou + i][retsu + i] == before_c:
                    migisita += 1
                elif ban[gyou + i][retsu + i] == after_c:
                    break
                else:
                    migisita = 0
                    break



    for i in range(7- gyou +1):
        if i==0:
            if retsu - i == 0 or gyou + i == 7:
                break
            else:
                continue
        else:
            if retsu - i == 0:
                if ban[gyou + i][retsu - i] == after_c:
                    break
                else:
                    hidarisita = 0
                    break
            elif gyou + i == 7:
                if ban[gyou + i][retsu - i] == after_c:
                    break
                else:
                    hidarisita = 0
                    break
            else:
                if ban[gyou + i][retsu - i] == before_c:
                    hidarisita += 1
                elif ban[gyou + i][retsu - i] == after_c:
                    break
                else:
                    hidarisita = 0
                    break



    for i in range(gyou+1):
        if i==0:
            if retsu - i == 0 or gyou - i == 0:
                break
            else:
                continue
        else:
            if retsu - i == 0:
                if ban[gyou - i][retsu - i] == after_c:
                    break
                else:
                    hidariue = 0
                    break
            elif gyou - i == 0:
                if ban[gyou - i][retsu - i] == after_c:
                    break
                else:
                    hidariue = 0
                    break
            else:
                if ban[gyou - i][retsu - i] == before_c:
                    hidariue += 1
                elif ban[gyou - i][retsu - i] == after_c:
                    break
                else:
                    hidariue = 0
                    break

    scoreall = ue + migiue + migi + migisita + sita + hidarisita + hidari + hidariue
    return scoreall

def score_calc2(ban):
    score = score_initialize(30, 10, 7, 3, 0)
    for gyou in range(8):
        for retsu in range(8):
            if ban[gyou][retsu] == 1 or ban[gyou][retsu] == 2:
                score[gyou][retsu] -= 200000
            else:
                continue

    for gyou in range(8):
        for retsu in range(8):
            if score_count(ban, gyou, retsu, 2) > 0:
                score[gyou][retsu] += score_count(ban, gyou, retsu, 2)
            else:
                score[gyou][retsu] -= 200000

    global turns
    for gyou in range(8):
        for retsu in range(8):
            score[gyou][retsu] += abs(int(random.gauss(0, 10))) // int(pow((turns+1), 0.5))

    return score

def score_calc1(ban):
    score = score_initialize(30, 10, 5, 3, 0)
    for gyou in range(8):
        for retsu in range(8):
            if ban[gyou][retsu] == 1 or ban[gyou][retsu] == 2:
                score[gyou][retsu] -= 200000
            else:
                continue

    for gyou in range(8):
        for retsu in range(8):
            if score_count(ban, gyou, retsu, 1) > 0:
                score[gyou][retsu] += score_count(ban, gyou, retsu, 2)
            else:
                score[gyou][retsu] -= 200000

    global turns
    for gyou in range(8):
        for retsu in range(8):
            score[gyou][retsu] += abs(int(random.gauss(0, 10))) // int(pow((turns+1), 0.5))

    return score

def ban_incdec(teban, ban):
    #    12345678   22 2726252423              282930313233
    #9   oooooooo   21 o o o o o o o o    o o o o o o o o 38
    #10  oooooooo   20 o o o o o o o o    o o o o o o o o 37
    #11  oooooooo   19 o o o o o o o o    o o o o o o o o 36
    #12  oooooooo   18 o o o o o o o o    o o o o o o o o 35
    #13  oooooooo   17 o o o o o o o o    o o o o o o o o 34
    #14  oooooooo      o o o o o o o o    o o o o o o o o
    #15  oooooooo      o o o o o o o o    o o o o o o o o
    #16  oooooooo      o o o o o o o o    o o o o o o o o

    #38 data
    #(0,1) = 1, (0,2) = 2, (1,0) = -1, (1, 2) = 3, (2,0) = -2, (2,1) = -3
    incdec2d = [[teban + 1]]
    for i in range(8):
        incdec = [0]
        for k in range(7):
            if ban[i][k] == 0 and ban[i][k+1] == 1:
                incdec.append(1)
            if ban[i][k] == 0 and ban[i][k+1] == 2:
                incdec.append(2)
            if ban[i][k] == 1 and ban[i][k+1] == 0:
                incdec.append(-1)
            if ban[i][k] == 1 and ban[i][k+1] == 2:
                incdec.append(3)
            if ban[i][k] == 2 and ban[i][k+1] == 0:
                incdec.append(-2)
            if ban[i][k] == 2 and ban[i][k+1] == 1:
                incdec.append(-3)
        incdec2d.append(incdec)

    for i in range(8):
        incdec = [0]
        for k in range(7):
            if ban[k][i] == 0 and ban[k+1][i] == 1:
                incdec.append(1)
            if ban[k][i] == 0 and ban[k+1][i] == 2:
                incdec.append(2)
            if ban[k][i] == 1 and ban[k+1][i] == 0:
                incdec.append(-1)
            if ban[k][i] == 1 and ban[k+1][i] == 2:
                incdec.append(3)
            if ban[k][i] == 2 and ban[k+1][i] == 0:
                incdec.append(-2)
            if ban[k][i] == 2 and ban[k+1][i] == 1:
                incdec.append(-3)
        incdec2d.append(incdec)

    for i in range(5):
        incdec = [0]
        for k in range(i+2):
            if ban[5-i+k][k] == 0 and ban[6-i+k][k+1] == 1:
                incdec.append(1)
            if ban[5-i+k][k] == 0 and ban[6-i+k][k+1] == 2:
                incdec.append(2)
            if ban[5-i+k][k] == 1 and ban[6-i+k][k+1] == 0:
                incdec.append(-1)
            if ban[5-i+k][k] == 1 and ban[6-i+k][k+1] == 2:
                incdec.append(3)
            if ban[5-i+k][k] == 2 and ban[6-i+k][k+1] == 0:
                incdec.append(-2)
            if ban[5-i+k][k] == 2 and ban[6-i+k][k+1] == 1:
                incdec.append(-3)
        incdec2d.append(incdec)

    incdec = [0]
    for k in range(7):
        if ban[k][k] == 0 and ban[k+1][k+1] == 1:
            incdec.append(1)
        if ban[k][k] == 0 and ban[k+1][k+1] == 2:
            incdec.append(2)
        if ban[k][k] == 1 and ban[k+1][k+1] == 0:
            incdec.append(-1)
        if ban[k][k] == 1 and ban[k+1][k+1] == 2:
            incdec.append(3)
        if ban[k][k] == 2 and ban[k+1][k+1] == 0:
            incdec.append(-2)
        if ban[k][k] == 2 and ban[k+1][k+1] == 1:
            incdec.append(-3)
    incdec2d.append(incdec)

    for i in range(5):
        incdec = [0]
        for k in range(i+2):
            if ban[k][5-i+k] == 0 and ban[k+1][6-i+k] == 1:
                incdec.append(1)
            if ban[k][5-i+k] == 0 and ban[k+1][6-i+k] == 2:
                incdec.append(2)
            if ban[k][5-i+k] == 1 and ban[k+1][6-i+k] == 0:
                incdec.append(-1)
            if ban[k][5-i+k] == 1 and ban[k+1][6-i+k] == 2:
                incdec.append(3)
            if ban[k][5-i+k] == 2 and ban[k+1][6-i+k] == 0:
                incdec.append(-2)
            if ban[k][5-i+k] == 2 and ban[k+1][6-i+k] == 1:
                incdec.append(-3)
        incdec2d.append(incdec)
    for i in range(5):
        incdec = [0]
        for k in range(i+2):
            if ban[k][2+i-k] == 0 and ban[k+1][1+i-k] == 1:
                incdec.append(1)
            if ban[k][2+i-k] == 0 and ban[k+1][1+i-k] == 2:
                incdec.append(2)
            if ban[k][2+i-k] == 1 and ban[k+1][1+i-k] == 0:
                incdec.append(-1)
            if ban[k][2+i-k] == 1 and ban[k+1][1+i-k] == 2:
                incdec.append(3)
            if ban[k][2+i-k] == 2 and ban[k+1][1+i-k] == 0:
                incdec.append(-2)
            if ban[k][2+i-k] == 2 and ban[k+1][1+i-k] == 1:
                incdec.append(-3)
        incdec2d.append(incdec)

    incdec = [0]
    for k in range(7):
        if ban[k][7-k] == 0 and ban[k+1][7-(k+1)] == 1:
            incdec.append(1)
        if ban[k][7-k] == 0 and ban[k+1][7-(k+1)] == 2:
            incdec.append(2)
        if ban[k][7-k] == 1 and ban[k+1][7-(k+1)] == 0:
            incdec.append(-1)
        if ban[k][7-k] == 1 and ban[k+1][7-(k+1)] == 2:
            incdec.append(3)
        if ban[k][7-k] == 2 and ban[k+1][7-(k+1)] == 0:
            incdec.append(-2)
        if ban[k][7-k] == 2 and ban[k+1][7-(k+1)] == 1:
            incdec.append(-3)
    incdec2d.append(incdec)

    for i in range(5):
        incdec = [0]
        for k in range(i+2):
            if ban[5-i+k][7-k] == 0 and ban[6-i+k][7-(k+1)] == 1:
                incdec.append(1)
            if ban[5-i+k][7-k] == 0 and ban[6-i+k][7-(k+1)] == 2:
                incdec.append(2)
            if ban[5-i+k][7-k] == 1 and ban[6-i+k][7-(k+1)] == 0:
                incdec.append(-1)
            if ban[5-i+k][7-k] == 1 and ban[6-i+k][7-(k+1)] == 2:
                incdec.append(3)
            if ban[5-i+k][7-k] == 2 and ban[6-i+k][7-(k+1)] == 0:
                incdec.append(-2)
            if ban[5-i+k][7-k] == 2 and ban[6-i+k][7-(k+1)] == 1:
                incdec.append(-3)
        incdec2d.append(incdec)
    return incdec2d

def save_incdec2d(teban, ban, filename, data):
    #f = open(filename, "a")
    data.append(ban_incdec(teban, ban))
    #writer = csv.writer(f)
    #writer.writerows(data)
    #f.close()
    #print(ban_incdec(teban, ban))
def score_learning(ban, color):
    #score = [[0,0,0,0,0,0,0,0],
    #[0,0,0,0,0,0,0,0],
    #[0,0,0,0,0,0,0,0],
    #[0,0,0,0,0,0,0,0],
    #[0,0,0,0,0,0,0,0],
    #[0,0,0,0,0,0,0,0],
    #[0,0,0,0,0,0,0,0],
    #[0,0,0,0,0,0,0,0]]

    score = score_initialize(30, 10, 5, 3, 0)


    for gyou in range(8):
        for retsu in range(8):

            if ban[gyou][retsu] == 1 or ban[gyou][retsu] == 2:
                score[gyou][retsu] -= 200000
                #error is not here

            if score_count(ban, gyou, retsu, 2) > 0:
                kasou_ban = [[0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0]]
                for i in range(8):
                    for k in range(8):
                        kasou_ban[i][k] = ban[i][k]
                #print(kasou_ban)
                kasou_ban[gyou][retsu] = color

                #print(ban)
                thisincdec2d = ban_incdec(0, kasou_ban)
                thisincdec2d = thisincdec2d[1:len(thisincdec2d)]
                #print(len(thisincdec2d))
                for i in range(len(thisincdec2d)):
                    for j in range(len(thisincdec2d[i])):
                        thisincdec2d[i][j] = str(thisincdec2d[i][j])


                for kaiseki in range(38):
                    filename2 = "data_learn/line{}.csv".format(str(kaiseki + 1))
                    linei = []
                    linei2 = []
                    with open(filename2, "r") as f2:
                        rows = csv.reader(f2)
                        for row in rows:
                            #print(row)
                            linei.append(row)
                            linei2.append(row[1:len(row)])

                    for m in range(len(linei2)):
                        #print(linei2[m])
                        #print("xxx")
                        #print(thisincdec2d[kaiseki])
                        if linei2[m] == thisincdec2d[kaiseki]:
                            if len(linei2[m]) == 0:
                                score[gyou][retsu] += 0
                            else:
                                a = int(math.log(int(linei[m][0]), 10))
                                score[gyou][retsu] += a
                                print(a)
                            break

            else:
                #print(score)
                score[gyou][retsu] -= 200000
                #print(gyou,",",retsu)
    #print(score)
    return score

def cpu_placestone2(ban):
    global owaru1
    global owaru2
    bestscorex = -1
    bestscorey = -1
    bestscore = -1
    score = score_calc2(ban)
    #score = score_learning(ban, 2)

    for gyou in range(8):
        for retsu in range(8):
            if bestscore < score[gyou][retsu]:
                bestscore = score[gyou][retsu]
                bestscorex = gyou
                bestscorey = retsu
    if bestscorex >= 0:

        #print("cpu:"," ", bestscorex, ",", bestscorey)
        ban = ban_placestone(ban, bestscorex, bestscorey, 2)
        owaru1 = False
        owaru2 = False
    else:
        print("cpupass")
        global turns
        turns -= 1
        #global owaru2
        owaru2 = True
    return ban

def cpu_placestone1(ban):
    global owaru1
    global owaru2
    bestscorex = -1
    bestscorey = -1
    bestscore = -1
    score = score_calc1(ban)

    for gyou in range(8):
        for retsu in range(8):
            if bestscore < score[gyou][retsu]:
                bestscore = score[gyou][retsu]
                bestscorex = gyou
                bestscorey = retsu
    if bestscorex >= 0:

        #print("cpu:"," ", bestscorex, ",", bestscorey)
        ban = ban_placestone(ban, bestscorex, bestscorey, 1)
        owaru1 = False
        owaru2 = False
    else:
        #print("cpupass")
        global turns
        turns -= 1
        #global owaru1
        owaru1 = True
    return ban

def player_placestone(ban, gyou, retsu):
    global owaru1
    global owaru2
    print(gyou, ",", retsu)
    if score_count(ban, gyou, retsu, 1) < 1 or ban[gyou][retsu] > 0:
        if ban[gyou][retsu]>0:
            print("Yes")
        print("playerpass")
        global turns
        turns -= 1
    else:
        ban = ban_placestone(ban, gyou, retsu, 1)
        owaru1 = False
        owaru2 = False
    return ban

def winner(ban):
    player = 0
    cpu = 0
    for gyou in range(8):
        for retsu in range(8):
            if ban[gyou][retsu] == 1:
                player += 1

    for gyou in range(8):
        for retsu in range(8):
            if ban[gyou][retsu] == 2:
                cpu += 1
    #if player > cpu:
        #print("Winner:", "player")
    #elif player < cpu:
        #print("Winner:", "cpu")
    #else:
        #print("Draw")
    #print("score:")
    return player-cpu

def winner_print(ban):
    player = 0
    cpu = 0
    for gyou in range(8):
        for retsu in range(8):
            if ban[gyou][retsu] == 1:
                player += 1

    for gyou in range(8):
        for retsu in range(8):
            if ban[gyou][retsu] == 2:
                cpu += 1
    if player > cpu:
        print("Winner:", "player")
    elif player < cpu:
        print("Winner:", "cpu")
    else:
        print("Draw")
    print("score:")
    return player-cpu

#main program from here
#suuji = 8
suuji = input("save file number:")
for kaisuu in range(10):
    data = []
    tkgui = Tkgui()
    turns = 0
    teban = 0
    gyoudayo = 0
    retudayo = 0
    owaru1 = False
    owaru2 = False
    ban = [ [0] * 8 for i in range(8)]
    ban = osero_initialize(ban)
    tkgui.ban_image(ban)
    a=5
    #a = input("time control:")
 
    filename = "oserou_log_learn/oserou_log_learn_incdec{}.csv".format(str(suuji))

    while turns < 60:
        if owaru1 == False or owaru2 == False:
            #time.sleep(0.001)
            if teban // 2 * 2 == teban:
                ban = cpu_placestone1(ban)
                #save_incdec2d(teban, ban, filename, data)
                teban += 1
                turns += 1
                tkgui.ban_image(ban)

            else:

                ban = cpu_placestone2(ban)
                save_incdec2d(teban, ban, filename, data)
                teban += 1
                turns += 1
                tkgui.ban_image(ban)
        else:
            break

    #ban[gyou][retsu]

    print(winner_print(ban))
    teban = 0
    if winner(ban) < 0:
        f = open(filename, "a")
        writer = csv.writer(f)
        for l in range(len(data)):
            writer.writerows(data[l])
        f.close()

    data = []

    #tkgui.ban_image(ban)


# koko kara save


#filename = "oserou_log/incdectest.csv"
ik = 0
with open(filename, "r") as f2:
    lines = csv.reader(f2)
    for line in lines:
        if ik % 39 == 0:
            #print(line)
            ik += 1
            continue
        else:
            ifilename2 = "data_learn/line{}.csv".format(ik % 39)
            iline = []
            iline2 = []
            with open(ifilename2, "r") as if2:
                irows = csv.reader(if2)

                for irow in irows:
                    #print(row)
                    iline.append(irow)
                    iline2.append(irow[1:len(irow)])

            for im in range(len(iline2)):
                if iline2[im] == line[1:len(line)]:
                    if len(line[1:len(line)]) == 0:
                        break
                    else:
                        ia = int(iline[im][0])
                        ia += 1
                        iline[im][0] = str(ia)
                        break

                if im == len(iline2) - 1:
                    iline.append(line)
                    iline2.append(line[1:len(line)])

            if2 = open(ifilename2, "w")
            iwriter = csv.writer(if2)
            iwriter.writerows(iline)
            if2.close()
            ik += 1
print("Learning done. Updated file is :")
print(filename)
