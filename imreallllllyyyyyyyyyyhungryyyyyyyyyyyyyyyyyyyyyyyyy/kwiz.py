import pygame
import pgzrun

WIDTH = 871
HEIGHT = 649

skor = 0

kweztoincuontor = 0
cwostionz = []
qestionindaks = 0

kwestionboks = Rect(0,0,650,150)
kwestionboks.move_ip(20,100)

ansorboks1 = Rect(0,0,300,120)
ansorboks1.move_ip(20, 300)

ansorboks2 = Rect(0,0,300,120)
ansorboks2.move_ip(369, 300)

ansorboks3 = Rect(0,0,300,120)
ansorboks3.move_ip(20, 466)

ansorboks4 = Rect(0,0,300,120)
ansorboks4.move_ip(369, 466)

ansorbokses = [ansorboks1, ansorboks2, ansorboks3, ansorboks4]

zkipboks = Rect(0,0,120,300)
zkipboks.move_ip(710, 300)

DAteimerr = Rect(0,0,120,150)
DAteimerr.move_ip(710, 100)

hoelaatweleven = 10

def draw():
    screen.fill(color = (70, 130, 180))
    screen.draw.filled_rect(kwestionboks, "MistyRose3")
    for i in ansorbokses:
        screen.draw.filled_rect(i, "mistyrose3")
    screen.draw.filled_rect(zkipboks, "mistyrose3")
    screen.draw.filled_rect(DAteimerr, "mistyrose3")
    screen.draw.textbox(str(hoelaatweleven), DAteimerr, color = "gray1")
    screen.draw.textbox("Skip", zkipboks, color = "black", angle=-89)
    screen.draw.textbox(questiooooooooooooooooooooooooooooooooon[0].strip(), kwestionboks, color = "gray2")
    indexks = 1
    for e in ansorbokses:
        screen.draw.textbox(questiooooooooooooooooooooooooooooooooon[indexks].strip(), e, color = "gray3")
        indexks+=1

def update():
    pass



def icantreadsoiletdacomputerdoitforme():
    global cwostionz, kweztoincuontor
    uhhidklikeletscallitwaytolongofafiletoreadorsmthlikethat = open("kwestions.txt", "r")
    print(uhhidklikeletscallitwaytolongofafiletoreadorsmthlikethat)
    for e in uhhidklikeletscallitwaytolongofafiletoreadorsmthlikethat:
        cwostionz.append(e)
        kweztoincuontor+=1
    uhhidklikeletscallitwaytolongofafiletoreadorsmthlikethat.close()


icantreadsoiletdacomputerdoitforme()

print(cwostionz)

def tiemer():
    global hoelaatweleven
    if hoelaatweleven:
        hoelaatweleven-=1
    else:
        skillissue()

clock.schedule_interval(tiemer, 2)

def nakstqwastoin():
    global qestionindaks
    qestionindaks+=1
    return cwostionz.pop(0).split(",")

def skillissue():
    global questiooooooooooooooooooooooooooooooooon, skor
    message = f"skill issue\nfinal skor = {skor}"
    questiooooooooooooooooooooooooooooooooon = [message, "big skill issoe", "burito", "im hungry", "", 0]
    if skor==11:
        questiooooooooooooooooooooooooooooooooon = ["imagine getting 11/11 big skil issjoe", "im still hungry ngl", "just close the tab ur done with the quiz why u still here reading this, i mean ur rading this prob in the script now cuz it prob fell of the screen and u prob stole this script from github just to flex to ur friends that u are cool or smth but u are not cuz u stealing MY script, also btw while making this game i discoverd that it DOES all show in the box, also u MUST have stolen my script cuz like to who am i giving this? my mom? like she prob like plays it once and never opens it again so ye, STOP STEALING MY SCRIPTS", "", "", 0]


def on_mouse_down(pos):
    indaks = 1
    for e in ansorbokses:
        if e.collidepoint(pos):
            if indaks is int(questiooooooooooooooooooooooooooooooooon[5]):
                korektansor()
            else:
                skillissue()
            
        indaks+=1

def korektansor():
    global skor, questiooooooooooooooooooooooooooooooooon, hoelaatweleven
    skor = skor+1
    if cwostionz:
        questiooooooooooooooooooooooooooooooooon = nakstqwastoin()
    else:
        skillissue()
    hoelaatweleven=10





questiooooooooooooooooooooooooooooooooon = nakstqwastoin()

pgzrun.go()