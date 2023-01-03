import json
import requests
from pprint import pp
#serialize a json, encoding data into json format
#deserialize a jason, decoding json into another format


data = {
    "user" : { "name": "william williams",
                "age": 93
}
}

#print(data["user"["age"]])

with open("data_file.json","w") as write_file:
    json.dump(data,write_file, indent=4)

json_str = json.dumps(data, indent=4)
print(json_str)

#let's check and see if serialization and deserialization are perfect inverses

blkjk_hand = (8,"Q")
encoded = json.dumps(blkjk_hand)
decoded = json.loads(encoded)

print(type(blkjk_hand))
print(type(decoded))
print(blkjk_hand == tuple(decoded))

response = requests.get("http://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

print(type(todos))

pp(todos[:10])

todos_by_user={}
for item in todos:
    if item["completed"]==True:
     
        if item["userId"] not in todos_by_user.keys():
            todos_by_user[item["userId"]]=1
        else:
            todos_by_user[item["userId"]]+=1
print(todos_by_user)

top_users = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
print(top_users)

# with that code above we are sorting by the values due to the lamda function sorting at x[1]
max_complete = top_users[0][1]
print(max_complete)
users = []
for user, value in top_users:
    if value== max_complete:
        users.append(str(user))
max_users = " and ".join(users)    
print("users {} completed {} ".format(max_users,max_complete))


def keep(todos):
      is_complete = todos["completed"]
      has_max_count = str(todos["userId"]) in users
      return is_complete and has_max_count

with open("filtered_data_file.json", "w") as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=2)

class Elf:
    def __init__(self, level, ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str": 11, "dex": 12, "con": 10,
            "int": 16, "wis": 14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores["con"]


        elf = Elf(level=4)
        json.dumps(elf)
#         # print(elf)
# z=8+3j
# print(type(z))
# # json.dumps(z)
# print(z.real)
# print(z.imag)

# complex(8,3)==z


        def encode_complex(z):
                if isinstance(z, complex):
                    return (z.real, z.imag)
                else:
                    type_name = z.__class__.__name__
                    raise TypeError(f"Object of type '{type_name}' is not JSON serializable")
                    # result=json.dumps(9 + 5j, default=encode_complex)
                    # print(result)
        # r=json.dumps(elf, default=encode_complex)
        # print(r)
    
class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            return super().default(z)
result=json.dumps(2 + 5j, cls=ComplexEncoder)
print(result)

encoder = ComplexEncoder()
r=encoder.encode(3 + 6j)
print(r)

complex_json = json.dumps(4 + 17j, cls=ComplexEncoder)
# json.loads(complex_json)
print(complex_json)


def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct

with open("complex_data.json") as complex_data:
    data = complex_data.read()
    z = json.loads(data, object_hook=decode_complex)

    print(z)

# with open("complex_data.json") as complex_data:
#     data = complex_data.read()
#     numbers = json.loads(data, object_hook=decode_complex)
 
# print(numbers)


















