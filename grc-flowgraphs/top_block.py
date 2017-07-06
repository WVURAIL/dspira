#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Jun 30 00:01:28 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import math
import sip
import sys


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.f = f = 500

        ##################################################
        # Blocks
        ##################################################
        self._f_range = Range(0, 1000, 10, 500, 200)
        self._f_win = RangeWidget(self._f_range, self.set_f, 'Frequency', "counter_slider", float)
        self.top_grid_layout.addWidget(self._f_win, 0,0,1,2)
        self.qtgui_time_sink_x_1_1_0_0_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"9 harmonics", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_1_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_1_0_0_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_1_1_0_0_0_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_1_1_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_1_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1_0_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_1_1_0_0_0_0.enable_grid(True)
        self.qtgui_time_sink_x_1_1_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_1_0_0_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_1_1_0_0_0_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_1_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_1_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1_0_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_1_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_1_0_0_0_0_win, 5,1,1,1)
        self.qtgui_time_sink_x_1_1_0_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"8 harmonics", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_1_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_1_0_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_1_1_0_0_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_1_1_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_1_1_0_0_0.enable_grid(True)
        self.qtgui_time_sink_x_1_1_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_1_0_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_1_1_0_0_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_1_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_1_0_0_0_win, 5,0,1,1)
        self.qtgui_time_sink_x_1_1_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"7 harmonics", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_1_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_1_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_1_1_0_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_1_1_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_1_1_0_0.enable_grid(True)
        self.qtgui_time_sink_x_1_1_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_1_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_1_1_0_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_1_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_1_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_1_0_0_win, 4,1,1,1)
        self.qtgui_time_sink_x_1_1_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"6 harmonics", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_1_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_1_1_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_1_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1_0.enable_autoscale(True)
        self.qtgui_time_sink_x_1_1_0.enable_grid(True)
        self.qtgui_time_sink_x_1_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_1_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_1_1_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_1_0_win, 4,0,1,1)
        self.qtgui_time_sink_x_1_1 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"5 harmonics", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1_1.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_1_1.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_1_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_1.enable_autoscale(True)
        self.qtgui_time_sink_x_1_1.enable_grid(True)
        self.qtgui_time_sink_x_1_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_1_1.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_1_win, 3,1,1,1)
        self.qtgui_time_sink_x_1_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"4 harmonics", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_1_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0.enable_autoscale(True)
        self.qtgui_time_sink_x_1_0.enable_grid(True)
        self.qtgui_time_sink_x_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_1_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_0_win, 3,0,1,1)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"3 harmonics", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(True)
        self.qtgui_time_sink_x_1.enable_grid(True)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_1.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_win, 2,1,1,1)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"2 harmonics", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(True)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win, 2,0,1,1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"Square Wave", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 1,0,1,2)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"FT or square Wave", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.blocks_throttle_0_5_0_0_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_5_0_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_5_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_5_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_5 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_4 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_3 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_2 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0_2 = blocks.multiply_const_vff((2/(3*math.pi), ))
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_vff((2/(5*math.pi), ))
        self.blocks_multiply_const_vxx_0_0_0_0_0_0 = blocks.multiply_const_vff((2/(15*math.pi), ))
        self.blocks_multiply_const_vxx_0_0_0_0_0 = blocks.multiply_const_vff((2/(13*math.pi), ))
        self.blocks_multiply_const_vxx_0_0_0_0 = blocks.multiply_const_vff((2/(11*math.pi), ))
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vff((2/(9*math.pi), ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vff((2/(7*math.pi), ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((2/math.pi, ))
        self.blocks_add_xx_0_3 = blocks.add_vff(1)
        self.blocks_add_xx_0_2 = blocks.add_vff(1)
        self.blocks_add_xx_0_1_0_0_0 = blocks.add_vff(1)
        self.blocks_add_xx_0_1_0_0 = blocks.add_vff(1)
        self.blocks_add_xx_0_1_0 = blocks.add_vff(1)
        self.blocks_add_xx_0_1 = blocks.add_vff(1)
        self.blocks_add_xx_0_0 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0_4 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, f*5, 1, 0)
        self.analog_sig_source_x_0_3_0_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, f*15, 1, 0)
        self.analog_sig_source_x_0_3_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, f*13, 1, 0)
        self.analog_sig_source_x_0_3_0_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, f*11, 1, 0)
        self.analog_sig_source_x_0_3_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, f*9, 1, 0)
        self.analog_sig_source_x_0_3 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, f*7, 1, 0)
        self.analog_sig_source_x_0_1_0 = analog.sig_source_f(samp_rate, analog.GR_SQR_WAVE, f, 1, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, f, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, f*3, 1, 0)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, 0.5)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_throttle_0_4, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0_3, 0))    
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_throttle_0_0, 0))    
        self.connect((self.analog_sig_source_x_0_1_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.analog_sig_source_x_0_3, 0), (self.blocks_throttle_0_5, 0))    
        self.connect((self.analog_sig_source_x_0_3_0, 0), (self.blocks_throttle_0_5_0, 0))    
        self.connect((self.analog_sig_source_x_0_3_0_0, 0), (self.blocks_throttle_0_5_0_0, 0))    
        self.connect((self.analog_sig_source_x_0_3_0_0_0, 0), (self.blocks_throttle_0_5_0_0_0, 0))    
        self.connect((self.analog_sig_source_x_0_3_0_0_0_0, 0), (self.blocks_throttle_0_5_0_0_0_0, 0))    
        self.connect((self.analog_sig_source_x_0_4, 0), (self.blocks_throttle_0_2, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_add_xx_0_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0_0, 0))    
        self.connect((self.blocks_add_xx_0_0, 0), (self.blocks_add_xx_0_2, 0))    
        self.connect((self.blocks_add_xx_0_0, 0), (self.qtgui_time_sink_x_1, 0))    
        self.connect((self.blocks_add_xx_0_1, 0), (self.blocks_add_xx_0_1_0, 0))    
        self.connect((self.blocks_add_xx_0_1, 0), (self.qtgui_time_sink_x_1_1_0, 0))    
        self.connect((self.blocks_add_xx_0_1_0, 0), (self.blocks_add_xx_0_1_0_0, 0))    
        self.connect((self.blocks_add_xx_0_1_0, 0), (self.qtgui_time_sink_x_1_1_0_0, 0))    
        self.connect((self.blocks_add_xx_0_1_0_0, 0), (self.blocks_add_xx_0_1_0_0_0, 0))    
        self.connect((self.blocks_add_xx_0_1_0_0, 0), (self.qtgui_time_sink_x_1_1_0_0_0, 0))    
        self.connect((self.blocks_add_xx_0_1_0_0_0, 0), (self.qtgui_time_sink_x_1_1_0_0_0_0, 0))    
        self.connect((self.blocks_add_xx_0_2, 0), (self.blocks_add_xx_0_3, 0))    
        self.connect((self.blocks_add_xx_0_2, 0), (self.qtgui_time_sink_x_1_0, 0))    
        self.connect((self.blocks_add_xx_0_3, 0), (self.blocks_add_xx_0_1, 0))    
        self.connect((self.blocks_add_xx_0_3, 0), (self.qtgui_time_sink_x_1_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0_3, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_add_xx_0_1, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0, 0), (self.blocks_add_xx_0_1_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0_0, 0), (self.blocks_add_xx_0_1_0_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0_0_0_0, 0), (self.blocks_add_xx_0_1_0_0_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_add_xx_0_2, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_2, 0), (self.blocks_add_xx_0_0, 1))    
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_throttle_0_2, 0), (self.blocks_multiply_const_vxx_0_1, 0))    
        self.connect((self.blocks_throttle_0_3, 0), (self.blocks_multiply_const_vxx_0_2, 0))    
        self.connect((self.blocks_throttle_0_4, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_throttle_0_5, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.blocks_throttle_0_5_0, 0), (self.blocks_multiply_const_vxx_0_0_0, 0))    
        self.connect((self.blocks_throttle_0_5_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0_0, 0))    
        self.connect((self.blocks_throttle_0_5_0_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0_0_0, 0))    
        self.connect((self.blocks_throttle_0_5_0_0_0_0, 0), (self.blocks_multiply_const_vxx_0_0_0_0_0_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_1_1_0_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_1_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_1_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.blocks_throttle_0_5_0_0_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_5_0_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_5_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_5_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_5.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_4.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_3.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_2.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0_4.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_3_0_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_3_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_3_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_3_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_3.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_f(self):
        return self.f

    def set_f(self, f):
        self.f = f
        self.analog_sig_source_x_0_4.set_frequency(self.f*5)
        self.analog_sig_source_x_0_3_0_0_0_0.set_frequency(self.f*15)
        self.analog_sig_source_x_0_3_0_0_0.set_frequency(self.f*13)
        self.analog_sig_source_x_0_3_0_0.set_frequency(self.f*11)
        self.analog_sig_source_x_0_3_0.set_frequency(self.f*9)
        self.analog_sig_source_x_0_3.set_frequency(self.f*7)
        self.analog_sig_source_x_0_1_0.set_frequency(self.f)
        self.analog_sig_source_x_0_1.set_frequency(self.f)
        self.analog_sig_source_x_0.set_frequency(self.f*3)


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
