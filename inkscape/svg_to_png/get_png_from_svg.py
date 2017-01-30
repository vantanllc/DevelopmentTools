import subprocess

INKSCAPE_COMMAND = "inkscape"
NO_GUI_FLAG = "-z"
OUTPUT_PNG_FLAG = "-e"
WIDTH_FLAG = "-w"
HEIGHT_FLAG = "-h"
SVG_SUFFIX = "svg"
PNG_SUFFIX = "png"
  
def get_png_from_svg(svg_file_path, output_file_path, width=None, height=None):
  if svg_file_path.endswith(SVG_SUFFIX) and output_file_path.endswith(PNG_SUFFIX):
    inkscape_call = [INKSCAPE_COMMAND, NO_GUI_FLAG, OUTPUT_PNG_FLAG, output_file_path, svg_file_path]
    if width:
      inkscape_call += [WIDTH_FLAG, width] 
    if height:
      inkscape_call += [HEIGHT_FLAG, height]
      
    return subprocess.call(inkscape_call)
  else:
    return -1

