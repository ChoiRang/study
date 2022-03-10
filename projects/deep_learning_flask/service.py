import pandas as pd


class Service:
	def __init__(self):
		self.labels = pd.read_csv('static/labels.csv').to_dict()

	def extract_label(self):
		label = self.labels
		return label
