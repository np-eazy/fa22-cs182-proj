# A simulator essentially streams data to a Stage, which is in charge
# with transforming, processing, and tampering with the data. It can either be
# When the simulator "adds" new datapoints it will save them to a data file that
# can be loaded later to create a new Stage.

class Stage:
    def __init__(self, name):
        self.name = name
        self.model_props = None
        self.physical_props = None
        self.data = []

    def clear(self):
        self.model_props = None
        self.physical_props = None
        self.data = []
    
    def set_model_props(self, model_props):
        self.model_props = model_props

    def set_physical_props(self, physical_props):
        self.physical_props = physical_props

    def add(self, nextstep):
        print(self.data)
        self.data += [nextstep]
        # TODO: Here we should be implementing persistence/caching for large data

    def reshape_for_network(self, props):
        # TODO: Change the tensor shape to whatever the network takes. Change model and physical props
        return None

    def tamper(self, params):
        # TODO: Change the tensor shape to whatever the network takes. Change model and physical props
        return None

    def load_from_file(self, update):
        # TODO: Retrieve saved data
        return None