from inkscape.svg_to_png.get_png_from_svg import get_png_from_svg
import os
from shutil import copyfile, rmtree
import pytest

class TestIntegrationGetPnyFromSvg(object):
  svg_test_dir = "/tmp/svg_test_dir"
  svg_file = "GrayBall.svg"
  png_file = "GrayBall.png"
  input_file = "{}/{}".format(svg_test_dir, svg_file)
  output_file = "{}/{}".format(svg_test_dir, png_file)

  def setup_method(self):
    cwd = os.getcwd()
    os.makedirs(self.svg_test_dir)
    copyfile("{}/tests/svgs/{}".format(cwd, self.svg_file), "{}/{}".format(self.svg_test_dir, self.svg_file))

  def teardown_method(self):
    rmtree(self.svg_test_dir)

  def test_get_png_from_svg__returns_success_status_code(self):
    status_code = get_png_from_svg(self.input_file, self.output_file)
    assert status_code == 0
    
  def test_get_png_from_svg__create_png_file(self):
    get_png_from_svg(self.input_file, self.output_file)
    assert os.path.isfile(self.output_file)

