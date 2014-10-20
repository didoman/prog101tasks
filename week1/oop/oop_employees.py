#


class Employee:
    def __init__(self, name):
        self.name = name
        self.weekly = 0
        pass

    def weeklyPay(self, hours):
        if isinstance(self, HourlyEmployee):
            if hours <= 40:
                self.weekly = float(hours * self.perhour)
            else:
                hours = hours - 40
                self.weekly = float((40 * self.perhour) + (hours * self.perhour * 1.5))
        elif isinstance(self, SalariedEmployee) and not isinstance(self, Manager):
            self.weekly = float(self.anually / 52)
        elif isinstance(self, Manager):
            self.weekly = float((self.anually / 52) + float(self.bonus))
        return self.weekly

    def getName(self):
        print(self.name)
        return self.name


class HourlyEmployee(Employee):
    def __init__(self, name, perhour):
        super().__init__(name)
        self.perhour = perhour


class SalariedEmployee(Employee):
    def __init__(self, name, anually):
        super().__init__(name)
        self.anually = anually
        pass


class Manager(SalariedEmployee):
    def __init__(self, name, anually, bonus):
        super().__init__(name, anually)
        self.bonus = bonus
        pass


staff = []
staff.append(HourlyEmployee("Morgan, Harry", 30.0))
staff.append(SalariedEmployee("Lin, Sally", 52000.0))
staff.append(Manager("Smith, Mary", 104000.0, 50.0))
for employee in staff:
    hours = int(input("Hours worked by " + employee.getName() + ": "))
    pay = employee.weeklyPay(hours)
    print(pay)
    print("Salary: %.2f" % pay)
