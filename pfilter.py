import os

current_directory = os.path.dirname(os.path.abspath(__file__))

def concatenate(base_path, sub_path):
	if not os.path.isabs(base_path):
		base_path = os.path.join(current_directory, base_path)

	final_path = os.path.abspath(os.path.join(base_path, sub_path))

	base_path = os.path.normpath(base_path)
	final_path = os.path.normpath(final_path)

	if os.path.commonpath([base_path, final_path]) == base_path:
		return final_path

