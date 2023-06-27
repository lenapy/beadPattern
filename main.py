import numpy as np
from PIL import Image
from sklearn.cluster import KMeans


class BeadPattern:
	
	def __init__(self, image_path, output_file_name, size, n_colors):
		self.image_path = image_path
		self.output_file_name = output_file_name
		self.size = size
		self.n_colors = n_colors
		self.img = None

	def load_image(self):
		self.img = Image.open(self.image_path)
	
	def process_image(self):
		width, height = self.img.size
		self.img = self.img.resize((width // self.size, height // self.size), Image.NEAREST)
		return np.array(self.img)
	
	def cluster_colors(self):
		data = self.process_image()
		reshaped_data = data.reshape(-1, 3)
		kmeans = KMeans(n_clusters=self.n_colors)
		kmeans.fit(reshaped_data)
		return kmeans.cluster_centers_[kmeans.predict(reshaped_data)]
	
	def map_colors_to_image(self):
		new_colors = self.cluster_colors()
		new_img = Image.fromarray(new_colors.astype('uint8'), 'RGB')
		return new_img.resize((new_img.size[0] * self.size, new_img.size[1] * self.size), Image.NEAREST)
	
	def save_bead_img(self):
		bead_img = self.map_colors_to_image()
		bead_img.save(self.output_file_name)
		
	def create_pattern(self):
		self.load_image()
		self.process_image()
		self.cluster_colors()
		self.map_colors_to_image()
		self.save_bead_img()
