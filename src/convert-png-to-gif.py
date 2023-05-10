from PIL import Image
import glob

# Create the frames
frames = []
imgs = glob.glob("../tmp/*.png")
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

# Save into a GIF file that loops forever
frames[0].save('png_to_gif.gif', format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=120, loop=1)