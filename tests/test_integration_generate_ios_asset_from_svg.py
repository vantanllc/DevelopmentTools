from inkscape.ios_asset.generate_from_svg import get_ios_asset_from_svg 
import os
from shutil import copyfile, rmtree
import pytest

class TestIntegrationGenerateIOSAsset(object):
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

  def test_generate_ios_assert_from_svg(self):
    status_code = get_ios_asset_from_svg(self.input_file)
    assert status_code == 0

