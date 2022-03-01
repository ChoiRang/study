import pandas as pd


class ExtractLegalCode:
	def __init__(self):
		self.legal_code_df = pd.read_csv('/Users/cyh/Documents/study/projects/project1/data/dong_legal_code.csv')

	def extract_local(self):
		local = {}
		local1 = self.legal_code_df['dong_name'].str.split().str[0].unique().tolist()
		for gu in local1:
			local2 = self.legal_code_df[self.legal_code_df['dong_name'].str.split().str[0] == gu]['dong_name'].str.split().str[
				1].dropna().unique().tolist()
			local[gu] = local2
		return local

	def extract_local_code(self, local_first, local_second):
		self.legal_code_df['dong_name']
		dong1 = self.legal_code_df[self.legal_code_df['dong_name'].str.split().str[0] == local_first]
		legal = dong1[dong1['dong_name'].str.split().str[1] == local_second]['dong_code'].head(1)
		legal_index = legal.index[0]
		legal_code = legal[legal_index]
		legal_code = str(legal_code)
		answer = legal_code[0:5]
		return answer
