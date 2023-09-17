import json 
import os

def rewrite_json(iter: int, script):
    path = "history/silicon_valley_ex.json"
    record_path = f"history/record_{iter}"


    dirname = os.path.dirname(__file__)
    path = os.path.join(dirname, path)
    record_path = os.path.join(dirname, record_path)

    with open(path, 'w') as f:
        json.dump(script, f)
    
    with open(record_path, 'w') as f:
        json.dump(script, f)




# def store_record(iter: int, info: dict(), id1: str, id2: str):
#     """
#     iter: # calls to this function so far, used to create a custom directory to store the json
#     info: the current dictionary containing information on the characters
#     id1: the id of person 1 in the conversation 
#     id2: the id of person 2 in the conversation
#     intel1: updated interactions for person 2 in person1's file
#     intel2: updated interactions for person 1 in person2's file
#     """


#     dirname = os.path.dirname(__file__)
#     path = os.path.join(dirname, path)

#     with open(path, "w") as f:
#         json.dump(info, f)

    # info[id1]["interactions"][id2] = inte1
    # info[id2]["interactions"][id1] = inte2
