from inkscape.ios_asset.generate_from_svg import get_ios_asset_from_svg 
from PIL import Image
import os
import subprocess
from shutil import copyfile, rmtree
import pytest

class TestIntegrationGenerateIOSAsset(object):
  svg_test_dir = "/tmp/svg_test_dir"
  svg_file = "GrayBall.svg"
  png_file = "GrayBall.png"
  png_file_2x = "GrayBall@2x.png"
  svg_width_2x = None
  svg_height_2x = None
  input_file = "{}/{}".format(svg_test_dir, svg_file)
  output_file = "{}/{}".format(svg_test_dir, png_file)
  output_file_2x = "{}/{}".format(svg_test_dir, png_file_2x)
          
  def setup_method(self):
    cwd = os.getcwd()
    os.makedirs(self.svg_test_dir)
    copyfile("{}/tests/svgs/{}".format(cwd, self.svg_file), "{}/{}".format(self.svg_test_dir, self.svg_file))
    self.svg_width_2x = float(subprocess.check_output(["inkscape", "-z", "-W", self.input_file]).decode('utf-8'))
    self.svg_height_2x = round(float(subprocess.check_output(["inkscape", "-z", "-H", self.input_file]).decode('utf-8')))


  def teardown_method(self):
    rmtree(self.svg_test_dir)
  

  def test_generate_ios_assert_from_svg(self):
    status_code = get_ios_asset_from_svg(self.input_file, self.svg_test_dir)
    assert status_code == 0


  def test_generate_ios_asset_from_svg__returns_png_file(self):
    get_ios_asset_from_svg(self.input_file, self.svg_test_dir)
    assert os.path.isfile(self.output_file) 


  def test_generate_ios_assert_from_svg__returns_png_with_half_original_size(self):
    get_ios_asset_from_svg(self.input_file, self.svg_test_dir)
    with Image.open(self.output_file) as image:
      width, height = image.size
      expected_width = self.svg_width_2x / 2
      expected_height = self.svg_height_2x / 2
      assert width == expected_width
      assert height == expected_height


  def test_generate_ios_asset_from_svg__returns_png_2x_file(self):
    get_ios_asset_from_svg(self.input_file, self.svg_test_dir)
    assert os.path.isfile(self.output_file_2x) 

  
  def test_generate_ios_assert_from_svg__returns_png_2x_with_original_size(self):
    get_ios_asset_from_svg(self.input_file, self.svg_test_dir)
    with Image.open(self.output_file_2x) as image:
      width, height = image.size
      assert width == self.svg_width_2x
      assert height == self.svg_height_2x

