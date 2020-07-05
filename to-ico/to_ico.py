import ctypes
from tkinter import Tk
from tkinter.filedialog import askopenfilenames
from pathlib import Path
from PIL import Image
from time import sleep


def open_explorer():
	Tk().withdraw()
	filenames = askopenfilenames(
		initialdir = "/",
		title = "Select file",
		filetypes = (("png files","*.png"),)
		)


def png_to_ico():
	counter = 0
	for file in filenames:
		p = Path(file)
		name = p.stem
		folder = p.parents[0]
		new_folder = folder.joinpath('ico')
		Path(new_folder).mkdir(parents=False, exist_ok=True)
		fname = new_folder.joinpath(name)

		img = Image.open(file)
		img.save(f'{fname}.ico', format = 'ICO')
		counter += 1
		print(counter, 'image(s) converted.')
	print('Images converted successfully.')


if __name__ == '__main__':
	ctypes.windll.shcore.SetProcessDpiAwareness(True)
	open_explorer()
	png_to_ico()
	sleep(1)
