import core.xMapCore as xMapCore


def print_hi():
    for r in xMapCore.main():
        for ri in r:
            print(ri)


if __name__ == '__main__':
    print_hi()
