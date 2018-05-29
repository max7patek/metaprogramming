

class image:

    def __init__(self, array):
        self.array = array

    def __eq__(self, other):
        return self.array == other.array

    def lighten(self, amount):
        out = []
        for i in range(len(self.array)):
            out.append([])
            for j in range(len(self.array[i])):
                out[i].append(self.array[i][j] + amount)
        return image(out)

    def darken(self, amount):
        out = []
        for i in range(len(self.array)):
            out.append([])
            for j in range(len(self.array[i])):
                out[i].append(self.array[i][j] - amount)
        return image(out)

    def scalar_multiply(self, scalar):
        out = []
        for i in range(len(self.array)):
            out.append([])
            for j in range(len(self.array[i])):
                out[i].append(self.array[i][j] * scalar)
        return image(out)

    def add(self, other):
        out = []
        assert len(self.array) == len(other.array), "must add images of same dimension"
        for i in range(len(self.array)):
            out.append([])
            assert len(self.array[i]) == len(other.array[i]), "must add images of same dimension"
            for j in range(len(self.array[i])):
                out[i].append(self.array[i][j] + other.array[i][j])
        return image(out)

    def average(self, other):
        out = []
        assert len(self.array) == len(other.array), "must average images of same dimension"
        for i in range(len(self.array)):
            out.append([])
            assert len(self.array[i]) == len(other.array[i]), "must average images of same dimension"
            for j in range(len(self.array[i])):
                out[i].append(.5*self.array[i][j] + .5*other.array[i][j])
        return image(out)
