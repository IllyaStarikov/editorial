import numpy
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import csv

#plot_legend = "Average Generations"
plot_title = "Gaussian Distribution (For Mutation)"

x_label = ""
y_label = ""

save = True

def function(x):
    from math import exp

    a_negative = .35
    a_positive = 1.0 - .35

    b_positive = 100
    b_negative = -100

    c = 3

    return a_negative*exp(-(x - b_negative)**2/(2 * c**2)) if x < 0 else \
        a_positive*exp(-(x - b_positive)**2/(2 * c**2))


def get_title_font_properties():
    return fm.FontProperties(fname='/Users/starikov/Library/Fonts/JosefinSans-Regular.ttf')


def get_font_properties():
    return fm.FontProperties(fname='/Users/starikov/Library/Fonts/JosefinSans-Light.ttf')


def main():
    fig, ax = plt.subplots()
    fig.set_size_inches((12, 5))

    x = numpy.linspace(-100, 100, 100000)
    y = [function(t) for t in x]

    plt.plot(x, y)

    y_labels = [item for item in plt.yticks()[0]]
    labels = [str(round(float(label), 2)) for label in y_labels]

    ax.set_xlabel(x_label, fontproperties=get_font_properties(), size=14)
    ax.set_ylabel(y_label, fontproperties=get_font_properties(), size=14)
    ax.set_title(plot_title, fontproperties=get_title_font_properties(), size=22)

    ax.set_xticklabels(plt.xticks()[0], fontproperties=get_font_properties())
    ax.set_yticklabels(labels, fontproperties=get_font_properties())

#    ax.legend(prop=get_font_properties())
    ax.grid()

    figure = plt.gcf()

    plt.draw()
    plt.show()

    if save:
        figure.savefig("{}.png".format("figure"), format='png', dpi=280)


if __name__ == '__main__':
    main()
