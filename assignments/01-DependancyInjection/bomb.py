class explosives:
    def trigger(self):
        print('BOOOOOOOM')
        exit(1)


class bomb(explosives):
    def trigger(self):
        print("the code is ", 'abcde')
        super().trigger()
