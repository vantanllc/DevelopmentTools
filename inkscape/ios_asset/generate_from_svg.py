from inkscape.svg_to_png.get_png_from_svg import get_png_from_svg

def get_ios_asset_from_svg(input_file, output_dir):
  file_name = input_file.split("/")[-1]
  file_name_png = file_name.replace(".svg", ".png")
  output_file = "{}/{}".format(output_dir, file_name_png)
  return get_png_from_svg(input_file, output_file) 
