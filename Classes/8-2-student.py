class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house} casts a/an {self.patronus} patronus!"

    @classmethod
    def get(cls):
        name = input("Name:  ")
        house = input("House:  ")
        patronus = input("Patronus:  ")
        return cls(name, house, patronus)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    @property
    def patronus(self):
        return self._patronus

    @patronus.setter
    def patronus(self, patronus):
        if patronus not in ["Stag", "Otter", "Jack Russell terrier"]:
            raise ValueError("Invalid Patronus")
        else:
            self._patronus = patronus

    def charm(self):
        if self.patronus == "Stag":
            return "🐴"
        elif self.patronus == "Otter":
            return "🦦"
        elif self.patronus == "Jack Russell terrier":
            return "🐶"
        else:
            return "🪄"


def main():
    student = Student.get()
    print(student)
    print("Expecto Patronum!")
    print(student.charm())


if __name__ == "__main__":
    main()