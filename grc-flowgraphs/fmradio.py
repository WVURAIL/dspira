#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: FMRadio
# Author: Pranav
# Description: An FM radio with Coarse and Fine scrubbing
# Generated: Wed Jun 28 16:20:55 2017
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
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import osmosdr
import sip
import sys
import time


class fmradio(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "FMRadio")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("FMRadio")
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

        self.settings = Qt.QSettings("GNU Radio", "fmradio")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.center_freq = center_freq = 100.1e6
        self.volume_slider = volume_slider = 5
        self.samp_rate = samp_rate = 2.5e6
        self.channel_width = channel_width = 200e3
        self.channel_slider = channel_slider = center_freq

        ##################################################
        # Blocks
        ##################################################
        self._center_freq_range = Range(80e6, 120e6, 10, 100.1e6, 200)
        self._center_freq_win = RangeWidget(self._center_freq_range, self.set_center_freq, 'Center Frequency', "counter_slider", float)
        self.top_layout.addWidget(self._center_freq_win)
        self._volume_slider_range = Range(0, 200, 10, 5, 200)
        self._volume_slider_win = RangeWidget(self._volume_slider_range, self.set_volume_slider, 'Volume', "counter_slider", float)
        self.top_layout.addWidget(self._volume_slider_win)
        self._channel_slider_range = Range(center_freq-samp_rate/2+channel_width/2, center_freq+samp_rate/2-channel_width/2, 1000, center_freq, 200)
        self._channel_slider_win = RangeWidget(self._channel_slider_range, self.set_channel_slider, 'Fine tuning', "slider", float)
        self.top_layout.addWidget(self._channel_slider_win)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=12,
                decimation=5,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	center_freq, #fc
        	samp_rate, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        
        self.qtgui_sink_x_0.enable_rf_freq(True)
        
        
          
        self.qtgui_histogram_sink_x_0 = qtgui.histogram_sink_f(
        	1024,
        	500,
                -0.2,
                0.2,
        	"Audio",
        	1
        )
        
        self.qtgui_histogram_sink_x_0.set_update_time(0.10)
        self.qtgui_histogram_sink_x_0.enable_autoscale(True)
        self.qtgui_histogram_sink_x_0.enable_accumulate(False)
        self.qtgui_histogram_sink_x_0.enable_grid(True)
        self.qtgui_histogram_sink_x_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_histogram_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_histogram_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_histogram_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_histogram_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_histogram_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_histogram_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_histogram_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_histogram_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_histogram_sink_x_0_win = sip.wrapinstance(self.qtgui_histogram_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_histogram_sink_x_0_win)
          
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + 'airspy=0' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(center_freq, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(50, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)
          
        self.low_pass_filter_0 = filter.fir_filter_ccf(12, firdes.low_pass(
        	1, samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume_slider, ))
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_wfm_rcv_0 = analog.wfm_rcv(
        	quad_rate=480,
        	audio_decimation=10,
        )
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq-channel_slider, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.analog_wfm_rcv_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_histogram_sink_x_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.qtgui_sink_x_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.rational_resampler_xxx_0, 0))    
        self.connect((self.osmosdr_source_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.rational_resampler_xxx_0, 0), (self.analog_wfm_rcv_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fmradio")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.set_channel_slider(self.center_freq)
        self.qtgui_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)
        self.osmosdr_source_0.set_center_freq(self.center_freq, 0)
        self.analog_sig_source_x_0.set_frequency(self.center_freq-self.channel_slider)

    def get_volume_slider(self):
        return self.volume_slider

    def set_volume_slider(self, volume_slider):
        self.volume_slider = volume_slider
        self.blocks_multiply_const_vxx_0.set_k((self.volume_slider, ))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 75e3, 25e3, firdes.WIN_HAMMING, 6.76))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

    def get_channel_width(self):
        return self.channel_width

    def set_channel_width(self, channel_width):
        self.channel_width = channel_width

    def get_channel_slider(self):
        return self.channel_slider

    def set_channel_slider(self, channel_slider):
        self.channel_slider = channel_slider
        self.analog_sig_source_x_0.set_frequency(self.center_freq-self.channel_slider)


def main(top_block_cls=fmradio, options=None):

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
