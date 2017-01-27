from inkscape.svg_to_png.get_png_from_svg import get_png_from_svg

def test_get_png_from_svg__given_svg_file__returns_success_code():
  svg_file = "a_valid_svg_file.svg"
  status_code = get_png_from_svg(svg_file)
  assert status_code == 0

def test_get_png_from_svg__given_non_svg_file__returns_fail_code():
  non_svg_file = "music.mp3"
  status_code = get_png_from_svg(non_svg_file)
  assert status_code == -1
