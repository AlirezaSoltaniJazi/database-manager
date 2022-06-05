#  Copyright (c) 2022/3/30 By Alireza Soltani Jazi
import pandas as pd
import random


class FileHandler:
	def __init__(self, src_file: str):
		self._src_file = src_file

	def read_csv_file(self):
		final_list = []
		file_break_point = 10000
		df = pd.read_csv(rf'{self._src_file}', low_memory=False, chunksize=file_break_point)
		print('Processing file', flush=True, end='...')
		for item in df:
			print('.', flush=True, end='')
			temp_list = []
			for index, row in item.iterrows():
				random_number = random.randrange(10, 999999999)
				temp_list.append([random_number + index, row[0], row[1], row[2], row[3]])
			final_list.append(temp_list)
		total_rows = 0
		for internal_list in final_list:
			total_rows += len(internal_list)
		print(f'\nNumber of rows fetched: {total_rows}')
		return final_list
