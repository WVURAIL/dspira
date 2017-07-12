# A Radio Telescope

You now have the tools necessary to create the digital signal processing for a Spectrometer for a radio telescope.  A spectrometer:

1.  Separates the incoming radio signal into individual frequency components (breaks it into individual cosine wave amplitudes and phases at each frequency)
2.  Measures the power in each of the cosine waves.
3.  Integrates (Averages) to get get a more precise measurement of the power at each frequency.

Use GnuRadio to create the signal processing chain to achieve this.  
Use an osmocom airspy source.  Use an FFT to separate frequency components.  This can be improved further by either windowing the FFT, or using a poly-phase filter bank to improve separating frequencies.

Convert to power and integrate using the appropriate blocks.

Initially, output to a vector sink to see the output spectrum.  Add a file sink to save the data.

switch over to using the hdf5 file sink from the gr-radio_astro repository.  This will require installing an out-of-tree module.    