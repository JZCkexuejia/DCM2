import numpy as np
from numpy import ndarray
from pyqtgraph import PlotDataItem, PlotWidget


# This class handles the graphs for the DCM
class GraphsHandler:
    _atri_data: ndarray
    _vent_data: ndarray
    _atri_plot: PlotDataItem
    _vent_plot: PlotDataItem

    def __init__(self, atri_plot: PlotWidget, vent_plot: PlotWidget):
        print("Graphs handler init")

        # noinspection PyArgumentList
        atri_plot.setRange(xRange=[-0.5, 10], yRange=[-0.1, 1.2], padding=0)
        atri_plot.setLimits(xMin=-0.5, yMin=-0.1, yMax=1.2)
        atri_plot.setMouseEnabled(x=True, y=False)
        atri_plot.setAutoVisible(x=False, y=True)
        atri_plot.showGrid(x=True, y=True)
        atri_plot.setMenuEnabled(False)
        atri_plot.setLabel('left', "Amplitude", units='V', **{'color': '#FFF', 'font-size': '10pt'})
        atri_plot.setLabel('bottom', "Time", units='s',**{'color': '#FFF', 'font-size': '8pt'})
        atri_plot.getAxis('bottom').setHeight(30)
        # noinspection PyArgumentList
        vent_plot.setRange(xRange=[-0.5, 10], yRange=[-0.1, 1.2], padding=0)
        vent_plot.setLimits(xMin=-0.5, yMin=-0.1, yMax=1.2)
        vent_plot.setMouseEnabled(x=True, y=False)
        vent_plot.setAutoVisible(x=False, y=True)
        vent_plot.showGrid(x=True, y=True)
        vent_plot.setMenuEnabled(False)
        vent_plot.setLabel('left', "Amplitude", units='V', **{'color': '#FFF', 'font-size': '10pt'})
        vent_plot.setLabel('bottom', "Time", units='s', **{'color': '#FFF', 'font-size': '8pt'})
        vent_plot.getAxis('bottom').setHeight(30)

        # Initialize graphs to 0
        self._atri_data = np.array([])
        self._vent_data = np.array([])
        self.index = 0
        # Create new sense plots for the atrial and ventricular graphs, in blue
        self._atri_plot = atri_plot.plot(pen=(0, 229, 255))
        self._vent_plot = vent_plot.plot(pen=(0, 229, 255))
        self._plot_data()

    # Plot the sense data on the graphs
    def _plot_data(self) -> None:
        time_period = 10
        atr_wid = self._atri_plot.getViewWidget()
        ven_wid = self._vent_plot.getViewWidget()
        atr_wid.disableAutoRange()
        ven_wid.disableAutoRange()
        if self.index <= 500:
            size = len(self._atri_data)
            x = np.arange(0, size) / time_period
            self._atri_plot.setData(x, self._atri_data)
            self._vent_plot.setData(x, self._vent_data)
            size = size/time_period
            if size % 5 == 0:
                atr_wid.setXRange(size-4,size+6)
                ven_wid.setXRange(size-4,size+6)
                atr_wid.enableAutoRange(x=False, y=True)
                ven_wid.enableAutoRange(x=False, y=True)
        else:
            x = np.arange(self.index - 500, self.index) / time_period
            self._atri_plot.setData(x, self._atri_data)
            self._vent_plot.setData(x, self._vent_data)
            position = self.index/time_period
            if position % 5 == 0:
                atr_wid.setXRange(position-4,position+6)
                ven_wid.setXRange(position-4,position+6)
                atr_wid.enableAutoRange(x=False, y=True)
                ven_wid.enableAutoRange(x=False, y=True)
        self.index = self.index + 1
        
    # Update and plot new received data
    def update_data(self, atri_data: float, vent_data: float):
        if self.index <= 500:
            self._atri_data = np.append(self._atri_data, atri_data)
            self._vent_data = np.append(self._vent_data, vent_data)
        else:
            self._atri_data = np.roll(self._atri_data, -1)
            self._vent_data = np.roll(self._vent_data, -1)
            self._atri_data[-1] = atri_data
            self._vent_data[-1] = vent_data
        self._plot_data()