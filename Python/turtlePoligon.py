import turtle
bob = turtle.Turtle()
nlati = int(input("Scrivi un numero "))
ang=360/nlati
bob.color('red', 'yellow')
bob.begin_fill()
while True:
    bob.forward(123)
    bob.left(ang)
    if abs(bob.pos()) < 1:
        break
bob.end_fill()