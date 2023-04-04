def getProgress(val, total, size=10, p='█', bg='-'):
    '''
    Return the progress drawing of current progress
    val: current progress out of total
    total: total progress
    p: progress char
    bg: progress background char
    '''

    perc = val/total
    c = int(perc*size)
    s = p*c
    s += bg*(size-c)
    perc *= 100
    return '\r|{}| {}%'.format(s, int(perc))


if __name__ == '__main__':
    print(getProgress(70,100))
