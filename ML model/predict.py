from operator import mod
from chefboost import Chefboost as chef
model=chef.load_model("model.pkl")
def predetor(model):
    predection=chef.predict(model,['Male','Yes',3,'Graduate','No',3036,2504,158,360,0,'Semiurban'])
    print(predection)
predetor(model)