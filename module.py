import json


import json

a={
    "name":"ajit",
    "age":89, 
    "year":4589 ,
    "marride":True,
    "divorced":False,
    "childere":("hardik","ajit"),
    "pets":"none",
    "cars":[
        {
            "model":"gwagon",
            "avg":12.5
        },
        {
            "model":"bmwx5",
            "avg":23.5

        }
    ]}



print(json.dumps(a,indent=3))