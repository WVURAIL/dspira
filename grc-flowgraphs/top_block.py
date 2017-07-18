#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Jul 13 16:39:50 2017
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
from gnuradio import fft
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
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
        self.fftsize = fftsize = 1024*4

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_vector_sink_f_0_1 = qtgui.vector_sink_f(
            fftsize,
            0,
            1.0,
            "x-Axis",
            "y-Axis",
            "REAL sine delay",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0_1.set_update_time(0.10)
        self.qtgui_vector_sink_f_0_1.set_y_axis(-140, 10)
        self.qtgui_vector_sink_f_0_1.enable_autoscale(True)
        self.qtgui_vector_sink_f_0_1.enable_grid(False)
        self.qtgui_vector_sink_f_0_1.set_x_axis_units("")
        self.qtgui_vector_sink_f_0_1.set_y_axis_units("")
        self.qtgui_vector_sink_f_0_1.set_ref_level(0)
        
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
                self.qtgui_vector_sink_f_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0_1.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0_1.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0_1.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_vector_sink_f_0_1_win = sip.wrapinstance(self.qtgui_vector_sink_f_0_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_vector_sink_f_0_1_win)
        self.qtgui_vector_sink_f_0_0_1 = qtgui.vector_sink_f(
            fftsize,
            0,
            1.0,
            "x-Axis",
            "y-Axis",
            "IMAGINARY sine delay",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0_0_1.set_update_time(0.10)
        self.qtgui_vector_sink_f_0_0_1.set_y_axis(-140, 10)
        self.qtgui_vector_sink_f_0_0_1.enable_autoscale(True)
        self.qtgui_vector_sink_f_0_0_1.enable_grid(False)
        self.qtgui_vector_sink_f_0_0_1.set_x_axis_units("")
        self.qtgui_vector_sink_f_0_0_1.set_y_axis_units("")
        self.qtgui_vector_sink_f_0_0_1.set_ref_level(0)
        
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
                self.qtgui_vector_sink_f_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0_0_1.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0_0_1.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0_0_1.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_vector_sink_f_0_0_1_win = sip.wrapinstance(self.qtgui_vector_sink_f_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_vector_sink_f_0_0_1_win)
        self.qtgui_vector_sink_f_0_0_0_0_0_0 = qtgui.vector_sink_f(
            fftsize,
            0,
            1.0,
            "x-Axis",
            "y-Axis",
            "covolution",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0_0_0_0_0_0.set_y_axis(-140, 10)
        self.qtgui_vector_sink_f_0_0_0_0_0_0.enable_autoscale(True)
        self.qtgui_vector_sink_f_0_0_0_0_0_0.enable_grid(True)
        self.qtgui_vector_sink_f_0_0_0_0_0_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0_0_0_0_0_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0_0_0_0_0_0.set_ref_level(0)
        
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
                self.qtgui_vector_sink_f_0_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0_0_0_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_vector_sink_f_0_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_vector_sink_f_0_0_0_0_0_0_win)
        self.qtgui_vector_sink_f_0_0_0_0_0 = qtgui.vector_sink_f(
            fftsize,
            0,
            1.0,
            "x-Axis",
            "y-Axis",
            "sine delay",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0_0_0_0_0.set_y_axis(-140, 10)
        self.qtgui_vector_sink_f_0_0_0_0_0.enable_autoscale(True)
        self.qtgui_vector_sink_f_0_0_0_0_0.enable_grid(True)
        self.qtgui_vector_sink_f_0_0_0_0_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0_0_0_0_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0_0_0_0_0.set_ref_level(0)
        
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
                self.qtgui_vector_sink_f_0_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0_0_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_vector_sink_f_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_vector_sink_f_0_0_0_0_0_win)
        self.qtgui_vector_sink_f_0_0_0_0 = qtgui.vector_sink_f(
            fftsize,
            0,
            1.0,
            "x-Axis",
            "y-Axis",
            "IMAGINAR",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0_0_0_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0_0_0_0.set_y_axis(-140, 10)
        self.qtgui_vector_sink_f_0_0_0_0.enable_autoscale(True)
        self.qtgui_vector_sink_f_0_0_0_0.enable_grid(True)
        self.qtgui_vector_sink_f_0_0_0_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0_0_0_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0_0_0_0.set_ref_level(0)
        
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
                self.qtgui_vector_sink_f_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_vector_sink_f_0_0_0_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_vector_sink_f_0_0_0_0_win)
        self.qtgui_vector_sink_f_0_0_0 = qtgui.vector_sink_f(
            fftsize,
            0,
            1.0,
            "x-Axis",
            "y-Axis",
            "IMAGINAR",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0_0_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0_0_0.set_y_axis(-140, 10)
        self.qtgui_vector_sink_f_0_0_0.enable_autoscale(True)
        self.qtgui_vector_sink_f_0_0_0.enable_grid(False)
        self.qtgui_vector_sink_f_0_0_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0_0_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0_0_0.set_ref_level(0)
        
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
                self.qtgui_vector_sink_f_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0_0_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0_0_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0_0_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_vector_sink_f_0_0_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_vector_sink_f_0_0_0_win)
        self.qtgui_vector_sink_f_0_0 = qtgui.vector_sink_f(
            fftsize,
            0,
            1.0,
            "x-Axis",
            "y-Axis",
            "IMAGINAR",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0_0.set_y_axis(-140, 10)
        self.qtgui_vector_sink_f_0_0.enable_autoscale(True)
        self.qtgui_vector_sink_f_0_0.enable_grid(False)
        self.qtgui_vector_sink_f_0_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0_0.set_ref_level(0)
        
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
                self.qtgui_vector_sink_f_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_vector_sink_f_0_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_vector_sink_f_0_0_win)
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            fftsize,
            0,
            1.0,
            "x-Axis",
            "y-Axis",
            "REAL",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(-140, 10)
        self.qtgui_vector_sink_f_0.enable_autoscale(True)
        self.qtgui_vector_sink_f_0.enable_grid(False)
        self.qtgui_vector_sink_f_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0.set_ref_level(0)
        
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
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_vector_sink_f_0_win)
        self.fft_vxx_0_0_1 = fft.fft_vfc(fftsize, True, (window.rectangular(fftsize)), 3)
        self.fft_vxx_0_0_0_0 = fft.fft_vcc(fftsize, False, (window.rectangular(fftsize)), True, 3)
        self.fft_vxx_0_0_0 = fft.fft_vcc(fftsize, True, (window.rectangular(fftsize)), True, 3)
        self.fft_vxx_0_0 = fft.fft_vcc(fftsize, True, (window.rectangular(fftsize)), True, 3)
        self.fft_vxx_0 = fft.fft_vcc(fftsize, True, (window.rectangular(fftsize)), True, 3)
        self.blocks_stream_to_vector_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fftsize)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_float*1, fftsize)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fftsize)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(fftsize)
        self.blocks_multiply_conjugate_cc_0_0_0 = blocks.multiply_conjugate_cc(fftsize)
        self.blocks_multiply_conjugate_cc_0_0 = blocks.multiply_conjugate_cc(fftsize)
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(fftsize)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 1)
        self.blocks_complex_to_real_0_1 = blocks.complex_to_real(fftsize)
        self.blocks_complex_to_real_0_0_0_0_0 = blocks.complex_to_real(fftsize)
        self.blocks_complex_to_real_0_0_0_0 = blocks.complex_to_real(fftsize)
        self.blocks_complex_to_real_0_0_0 = blocks.complex_to_real(fftsize)
        self.blocks_complex_to_real_0_0 = blocks.complex_to_real(fftsize)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(fftsize)
        self.blocks_complex_to_imag_0_0 = blocks.complex_to_imag(fftsize)
        self.blocks_complex_to_imag_0 = blocks.complex_to_imag(fftsize)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_SQR_WAVE, 500, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 100*fftsize/32000.0, 1, 0)
        self.analog_const_source_x_0 = analog.sig_source_c(0, analog.GR_CONST_WAVE, 0, 0, 1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_stream_to_vector_0, 0))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_delay_0, 0))    
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_stream_to_vector_0_0_0, 0))    
        self.connect((self.blocks_complex_to_imag_0, 0), (self.qtgui_vector_sink_f_0_0, 0))    
        self.connect((self.blocks_complex_to_imag_0_0, 0), (self.qtgui_vector_sink_f_0_0_1, 0))    
        self.connect((self.blocks_complex_to_real_0, 0), (self.qtgui_vector_sink_f_0, 0))    
        self.connect((self.blocks_complex_to_real_0_0, 0), (self.qtgui_vector_sink_f_0_0_0, 0))    
        self.connect((self.blocks_complex_to_real_0_0_0, 0), (self.qtgui_vector_sink_f_0_0_0_0, 0))    
        self.connect((self.blocks_complex_to_real_0_0_0_0, 0), (self.qtgui_vector_sink_f_0_0_0_0_0, 0))    
        self.connect((self.blocks_complex_to_real_0_0_0_0_0, 0), (self.qtgui_vector_sink_f_0_0_0_0_0_0, 0))    
        self.connect((self.blocks_complex_to_real_0_1, 0), (self.qtgui_vector_sink_f_0_1, 0))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_stream_to_vector_0_0, 0))    
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.blocks_complex_to_real_0_0, 0))    
        self.connect((self.blocks_multiply_conjugate_cc_0_0, 0), (self.blocks_complex_to_real_0_0_0, 0))    
        self.connect((self.blocks_multiply_conjugate_cc_0_0_0, 0), (self.blocks_complex_to_real_0_0_0_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.fft_vxx_0_0_0_0, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))    
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.fft_vxx_0_0_1, 0))    
        self.connect((self.blocks_stream_to_vector_0_0_0, 0), (self.fft_vxx_0_0_0, 0))    
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_imag_0, 0))    
        self.connect((self.fft_vxx_0, 0), (self.blocks_complex_to_real_0, 0))    
        self.connect((self.fft_vxx_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))    
        self.connect((self.fft_vxx_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))    
        self.connect((self.fft_vxx_0, 0), (self.fft_vxx_0_0, 0))    
        self.connect((self.fft_vxx_0_0, 0), (self.blocks_multiply_conjugate_cc_0_0, 0))    
        self.connect((self.fft_vxx_0_0, 0), (self.blocks_multiply_conjugate_cc_0_0, 1))    
        self.connect((self.fft_vxx_0_0_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.fft_vxx_0_0_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.fft_vxx_0_0_0_0, 0), (self.blocks_complex_to_real_0_0_0_0_0, 0))    
        self.connect((self.fft_vxx_0_0_1, 0), (self.blocks_complex_to_imag_0_0, 0))    
        self.connect((self.fft_vxx_0_0_1, 0), (self.blocks_complex_to_real_0_1, 0))    
        self.connect((self.fft_vxx_0_0_1, 0), (self.blocks_multiply_conjugate_cc_0_0_0, 0))    
        self.connect((self.fft_vxx_0_0_1, 0), (self.blocks_multiply_conjugate_cc_0_0_0, 1))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_fftsize(self):
        return self.fftsize

    def set_fftsize(self, fftsize):
        self.fftsize = fftsize
        self.analog_sig_source_x_0.set_frequency(100*self.fftsize/32000.0)


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
