


def furthest_value_in_list(List:list, number:int|float):
    a = max(List, key=lambda x:abs(x-number))
def closest_value_in_list(List:list, number:int|float):
    a = min(List, key=lambda x:abs(x-number))

def furthest_value_in_dict(Dict:dict, number:int|float):
    a = max(Dict, key=lambda x:abs(Dict[x]-number))
def closest_value_in_dict(Dict:dict, number:int|float):
    a = min(Dict, key=lambda x:abs(Dict[x]-number))
