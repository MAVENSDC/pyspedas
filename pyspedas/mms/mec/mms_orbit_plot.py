
import os
import matplotlib.pyplot as plt
from pytplot import get_data
from pyspedas import mms_load_mec

def mms_orbit_plot(trange=['2015-10-16', '2015-10-17'], probes=[1, 2, 3, 4], data_rate='srvy', xrange=None, yrange=None, plane='xy', coord='gse'):
    spacecraft_colors = [(0,0,0), (213/255,94/255,0), (0,158/255,115/255), (86/255,180/255,233/255)]

    mec_vars = mms_load_mec(trange=trange, data_rate=data_rate, probe=probes, varformat='*_r_' + coord, time_clip=True)

    if plane == 'xy':
        plt.xlabel('X Position, Re')
        plt.ylabel('Y Position, Re')
    elif plane == 'yz':
        plt.xlabel('Y Position, Re')
        plt.ylabel('Z Position, Re')
    elif plane == 'xz':
        plt.xlabel('X Position, Re')
        plt.ylabel('Z Position, Re')

    km_in_re = 6371.2

    plt.axes().set_aspect('equal')

    im = plt.imread(os.path.dirname(os.path.realpath(__file__)) + '/earth_polar1.png')
    plt.imshow(im, extent=(-1, 1, -1, 1))

    for probe in probes:
        t, d = get_data('mms' + str(probe) + '_mec_r_' + coord)
        if plane == 'xy':
            plt.plot(d[:, 0]/km_in_re, d[:, 1]/km_in_re, label='MMS' + str(probe), color=spacecraft_colors[int(probe)-1])
        if plane == 'yz':
            plt.plot(d[:, 1]/km_in_re, d[:, 2]/km_in_re, label='MMS' + str(probe), color=spacecraft_colors[int(probe)-1])
        if plane == 'xz':
            plt.plot(d[:, 0]/km_in_re, d[:, 2]/km_in_re, label='MMS' + str(probe), color=spacecraft_colors[int(probe)-1])

    plt.legend()
    plt.title(trange[0] + ' to ' + trange[1])
    plt.annotate(coord.upper() + ' coordinates', xy=(0.6, 0.05), xycoords='axes fraction')

    plt.show()

