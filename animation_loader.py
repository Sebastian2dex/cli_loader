def runner(string, speed=0.2):
    from time import sleep
    rotate = ('|', '/', '-', '\\', '-')
    i = 0
    r = 0
    while True:
        print(f'  {string[0:i] + string[i].upper() + string[i+1:len(string)]}' + f' --[{rotate[r]}]', end='\r')
        sleep(speed)
        i += 1
        r += 1
        if i == len(string):
            i = 0
        if r == len(rotate)-1:
            r = 0

if __name__ == '__main__':
	runner(input())
