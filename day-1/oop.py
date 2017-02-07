__author__ = 'Scott Businge'


# OOP real world example was demonstrating OOP through Andela boot camp

class Bootcamp(object):  # super class (main).
    def __init__(self, cohort, group, bcf):  # instantiation
        self.cohort = cohort
        self.group = group
        self.bcf = bcf


class Bootcamper(Bootcamp):  # inheritance                            # second class that inherits from super.
    def __init__(self, cohort, group, first_name, last_name, gender, pay, ):
        super().__init__(cohort, group)
        self.first_name = first_name  # other class declarations not main.
        self.last_name = last_name
        self.gender = gender
        self.email = first_name + last_name + '@gmail.com'

    def permanent(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


entry1 = Bootcamper(15, 8, 'scott', 'bb', 'M', )           # instances
entry2 = Bootcamper(15, 8, 'kayuyu', 'kk', 'F', )
entry3 = Bootcamper(15, 8, 'vivian', 'vv', 'F', )
entry4 = Bootcamper(15, 8, 'brenda', 'ba', 'F', )

print(entry1.first_name)                                                             # print returns
print(entry2.group)
print(entry3.cohort)
print(entry4.gender)