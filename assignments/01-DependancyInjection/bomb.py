secret_code = "foo"

class explosives:
    def trigger(self):
        print('BOOOOOOOM')
        #exit(1)

class bomb(explosives):
    def trigger(self):
        assert isinstance(self, bomb)
        #from runner import secret_code
        print("the code is ", secret_code)
        super().trigger()
