import turtle

def do_move(turt, move):
    if move == 'f':
        turt.forward(15)
    elif move == 'b':
        turt.backward(15)
    elif move == 'r':
        turt.right(90)
    elif move == 'l':
        turt.left(90)
    else:
        print("Invalid command:", move)

def tele_turtle(n):
    win = turtle.Screen()
    tele_t = turtle.Turtle()

    for i in range(n):
        move = input("Enter next move: ")
        do_move(tele_t, move)

    win.exitonclick()

if __name__ == "__main__":
    tele_turtle(10)
