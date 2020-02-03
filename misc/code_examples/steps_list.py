class Processor:

    def __init__(self, x):
        self.x = x
        self.steps = [
            self.add_one,
            self.add_two,
            self.subtract_one,
            self.add_one,
        ]

    def add_one(self):
        self.x += 1

    def add_two(self):
        self.x += 2

    def subtract_one(self):
        self.x -= 1

    def __call__(self):
        for step in self.steps:
            step()
        return self.x


class OneLessProcessor(Processor):

    def __init__(self, x):
        super().__init__(x)
        self.steps.append(self.subtract_one)
