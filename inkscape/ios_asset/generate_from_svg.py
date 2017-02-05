import sys
import os

try:
  sys.path.index(os.getcwd())
except ValueError:
  sys.path.append(os.getcwd())

from inkscape.svg_to_png.get_png_from_svg import get_png_from_svg
import subprocess

def get_ios_asset_from_svg(input_file, output_dir):
  status_code = _create_1x_asset(input_file, output_dir)
  status_code = _create_2x_asset(input_file, output_dir)
  status_code = _create_3x_asset(input_file, output_dir)
  return status_code


def get_width_of_svg(input_file):
  return round(float(subprocess.check_output(["inkscape", "-z", "-W", input_file]).decode('utf-8')))


def get_height_of_svg(input_file):
  return round(float(subprocess.check_output(["inkscape", "-z", "-H", input_file]).decode('utf-8'))) 


def _create_1x_asset(input_file, output_dir):
  file_name = input_file.split("/")[-1]
  scale = 0.5
  width = get_width_of_svg(input_file) * scale
  height = get_height_of_svg(input_file) * scale
  file_name_png = file_name.replace(".svg", ".png")
  output_file = "{}/{}".format(output_dir, file_name_png)
  return get_png_from_svg(input_file, output_file, str(width), str(height)) 

def _create_3x_asset(input_file, output_dir):
  file_name = input_file.split("/")[-1]
  scale = 1.5
  width = get_width_of_svg(input_file) * scale
  height = get_height_of_svg(input_file) * scale
  file_name_png = file_name.replace(".svg", "@3x.png")
  output_file = "{}/{}".format(output_dir, file_name_png)
  return get_png_from_svg(input_file, output_file, str(width), str(height)) 


def _create_2x_asset(input_file, output_dir):
  file_name = input_file.split("/")[-1]
  file_name_png = file_name.replace(".svg", "@2x.png")
  output_file = "{}/{}".format(output_dir, file_name_png)
  return get_png_from_svg(input_file, output_file) 

if __name__ == "__main__":
  input_file = sys.argv[1]
  output_dir = sys.argv[2]
  if not os.path.isdir(output_dir):
    os.makedirs(output_dir)
  get_ios_asset_from_svg(input_file, output_dir)
 
