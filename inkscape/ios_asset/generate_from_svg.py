import sys
import os
import xml.etree.ElementTree as ET

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
  svg_settings = _get_svg_settings(input_file)
  return int(svg_settings["width"])


def get_height_of_svg(input_file):
  svg_settings = _get_svg_settings(input_file)
  return int(svg_settings["height"])


def _get_svg_settings(input_file):
  tree = ET.parse(input_file)
  svg_root = tree.getroot()
  return {tuple_item[0]: tuple_item[1] for tuple_item in svg_root.items()}
  

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
  input_dir = sys.argv[1]
  output_dir = sys.argv[2]
  if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

  for root, dirs, file_names in os.walk(input_dir):
    for file_name in file_names:
      file_path = os.path.join(root, file_name)
      if os.path.isfile(file_path) and file_path.endswith(".svg"):
        print(file_path)
        get_ios_asset_from_svg(file_path, output_dir)
 
