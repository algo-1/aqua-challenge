from typing import List, Dict, Tuple
from copy import deepcopy

opp: Dict[int, int] = {i: 7-i for i in range(1, 7)}
    
opp_name: Dict[str, str] = {"F": "B", "T": "BT", "L": "R"}
pairs: List[Tuple[str, str]] = list(opp_name.items())
for k,v in pairs:
    opp_name[v] = k

dir_map: Dict[int, List[Tuple[str, str]]] = {
    0 : [("F", "R"), ("L", "F"), ("B", "L"), ("R", "B"), ("T", "T"), ("BT", "BT")],
    1 : [("F", "BT"), ("T", "F"), ("B", "T"), ("BT", "B"), ("L", "L"), ("R", "R")]
}


def reorder_dict(die_map: Dict[str, int], _T: str,  trans: Dict[str, int]) -> dict:
    if _T == "L":
        for x,y in dir_map[0]:
            trans[x] = die_map[y]
    elif _T == "R":
        for x,y in dir_map[0]:
            trans[y] = die_map[x]
    elif _T == "U":
        for x,y in dir_map[1]:
            trans[x] = die_map[y]
    elif _T == "D":
        for x,y in dir_map[1]:
            trans[y] = die_map[x]

    return trans


def get_score(die: Dict[str, int], dirs: str) -> int:
    curr_state: Dict[str, int] = {}
    for s in die:
        curr_state[s] = die[s]
        curr_state[opp_name[s]] = opp[die[s]]

    if not dirs:
        return curr_state["F"]

    trans: Dict[str, int] = {}
    for v in dirs:
        curr_state = deepcopy(reorder_dict(curr_state, v, trans))

    return curr_state["F"]


def face_sum(dirs: str, *dice: Dict[str, int]) -> int:
    total: int = 0
    for die in dice:
        total += get_score(die, dirs)
    
    return total 


if __name__ == '__main__':
    die_1 = {"F": 1, "L": 2, "T": 3} 
    die_2 = {"F": 5, "L": 4, "T": 6}
    die_3 = {"F": 2, "L": 4, "T": 1}

    assert face_sum("LRDLU", die_1, die_1, die_1) == 3
    assert face_sum("", die_1, die_2) == 6
    assert face_sum("LLULULDR", die_2, die_3) == 7
    
    print("\nNO ERRORS FOUND\n")


# User guide

""" Call the face_sum function and pass in the directions as a string of form "ULDLDR" and any number of dice as a dict of form {"BT": 4, "L": 2, "B": 6}
 T -> Top, BT -> Bottom, F -> Front, B -> Back, L -> Left, R -> Right.
 The function returns the desired sum. """