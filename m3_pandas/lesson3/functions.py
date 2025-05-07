def set_size(size):
    if size[-1] == 'M':
        size = size[:-1]
        return float(size)
    elif size[-1] == 'k':
        size = size[:-1]
        return float(size)/1024
    return -1


def set_installs(installs):
    if installs == '0':
        return 0
    return int(installs[:-1].replace(',', ''))

