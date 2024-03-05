import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import csv

filename = "data.csv"

plot_legend = "Average Generations"
plot_title = ""

x_label = "k"
y_label = "Average Generations"

spline = False
save = True

def read_csv():
    x = []
    y = []

    with open(filename,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(float(row[0]))
            y.append(float(row[1]))

    return x, y


def get_title_font_properties():
    return fm.FontProperties(fname='/Users/starikov/Library/Fonts/JosefinSans-Regular.ttf')


def get_font_properties():
    return fm.FontProperties(fname='/Users/starikov/Library/Fonts/JosefinSans-Light.ttf')


def make_spline(x, y):
    from scipy.interpolate import interp1d
    import numpy as np

    f = interp1d(x, y, kind='cubic', )
    xnew = np.linspace(min(x), max(x), num=len(x), endpoint=True)
    plt.plot(xnew, f(xnew), 'b-', label=plot_legend)


def main():
    fig, ax = plt.subplots()
    fig.set_size_inches((12, 5))

    x, y = read_csv()

    if not spline:
        ax.plot(x, y, 'b+', label=plot_legend)

    ax.set_xlabel(x_label, fontproperties=get_font_properties(), size=14)
    ax.set_ylabel(y_label, fontproperties=get_font_properties(), size=14)
    ax.set_title(plot_title, fontproperties=get_title_font_properties(), size=22)

    ax.set_xticklabels(plt.xticks()[0], fontproperties=get_font_properties())
    ax.set_yticklabels([round(float(y), 2) for y in plt.yticks()[0]], fontproperties=get_font_properties())

    ax.legend(prop=get_font_properties())
    ax.grid()

    if spline:
        make_spline(x, y)


    figure = plt.gcf()
    plt.draw()
    plt.show()

    if save:
        figure.savefig("{}.png".format("figure"), format='png', dpi=280)


if __name__ == '__main__':
    main()
