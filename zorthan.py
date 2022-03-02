import random
import turtle
import time
import math

sorte = [
    'Tudo começa a dar certo, quando deixa de dar errado', 
    'Nenhum obstáculo é grande demais para quem desiste', 
    'Sem lutas não há derrotas!', 
    'Você não pode mudar seu passado, mas pode estragar seu futuro!', 
    'Lute como nunca, perca como sempre',
    'Não sabendo que era impossível, corra atrás e saiba',
    'Nada é tão horrível que não possa piorar muito',
    'Se alguém te ofendeu sem você merecer, volte lá e mereça!',
    'Você é mais fraco do que pensa',
    'O caminho é longo, mas a derrota é certa']
zguess = random.choice(sorte)

wn = turtle.Screen()
wn.title('curse101')
wn.bgcolor('black')
curse1 = turtle.Turtle()
curse1.hideturtle()
curse1.speed(0)
curse1.color('red')
rotate=int(360)
def drawCircles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def drawSpecial(t,size,repeat):
  for i in range (repeat):
    drawCircles(t,size)
    t.right(360/repeat)
drawSpecial(curse1,100,10)
curse2 = turtle.Turtle()
curse2.hideturtle()
curse2.speed(0)
curse2.color('yellow')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(curse2,100,10)
curse3 = turtle.Turtle()
curse3.hideturtle()
curse3.speed(0)
curse3.color('white')
rotate=int(80)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(curse3,100,10)
curse4 = turtle.Turtle()
curse4.hideturtle()
curse4.speed(0)
curse4.color('blue')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-19
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(curse4,100,10)
curse5 = turtle.Turtle()
curse5.hideturtle()
curse5.speed(0)
curse5.color('orange')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-20
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(curse5,100,10)


presentation = 'Bem-vindo mortal!!Eu sou Zorthan, Seu último biscoito da sorte!!'
t1 = turtle.Turtle()
t1.hideturtle()
t1.setposition(0, 260)
fontcolor=t1.color('white')
t1.write(presentation, font=("Arial", 12, "bold"), align="center")

time.sleep(2)
t1.clear()
presentation2 = 'Leia sua sorte agora e ilumine sua vida!!'
t2 = turtle.Turtle()
t2.hideturtle()
t2.setposition(0, 260)
fontcolor=t2.color('white')
t2.write(presentation2, font=("Arial", 12, "bold"), align="center")

time.sleep(2)
t2.clear()
presentation3 = 'Seu pedaço de sabedoria cósmica de hoje é:'
t3 = turtle.Turtle()
t3.hideturtle()
t3.setposition(0, 260)
fontcolor=t3.color('white')
t3.write(presentation3, font=("Arial", 12, "bold"), align="center")

time.sleep(2)
t3.clear()
presentation4 = zguess
t4 = turtle.Turtle()
t4.hideturtle()
t4.setposition(0, 260)
fontcolor=t4.color('white')
t4.write(presentation4, font=("Arial", 15, "bold"), align="center")

time.sleep(5)
t4.clear()

