from typing import Any

def root(num: int):
    return pow(num, .5)

root1_25 = root(25)
# root1_25.  # Did not got related commands suggestion on typing dot after `root_25` as it is not known which type of data will it store

root2_25: float = root(25)
# root2_25.  # We now got float related functions in suggestions

# Another way is to hint on the return type of the definition itself
def root1(num: int | float, exp: float | None = .5) -> float:   # if `exp` is not passed then its value becomes 0.5, BUT if `exp` is passed as `None` then its value is `None` so his case is handled explicitly in return statement
    # if exp is None:
    #     exp = .5
    # return pow(num, exp)

    # return pow(num, exp or .5)

    return pow(num, .5 if exp is None else exp)

root3_25 = root1(36, None)
# root3_25.  # We now got float related functions in suggestions

root4_25 = root1(25)
# root4_25.  # We now got float related functions in suggestions

# ***** Type Hinting for List & Tuple & Dict *****

alphabets: list = [3, 5, 8]
digits: list[int] = [3]

class City:
    def __init__(self, name, location):
        self.name = name,
        self.location = location

alphabetsTuple: tuple = (1, 6, 9)
digitsTuple1: tuple[str] = ('d', 'a')    # Type Hinting Error (Not the syntax error)
digitsTuple2: tuple[int, int, str] = (2, 4, 'd')
digitsTuple3: tuple[str] = ('d', 'a')    # Type Hinting Error (Not the syntax error)
digitsTuple4: tuple[str, ...] = ('a', 'b', 'c')
digitsTuple5: tuple[int, ...] = (1, 2, 3)

city_temp1: tuple[str, float] = ("City", 20.5)

city = City("City", 82304873)
city_temp2: tuple[City, float] = (city, 20.5)

shipment0: dict = {
    "content": "wooden table",
    "status": "in transit"
}

shipment1: dict[str, str] = {   # Type hinting for dict is done as [key, value]
    "content": "wooden table",
    "status": "in transit"
}

shipment2: dict[str, str | int] = {
    "id": 90127,
    "content": "wooden table",
    "status": "in transit"
}

shipment3: dict[str, str | int | float] = {
    "id": 32874,
    "weight": 2.17,
    "content": "wooden table",
    "status": "in transit"
}

shipment4: dict[str, Any] = {
    "id": 32874,
    "weight": 2.17,
    "content": "wooden table",
    "status": "in transit"
}


# About Union & Optional
from typing import Union, Optional


