import turtle
import math

def draw_tree(t, length, angle, depth):
    if depth == 0:
        return

    t.forward(length)
    t.left(angle)

    draw_tree(t, length * 0.7, angle, depth - 1)

    t.right(2 * angle)

    draw_tree(t, length * 0.7, angle, depth - 1)

    t.left(angle)
    t.backward(length)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("brown")
    t.speed("fastest")

    # Позиціонування черепахи для початку малювання
    t.left(90)
    t.penup()
    t.goto(0, -300)
    t.pendown()

    # Параметри дерева
    depth = int(input("Введіть рівень рекурсії: "))
    length = 150  # Довжина основного стовбура
    angle = 30    # Кут нахилу гілок

    draw_tree(t, length, angle, depth)

    turtle.done()

if __name__ == "__main__":
    main()