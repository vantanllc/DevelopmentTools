from inkscape.svg_to_png.get_png_from_svg import get_png_from_svg
from mock import patch, mock
import pytest

SVG_FILE_PATH = "a_valid_svg_file.svg"
OUTPUT_FILE_PATH = "expected_png_file.png"
INKSCAPE_COMMAND = "inkscape"
NO_GUI_FLAG = "-z"
OUTPUT_PNG_FLAG = "-e"

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


  def test_get_png_from_svg__given_svg_file__calls_inkscape_with_svg_file(self):
    status_code = get_png_from_svg(SVG_FILE_PATH, OUTPUT_FILE_PATH)
    self.subprocess.call.assert_called_with([mock.ANY, mock.ANY, mock.ANY, mock.ANY, SVG_FILE_PATH])
