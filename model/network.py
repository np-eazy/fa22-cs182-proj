# TODO: Combine smaller modules into the full network here

class Network:
    def __init__(self, props):
        self.x = None

    def trainNetwork(self, data, props):
        for i in range(len(data)):
            self.forward()
            self.backward()
        return None

    def testNetwork(self, data, props):
        for i in range(len(data)):
            self.forward()
        return None

    def forward(self, x):
        return None

    def backward(self, grad):
        return None