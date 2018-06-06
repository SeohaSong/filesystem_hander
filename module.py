import os

def get_global_filepaths(root_dir):
    ls = os.listdir(root_dir)
    paths = [os.path.join(root_dir, c) for c in ls]
    filepaths = [[path] if os.path.isfile(path)
                 else get_global_filepaths(path)
                 for path in paths]
    filepaths = sum(filepaths, [])
    return filepaths