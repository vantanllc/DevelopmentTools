from inkscape.svg_to_png.get_png_from_svg import get_png_from_svg
from mock import patch, mock
import pytest

SVG_FILE_PATH = "a_valid_svg_file.svg"
OUTPUT_FILE_PATH = "expected_png_file.png"
INKSCAPE_COMMAND = "inkscape"
NO_GUI_FLAG = "-z"
OUTPUT_PNG_FLAG = "-e"
WIDTH_FLAG = "-w"
HEIGHT_FLAG = "-h"
DPI_FLAG = "-d"
DPI = "72"
EXPECTED_WIDTH = 100
EXPECTED_HEIGHT = 200

SUBPROCESS_IMPORT = "inkscape.svg_to_png.get_png_from_svg.subprocess"

class TestGetPngFromSvg(object):
  subprocess = None

  def setup_method(self):
    self.subprocess_patch = patch(SUBPROCESS_IMPORT)
    self.subprocess = self.subprocess_patch.start()

  def teardown_method(self):
    self.subprocess_patch.stop()


  def test_get_png_from_svg__given_svg_file_and_output_path__returns_success_code(self):
    self.subprocess.call.return_value = 0
    status_code = get_png_from_svg(SVG_FILE_PATH, OUTPUT_FILE_PATH)
    assert status_code == 0


  def test_get_png_from_svg__given_only_svg_file__returns_fail_code(self):
    status_code = get_png_from_svg(SVG_FILE_PATH, "")
    assert status_code == -1


  def test_get_png_from_svg__given_non_svg_file__returns_fail_code(self):
    non_svg_file = "music.mp3"
    status_code = get_png_from_svg(non_svg_file, "")
    assert status_code == -1


  def test_get_png_from_svg__given_svg_file_and_output_file_path__calls_inkscape(self):
    get_png_from_svg(SVG_FILE_PATH, OUTPUT_FILE_PATH)
    self.subprocess.call.assert_called_with([INKSCAPE_COMMAND, mock.ANY, mock.ANY, mock.ANY, mock.ANY, mock.ANY, mock.ANY])
  

  def test_get_png_from_svg__given_svg_file_and_output_file_path__calls_with_svg_file(self):
    get_png_from_svg(SVG_FILE_PATH, OUTPUT_FILE_PATH)
    self.subprocess.call.assert_called_with([mock.ANY, mock.ANY, mock.ANY, mock.ANY, SVG_FILE_PATH, mock.ANY, mock.ANY])


  def test_get_png_from_svg__given_svg_file_and_output_file_path__calls_with_output_file(self):
    get_png_from_svg(SVG_FILE_PATH, OUTPUT_FILE_PATH)
    self.subprocess.call.assert_called_with([mock.ANY, mock.ANY, mock.ANY, OUTPUT_FILE_PATH, mock.ANY, mock.ANY, mock.ANY])


  def test_get_png_from_svg__given_svg_file_and_output_file_path__calls_with_no_gui_flag(self):
    get_png_from_svg(SVG_FILE_PATH, OUTPUT_FILE_PATH)
    self.subprocess.call.assert_called_with([mock.ANY, NO_GUI_FLAG, mock.ANY, mock.ANY, mock.ANY, mock.ANY, mock.ANY])


  def test_get_png_from_svg__given_svg_file_and_output_file_path__calls_with_output_png_flag(self):
    get_png_from_svg(SVG_FILE_PATH, OUTPUT_FILE_PATH)
    self.subprocess.call.assert_called_with([mock.ANY, mock.ANY, OUTPUT_PNG_FLAG, mock.ANY, mock.ANY, mock.ANY, mock.ANY])


  def test_get_png_from_svg__given_svg_file_and_output_file_path__calls_with_dpi_flag_and_value(self):
    get_png_from_svg(SVG_FILE_PATH, OUTPUT_FILE_PATH)
    self.subprocess.call.assert_called_with([mock.ANY, mock.ANY, OUTPUT_PNG_FLAG, mock.ANY, mock.ANY, DPI_FLAG, DPI])


  def test_get_png_from_svg__given_width__calls_with_width_flag_and_value(self):
    get_png_from_svg(SVG_FILE_PATH, OUTPUT_FILE_PATH, EXPECTED_WIDTH)
    self.subprocess.call.assert_called_with([mock.ANY, mock.ANY, mock.ANY, mock.ANY, mock.ANY, mock.ANY, mock.ANY, WIDTH_FLAG, EXPECTED_WIDTH])


  def test_get_png_from_svg__given_height__calls_with_height_flag_and_value(self):
    get_png_from_svg(SVG_FILE_PATH, OUTPUT_FILE_PATH, None, EXPECTED_HEIGHT)
    self.subprocess.call.assert_called_with([mock.ANY, mock.ANY, mock.ANY, mock.ANY, mock.ANY, mock.ANY, mock.ANY, HEIGHT_FLAG, EXPECTED_HEIGHT])
