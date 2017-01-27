import subprocess

INKSCAPE_COMMAND = "inkscape"
NO_GUI_FLAG = "-z"
OUTPUT_PNG_FLAG = "-e"
  
def get_png_from_svg(svg_file_path, output_file_path):
  if svg_file_path.endswith("svg") and output_file_path.endswith("png"):
    return subprocess.call([INKSCAPE_COMMAND, NO_GUI_FLAG, OUTPUT_PNG_FLAG, output_file_path, svg_file_path])
  else:
    return -1

