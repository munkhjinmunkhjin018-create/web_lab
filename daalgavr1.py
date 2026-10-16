
class Worker:
    ndaatgal = 16
    emdaatgal = 4

    def __init__(self, code, name, salary):
        self.workerCode = code
        self.workerName = name
        self.fixedSalary = salary

    def calculateTax(self, nd, emd):
        return self.fixedSalary * (nd + emd) / 100

    def calculateSalary(self):
        return self.fixedSalary - self.calculateTax(self.ndaatgal, self.emdaatgal)

    def __str__(self):
        return f"{self.workerCode} - {self.workerName}"


class BasicWorker(Worker):
    bonusSalary = 100000

    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)

    def calculateTax(self, nd, emd):
        return (self.fixedSalary + self.bonusSalary) * (nd + emd) / 100

    def calculateSalary(self):
        return self.fixedSalary + self.bonusSalary - self.calculateTax(self.ndaatgal, self.emdaatgal)


class Company:
    def __init__(self, name):
        self.companyName = name
        self.resource = []

    def addNewWorker(self, worker):
        if isinstance(worker, BasicWorker):
            self.resource.append(worker)
        else:
            print("Зөвхөн BasicWorker бүртгэнэ.")

    def countWorker(self):
        return len(self.resource)

    def calculateTotalTax(self):
        total = 0
        for worker in self.resource:
            total += worker.calculateTax(worker.ndaatgal, worker.emdaatgal)
        return total

    def __str__(self):
        return f"Компани: {self.companyName}, Ажилтны тоо: {self.countWorker()}"


company = Company("My Company")

worker1 = Worker(101, "Bat", 1000000)
worker2 = Worker(102, "Bold", 1200000)

worker3 = BasicWorker(103, "Sara", 1100000)
worker4 = BasicWorker(104, "Anu", 1300000)
worker5 = BasicWorker(105, "Naraa", 900000)
worker6 = BasicWorker(106, "Temuulen", 1500000)
worker7 = BasicWorker(107, "Enkhjin", 1400000)

company.addNewWorker(worker3)
company.addNewWorker(worker4)
company.addNewWorker(worker5)
company.addNewWorker(worker6)
company.addNewWorker(worker7)

print("--- Worker объектууд ---")
for worker in [worker1, worker2]:
    print(worker)
    print("Гарт олгох цалин:", worker.calculateSalary())
    print("Шимтгэл:", worker.calculateTax(worker.ndaatgal, worker.emdaatgal))

print("\n--- Компанийн ажилтнууд ---")
for worker in company.resource:
    print(worker)
    print("Гарт олгох цалин:", worker.calculateSalary())
    print("Шимтгэл:", worker.calculateTax(worker.ndaatgal, worker.emdaatgal))

print("\n--- Компанийн мэдээлэл ---")
print(company)
print("Нийт ажилтны тоо:", company.countWorker())
print("Нийт суутгал:", company.calculateTotalTax())
