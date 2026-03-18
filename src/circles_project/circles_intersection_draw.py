def draw_data(circle_1, circle_2):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()  # připravení okna pro vykreslení

    circle = plt.Circle((0, 0), 2, fill=False, color="blue")  # vytvoření kružnice
    ax.add_patch(circle)  # přidání kružnice do okna

    ax.set_xlim(-5, 5)  # nastavení rozsahu os, aby bylo vidět celý graf
    ax.set_ylim(-5, 5)

    ax.set_aspect("equal")  # nastavení stejného poměru os, aby kružnice vypadala jako kruh
    plt.show()  # zobrazení okna s kružnicí

circle_1 = {"x": 8, "y": 3, "r": 2}
circle_2 = {"x": 3, "y": 6, "r": 10}
print(draw_data(circle_1, circle_2))