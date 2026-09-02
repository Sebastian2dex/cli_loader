def runner(string, duration=10):
    from time import monotonic, sleep
    rotate = ('|', '/', '-', '\\', '-')
    speed = 0.2
    i = 0
    r = 0
    end_time = monotonic() + duration
    while monotonic() < end_time:
        print(f'{string[0:i] + string[i].upper() + string[i+1:len(string)]}' + f' --[{rotate[r]}]', end='\r')
        sleep(min(speed, max(0, end_time - monotonic())))
        i += 1
        r += 1
        if i == len(string):
            i = 0
        if r == len(rotate)-1:
            r = 0

if __name__ == '__main__':
    runner(input(), duration=5)
