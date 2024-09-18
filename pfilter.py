import os

current_directory = os.path.dirname(os.path.abspath(__file__))

def concatenate(base_dir, path):
    
    if not os.path.isabs(base_dir):
        base_dir = os.path.join(current_directory, base_dir)

    path = os.path.join(base_dir, path)
    if os.path.commonprefix([os.path.realpath(path), base_dir]) == base_dir:
        return path
    
    return None

