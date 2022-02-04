from operator import mod
from chefboost import Chefboost as chef

class Predector:
    def __init__(self):
        self.model = chef.load_model("model.pkl")

    def predetor(self,userdata):
        self.predection= chef.predict(self.model,userdata)
        return self.predection

