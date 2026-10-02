"""Run the HDF5 converter against small, generated captures."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import h5py
import numpy as np


SCRIPT = Path(__file__).resolve().parents[1] / "python" / "hdf5_to_csv.py"


class ConverterTests(unittest.TestCase):
    def check_capture(self, channels):
        with tempfile.TemporaryDirectory() as folder:
            folder = Path(folder)
            capture = folder / "capture.h5"
            output = folder / "capture.csv"
            spectra = np.arange(3 * channels, dtype=float).reshape(3, channels)
            with h5py.File(capture, "w") as data:
                data.create_dataset("spectrum", data=spectra)
                data.attrs["freq_start"] = 1400e6
                data.attrs["freq_step"] = 1000.0
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "-f", str(capture), "-o", str(output)],
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            actual = np.loadtxt(output, delimiter=",")
            self.assertEqual(actual.shape, (channels, 4))
            np.testing.assert_array_equal(actual[:, 0], 1400e6 + np.arange(channels) * 1000)
            np.testing.assert_array_equal(actual[:, 1:], spectra.T)

    def test_nondefault_channel_count(self):
        self.check_capture(8)

    def test_historical_4096_channel_capture(self):
        self.check_capture(4096)


if __name__ == "__main__":
    unittest.main()
