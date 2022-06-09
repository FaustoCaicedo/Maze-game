import math
import random
import turtle
import datetime as dt

current_datetime = dt.datetime.now()

#Window
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Odyssey")
wn.setup(800, 800)

# Register Shapes
turtle.register_shape("left_0.gif")
turtle.register_shape("right_0.gif")
turtle.register_shape("rock.gif")
turtle.register_shape("0.gif")
turtle.register_shape("15.gif")
turtle.register_shape("down_0.gif")
turtle.register_shape("up_0.gif")
turtle.register_shape("black.gif")


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)

#Nearsight
class Muro(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.shape(shape_1)
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

    def change_shape(self):
        self.shape(shape_2)

    def change_shape_again(self):
        self.shape(shape_1)


shape_1 = ("black.gif")
shape_2 = ("rock.gif")

#Player
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("right_0.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0

    #Move functions
    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        self.shape("up_0.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        self.shape("down_0.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        self.shape("left_0.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        self.shape("right_0.gif")

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_close_to(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 125:
            return True
        else:
            return False

    def is_far_away_from(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance > 125:
            return True
        else:
            return False

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False

#Enemy
class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("0.gif")
        self.color("red")
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])

    #Enemy move by itself
    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        elif self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0

        #Attack Player
        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() > self.xcor():
                self.direction = "right"
            elif player.ycor() < self.xcor():
                self.direction = "down"
            elif player.ycor() > self.ycor():
                self.direction = "up"

        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = random.choice(["up", "down", "left", "right"])

        turtle.ontimer(self.move, t=random.randint(100, 300))

    def is_close(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 50:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

#Treasure
class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("15.gif")
        self.color("green")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    #Destroys/Hide itseld when touched by player
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

#Level and possibilities for more levels
levels = [""]

level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XMMMMMMMMMMMMMMMMMMMMMMMMMX",
    "XMP    T              MMMMX",
    "XM  MXXXXXM  MMMMM T  MMMMX",
    "XM  MXXXXXM  MXXXM    MMMMX",
    "XM  MMMMMMM  MXXXM    MMMMX",
    "XM     E     MXXXM    MMMMX",
    "XMMMMMMM   MMXXXM      MMMX",
    "XXXXXXXM   MXXXXM   T  MMMX",
    "XMMMMMMM   MMXXXXXM  MMMMMX",
    "XM   MXM     MXXXXM  MMMMMX",
    "XM   MXM     MXXXXM  MMMMMX",
    "XM   MXM T   MMMMMMMMMMMMMX",
    "XM   MMM     MXXXXXXXXXXXXX",
    "XMM          MMMMMMMMMMMMMX",
    "XMMMMMMMMM   MXXXXMMXM   MX",
    "XMMMMMMMMM    MXXM  MM   MX",
    "XMMM   MMMMM  MMMMM  MM  MX",
    "XMMM                    EMX",
    "XMMM T        MMMMMMMMMMMMX",
    "XMMMMMMMMMM   MMMMMMMMMMMMX",
    "XMMMMMMMXXM              MX",
    "XXXM   MXXM       T      MX",
    "XXXMT  MMXXMMMMMMMMMM  MMMX",
    "XXXXMM   MMMMMXXXXXXM  MMMX",
    "XXXXXXM       MMMMMMM  MMMX",
    "XXXXXXXM  T        T     MX",
    "XMMMMMMMMMMMMMMMMMMMMMMMMMX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

muros = []
enemies = []
treasures = []

levels.append(level_1)

#Maze basic setup
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()

                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "M":
                muros.append(Muro(screen_x, screen_y))

                walls.append((screen_x, screen_y))

            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))

            if character == "E":
                enemies.append(Enemy(screen_x, screen_y))


pen = Pen()
player = Player()

walls = []

setup_maze(levels[1])
print(walls)

#Key Movement function
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

wn.tracer(0)

for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)

for enemy in enemies:
    if player.is_collision(enemy):
        print("You Died!")

#Nearsighted
while True:
    for muro in muros:
        if player.is_close_to(muro):
            muro.change_shape()

        if player.is_far_away_from(muro):
            muro.change_shape_again()

    #Player gold
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            print("Player Gold: {}".format(player.gold))

            treasure.destroy()
            treasures.remove(treasure)

    #Lose or win game
    for enemy in enemies:
        if player.is_collision(enemy):
            print("You Died!")
            exit()

        if player.gold == 900:
            print("You Win!")
            exit()

    #Save function and show gold/time
    gold = player.gold
    f = open("save.py", "w")
    f.write("gold = " + str(gold))
    f.write("\ncurrent_datetime = " + str(current_datetime))

    wn.update()
