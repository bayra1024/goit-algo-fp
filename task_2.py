import turtle


def draw_pyt_tree(branch_length, t, level):
    if level > 0:
        t.forward(branch_length)
        t.right(45)

        draw_pyt_tree(branch_length - 10, t, level - 1)

        t.left(90)
        draw_pyt_tree(branch_length - 10, t, level - 1)

        t.right(45)
        t.backward(branch_length)


level = int(input("Введіть рівень рекурсії: "))
turtle.speed(0)
turtle.left(90)
turtle.up()
turtle.backward(200)
turtle.down()

draw_pyt_tree(100, turtle, level)

turtle.exitonclick()
