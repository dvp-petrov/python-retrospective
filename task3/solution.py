class Person:

    def __init__(self, name="", birth_year=0, gender=""):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.brother_list = []
        self.sister_list = []
        self.children_list = []

    def father(self, father_person):
        if father_person.gender == "male" and father_person.birth_year + 18 <= self.birth_year:
            self.father = father_person
            return father_person
        else:
            return (father_person.name + " can't be father of " + self.name)

    def mother(self, mother_person):
        if mother_person.gender == "female" and mother_person.birth_year + 18 <= self.birth_year:
            self.mother = mother_person
            return mother_person
        else:
            return (mother_person.name + " can't be mother of " + self.name)

    def is_brother(self, brother_person):
        if self is not brother_person:
            if brother_person.gender == "male":
                if self.mother is brother_person.mother or self.father is brother_person.father:
                    if brother_person not in self.brother_list:
                        self.brother_list.append(brother_person)
                    if self.gender == "male":
                        if self not in brother_person.brother_list:
                            brother_person.brother_list.append(self)
                    elif self.gender == "female":
                        if self not in brother_person.sister_list:
                            brother_person.sister_list.append(self)

    def get_brother(self):
        return self.brother_list

    def is_sister(self, sister_person):
        if self is not sister_person:
            if sister_person.gender == "female":
                if self.mother is sister_person.mother or self.father is sister_person.father:
                    if sister_person not in self.sister_list:
                        self.sister_list.append(sister_person)
                    if self.gender == "male":
                        if self not in sister_person.brother_list:
                            sister_person.brother_list.append(self)
                    elif self.gender == "female":
                        if self not in sister_person.sister_list:
                            sister_person.sister_list.append(self)

    def get_sister(self):
        return self.sister_list

    def is_child(self, child_person):
        if child_person.mother is self or child_person.father is self:
            if child_person not in self.children_list:
                self.children_list.append(child_person)

    def children(self, gender=""):
        if gender == "male":
            return_list = []
            for child in self.children_list:
                if child.gender == "male":
                    return_list.append(child)
            return return_list
        elif gender == "female":
            return_list = []
            for child in self.children_list:
                if child.gender == "female":
                    return_list.append(child)
            return return_list
        else:
            return self.children_list

    def is_direct_successor(self, person):
        if self is person.father or self is person.mother or person is self.father or person is self.mother:
            return True
        else:
            return False
