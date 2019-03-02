import plotly.offline as offline
import plotly.graph_objs as go

class Plotter(object):
    """Handle plotting for GUIs"""

    def __init__(self, pList, htmlFile, autoOpen = False):
        """Bubble plots for now"""
        xAxis = []
        yAxis = []
        for p in pList:
            yAxis.append(p[0])
            if type(p[1]) == int:
                xAxis.append('_' + str(p[1]))
            else:
                xAxis.append(p[1])
        trace0 = go.Scatter(x = xAxis,
                            y = yAxis,
                            mode = 'markers',
                            marker = dict(size = yAxis,
                                          sizemode = 'area',
                                          sizeref = 2.*max(yAxis)/(40.**2),                                            sizemin = 4
                                          )
                            )
        data = [trace0]
        offline.plot(data, filename = htmlFile, auto_open = autoOpen)
