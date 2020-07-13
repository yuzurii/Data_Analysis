import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the point in the walk.
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize = (10, 6))
    point_numbers = range(rw.num_points)
    #cmap=plt.cm.Blues, edgecolors='none', s=1
    ax.plot(rw.x_values, rw.y_values, c="pink")

    # Emphasize the first and last points.
    # edgecolors='none',  s=100
    ax.plot(0, 0, c='green')
    ax.plot(rw.x_values[-1], rw.y_values[-1], c='red')

    #Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break