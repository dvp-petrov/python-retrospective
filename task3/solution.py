class Person:

    def __init__(self, name, gender, birth_year, father=None, mother=None):
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        if father and father.birth_year + 18 <= self.birth_year:
            self.father = father
            self.father.children_list.append(self)
        if mother and mother.birth_year + 18 <= self.birth_year:
            self.mother = mother
            self.mother.children_list.append(self)
        self.children_list = []

    def get_brothers(self):
        return [brother for brother in
                self.mother.children_list or
                self.father.children_list if
                brother.gender == 'M' and
                brother != self
                ]

    def get_sisters(self):
        return [sister for sister in
                self.mother.children_list or
                self.father.children_list if
                sister.gender == 'F' and
                sister != self
                ]

    def children(self, gender=None):
        if gender:
            return [girls_or_boys for girls_or_boys in
                    self.children_list if girls_or_boys.gender == gender
                    ]
        return self.children_list

    def is_direct_successor(self, person):
        if person in self.children_list:
            return True
        else:
            return False
