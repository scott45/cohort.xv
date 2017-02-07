__author__ = 'Scott Businge'


# OOP real world example was demonstrating OOP through Andela boot camp

class Bootcamp(object):  # super class (main).
    def __init__(self, cohort, group, bcf):  # instantiation
        self.cohort = cohort
        self.group = group
        self.bcf = bcf


class Bootcamper(Bootcamp):  # inheritance                                 # second class that inherits from super.
    def __init__(self, country, city, first_name, last_name, role, pay, ):
        super().__init__(country, city)
        self.first = first  # other class declarations not main.
        self.last = last
        self.role = role
        self.pay = pay
        self.email = first + last + '@gmail.com'

    def permanent(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


employee1 = Andelan('Kenya', 'Nairobi', 'James', 'Ndiga', 'HR', 2000, )           # instances
fellow2 = Andelan('Kenya', 'Nairobi', 'kironde', 'victor', 'fellow', 500, )
bootcamper3 = Andelan('Kenya', 'Nairobi', 'scott', 'businge', 'b.c', 500, )

print(employee1.email)                                                             # print returns
print(fellow2.email)
print(bootcamper3.email)
print(employee1.logo)