#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Spectrometer
# Generated: Wed Jul 19 14:54:43 2017
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
from datetime import datetime
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from optparse import OptionParser
import numpy as np
import osmosdr
import radio_astro
import sip
import sys
import time


class spectrometer(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Spectrometer")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Spectrometer")
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

        self.settings = Qt.QSettings("GNU Radio", "spectrometer")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.vec_length = vec_length = 4096
        self.sinc_sample_locations = sinc_sample_locations = np.arange(-np.pi*4/2.0, np.pi*4/2.0, np.pi/vec_length)
        self.timenow = timenow = datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
        self.sinc = sinc = np.sinc(sinc_sample_locations/np.pi)
        self.prefix = prefix = "/home/dspradio/grc_data/"
        self.samp_rate = samp_rate = 10e6
        self.recfile = recfile = prefix + timenow + ".h5"
        self.integration_time = integration_time = 2
        self.freq = freq = 1.419e9
        self.display_integration = display_integration = 0.5
        self.custom_window = custom_window = sinc*np.hamming(4*vec_length)

        ##################################################
        # Blocks
        ##################################################
        self.radio_astro_hdf5_sink_0 = radio_astro.hdf5_sink(vec_length, recfile, 'AZ: 180, EL: 30', freq - samp_rate/2, samp_rate/vec_length, 'testing az el etc')
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            vec_length,
            freq - samp_rate/2,
            samp_rate/vec_length,
            "Frequency",
            "PSD",
            "Spectrum",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(0, 3000)
        self.qtgui_vector_sink_f_0.enable_autoscale(True)
        self.qtgui_vector_sink_f_0.enable_grid(True)
        self.qtgui_vector_sink_f_0.set_x_axis_units("Hz")
        self.qtgui_vector_sink_f_0.set_y_axis_units("arb")
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
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	vec_length, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(False)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        
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
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + 'airspy=0,bias=0,pack=0' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(20, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.fft_vxx_0 = fft.fft_vcc(vec_length, True, (window.rectangular(vec_length)), True, 1)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_float*1, vec_length)
        self.blocks_stream_to_vector_0_2 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, vec_length)
        self.blocks_stream_to_vector_0_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, vec_length)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, vec_length)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, vec_length)
        self.blocks_nlog10_ff_0_0 = blocks.nlog10_ff(10, vec_length, 0)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(10, 1, 0)
        self.blocks_multiply_const_vxx_0_2 = blocks.multiply_const_vcc((custom_window[-vec_length:]))
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_vcc((custom_window[2*vec_length:3*vec_length]))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vcc((custom_window[vec_length:2*vec_length]))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((custom_window[0:vec_length]))
        self.blocks_multiply_conjugate_cc_0 = blocks.multiply_conjugate_cc(vec_length)
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_integrate_xx_0_0 = blocks.integrate_ff(int(display_integration*samp_rate/vec_length), vec_length)
        self.blocks_integrate_xx_0 = blocks.integrate_ff(int((integration_time)*samp_rate/vec_length)/int(display_integration*samp_rate/vec_length), vec_length)
        self.blocks_delay_0_0_0_0 = blocks.delay(gr.sizeof_gr_complex*1, 3*vec_length)
        self.blocks_delay_0_0_0 = blocks.delay(gr.sizeof_gr_complex*1, 2*vec_length)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_gr_complex*1, vec_length)
        self.blocks_complex_to_real_0_0 = blocks.complex_to_real(vec_length)
        self.blocks_add_xx_0 = blocks.add_vcc(vec_length)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.qtgui_vector_sink_f_0, 'xval'), (self.blocks_message_debug_0, 'print'))    
        self.connect((self.blocks_add_xx_0, 0), (self.fft_vxx_0, 0))    
        self.connect((self.blocks_complex_to_real_0_0, 0), (self.blocks_integrate_xx_0_0, 0))    
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_stream_to_vector_0_0, 0))    
        self.connect((self.blocks_delay_0_0_0, 0), (self.blocks_stream_to_vector_0_2, 0))    
        self.connect((self.blocks_delay_0_0_0_0, 0), (self.blocks_stream_to_vector_0_1, 0))    
        self.connect((self.blocks_integrate_xx_0, 0), (self.blocks_vector_to_stream_0, 0))    
        self.connect((self.blocks_integrate_xx_0, 0), (self.radio_astro_hdf5_sink_0, 0))    
        self.connect((self.blocks_integrate_xx_0_0, 0), (self.blocks_integrate_xx_0, 0))    
        self.connect((self.blocks_integrate_xx_0_0, 0), (self.blocks_nlog10_ff_0_0, 0))    
        self.connect((self.blocks_multiply_conjugate_cc_0, 0), (self.blocks_complex_to_real_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 3))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_add_xx_0, 2))    
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_2, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_nlog10_ff_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_nlog10_ff_0_0, 0), (self.qtgui_vector_sink_f_0, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.blocks_multiply_const_vxx_0_2, 0))    
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.blocks_multiply_const_vxx_0_1, 0))    
        self.connect((self.blocks_stream_to_vector_0_1, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_stream_to_vector_0_2, 0), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_nlog10_ff_0, 0))    
        self.connect((self.fft_vxx_0, 0), (self.blocks_multiply_conjugate_cc_0, 0))    
        self.connect((self.fft_vxx_0, 0), (self.blocks_multiply_conjugate_cc_0, 1))    
        self.connect((self.osmosdr_source_0, 0), (self.blocks_delay_0_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.blocks_delay_0_0_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.blocks_delay_0_0_0_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.blocks_stream_to_vector_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "spectrometer")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_vec_length(self):
        return self.vec_length

    def set_vec_length(self, vec_length):
        self.vec_length = vec_length
        self.set_custom_window(self.sinc*np.hamming(4*self.vec_length))
        self.set_sinc_sample_locations(np.arange(-np.pi*4/2.0, np.pi*4/2.0, np.pi/self.vec_length))
        self.qtgui_vector_sink_f_0.set_x_axis(self.freq - self.samp_rate/2, self.samp_rate/self.vec_length)
        self.blocks_multiply_const_vxx_0_2.set_k((self.custom_window[-self.vec_length:]))
        self.blocks_multiply_const_vxx_0_1.set_k((self.custom_window[2*self.vec_length:3*self.vec_length]))
        self.blocks_multiply_const_vxx_0_0.set_k((self.custom_window[self.vec_length:2*self.vec_length]))
        self.blocks_multiply_const_vxx_0.set_k((self.custom_window[0:self.vec_length]))
        self.blocks_delay_0_0_0_0.set_dly(3*self.vec_length)
        self.blocks_delay_0_0_0.set_dly(2*self.vec_length)
        self.blocks_delay_0_0.set_dly(self.vec_length)

    def get_sinc_sample_locations(self):
        return self.sinc_sample_locations

    def set_sinc_sample_locations(self, sinc_sample_locations):
        self.sinc_sample_locations = sinc_sample_locations
        self.set_sinc(np.sinc(self.sinc_sample_locations/np.pi))

    def get_timenow(self):
        return self.timenow

    def set_timenow(self, timenow):
        self.timenow = timenow
        self.set_recfile(self.prefix + self.timenow + ".h5")

    def get_sinc(self):
        return self.sinc

    def set_sinc(self, sinc):
        self.sinc = sinc
        self.set_custom_window(self.sinc*np.hamming(4*self.vec_length))
        self.set_sinc(np.sinc(self.sinc_sample_locations/np.pi))

    def get_prefix(self):
        return self.prefix

    def set_prefix(self, prefix):
        self.prefix = prefix
        self.set_recfile(self.prefix + self.timenow + ".h5")

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_vector_sink_f_0.set_x_axis(self.freq - self.samp_rate/2, self.samp_rate/self.vec_length)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)

    def get_recfile(self):
        return self.recfile

    def set_recfile(self, recfile):
        self.recfile = recfile

    def get_integration_time(self):
        return self.integration_time

    def set_integration_time(self, integration_time):
        self.integration_time = integration_time

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.qtgui_vector_sink_f_0.set_x_axis(self.freq - self.samp_rate/2, self.samp_rate/self.vec_length)
        self.osmosdr_source_0.set_center_freq(self.freq, 0)

    def get_display_integration(self):
        return self.display_integration

    def set_display_integration(self, display_integration):
        self.display_integration = display_integration

    def get_custom_window(self):
        return self.custom_window

    def set_custom_window(self, custom_window):
        self.custom_window = custom_window
        self.blocks_multiply_const_vxx_0_2.set_k((self.custom_window[-self.vec_length:]))
        self.blocks_multiply_const_vxx_0_1.set_k((self.custom_window[2*self.vec_length:3*self.vec_length]))
        self.blocks_multiply_const_vxx_0_0.set_k((self.custom_window[self.vec_length:2*self.vec_length]))
        self.blocks_multiply_const_vxx_0.set_k((self.custom_window[0:self.vec_length]))


def main(top_block_cls=spectrometer, options=None):

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
