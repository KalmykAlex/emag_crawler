import os
import csv
import matplotlib.pyplot as plt


BASEDIR = 'echipamente'

ITEM_TYPE = ['laptopuri',
             'monitoare-lcd-led',
             'scaune-gaming',
             'telefoane-mobile',
             'televizoare'
             ]


def item_price_graph(link, type):
    filenames = os.listdir(BASEDIR + '/' + type)
    y_price = list()
    x_time = list()

    for file in filenames:
        relative_path = '/'.join([BASEDIR, type, file])
        with open(relative_path) as csvfile:
            csv_reader = csv.reader(csvfile)

            for row in csv_reader:
                if link in row:
                    y_price.append(float(row[1]))
                    x_time.append(file.split('.')[0])

    plt.plot(x_time, y_price)
    plt.gcf().autofmt_xdate()
    plt.show()


# TODO: multiple items price evolution grapth visualisation

# TODO: moving avarage overlapping traces for different graphs