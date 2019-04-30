# Family Tree Boilerplate

- The only two files you have to edit are `api/views.py` and `api/family_datastructure.py`
- We have prepared a set of automated tests that will give you an idea if your code is done, run the tests by typing `$ pipenv run tests` on the command line.

Today we are going to be building a small API around the following data-structure class:
```py
class Family:

	def __init__(self, last_name):
		self.last_name = last_name
		self._members = []

    def _generateId(self):
        return randint(0, 99999999)

	def add_member(self, member):
		pass

	def delete_member(self, id):
		pass

	def update_member(self, id, member):
		pass

	def get_member(self, id):
		pass

	def get_all_members(self, id):
		return self._members;
```
