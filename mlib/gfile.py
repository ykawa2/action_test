import os


def basename_without_ext(path):
    basename = os.path.basename(path)
    dot_cnt = basename.count('.')

    if dot_cnt <= 1:
        ret = os.path.splitext(basename)[0]
    elif dot_cnt == 2:
        print(basename.split('.'))
        ret = basename.split('.')[0]
    else:
        raise ValueError('Too many dots in {}'.format(basename))

    return ret


def load_numbers_sorted(filepath):
    numbers = []

    with open(filepath) as f:
        numbers = sorted(map(lambda e: int(e), f))

    return numbers
