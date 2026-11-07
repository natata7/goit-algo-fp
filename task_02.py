import turtle

def draw_pythagoras_tree(branch_len: float, level: int, angle: float = 45):
    if level == 0:
        return

    turtle.forward(branch_len)

    turtle.left(angle)
    draw_pythagoras_tree(branch_len * 0.7, level - 1, angle)

    turtle.right(2 * angle)
    draw_pythagoras_tree(branch_len * 0.7, level - 1, angle)

    turtle.left(angle)
    turtle.backward(branch_len)


def main():
    try:
        recursion_level = int(
            input("Введіть рівень рекурсії: ")
        )
        if recursion_level < 0:
            print("Рівень рекурсії має бути невід'ємним числом.")
            return
    except ValueError:
        print("Введіть ціле число.")
        return

    screen = turtle.Screen()
    screen.setup(width=800, height=700)
    screen.bgcolor("white")

    turtle.speed("fastest")
    turtle.color("forestgreen")

    turtle.left(90)
    turtle.penup()
    turtle.goto(0, -250)
    turtle.pendown()

    initial_length = 100
    draw_pythagoras_tree(initial_length, recursion_level)
    screen.exitonclick()


if __name__ == "__main__":
    main()

