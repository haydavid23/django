"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [{
            "id": 1,
            "first_name": "John"
        }]

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["id"] = self._generateId()
        self._members.append(member)
        return member

    def delete_member(self, id):
        aux = []
        for x in self._members:
            if x["id"] != id:
                aux.append(x)
        self._members = aux
        return self._members

    def update_member(self, id, member):
        aux = []
        for x in self._members:
            if x["id"] != id:
                aux.append(x)
            else:
                aux.append(member)
        self._members = aux
        return member

    def get_member(self, id):
        for x in self._members:
            if x["id"] == id:
                return x
        return None

    def get_all_members(self):
        return self._members