
from .heatmapper import Heatmapper
from PIL import Image, ImageEnhance

def draw_heat(input_filename, output_filename, points, brightness=0.6):
    example_img = Image.open(input_filename)
    enhancer = ImageEnhance.Brightness(example_img)
    example_img = enhancer.enhance(brightness)

    heatmapper = Heatmapper()
    heatmap = heatmapper.heatmap_on_img(points, example_img)
    heatmap.save(output_filename)
