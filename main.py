import random

print("\t\t\t\t**************************")
print("\t\t\t\t\t\tZADANIE 1")
print("\t\t\t\t**************************")


class Komputer:
    def __init__(self, komputer, ram,  pamiec):
        self.komputer = komputer;
        self.ram = ram;
        self.pamiec = pamiec;

class Laptop(Komputer):
    def __init__(self, komputer, ram, pamiec, model):
        super().__init__(komputer, ram, pamiec)
        self.model = model;

class Tablet(Komputer):
    def __init__(self, komputer, pamiec, model, ram):
        super().__init__(komputer, ram, pamiec)
        self.model = model

huawei = Tablet('huawei', 2, 256, 'matepad 11')
print('\nTo jest tablet: ', huawei.komputer);
print('Pamiec RAM: ', huawei.ram, 'gb');
print('Pamiec na dysku: ', huawei.pamiec, 'gb');
print('To jest model tableta: ', huawei.model);


lenovo = Laptop('lenovo', 2, 512,'Y520')
print('\nTo jest laptop: ', lenovo.komputer);
print('Pamiec RAM: ', lenovo.ram, 'gb');
print('Pamiec na dysku: ', lenovo.pamiec, 'gb');
print('To jest model laptopa: ', lenovo.model);

class Stos:
    gadzety=[];
    gadzety.append('lenovo')
    gadzety.append('huawei')
    print('\nObecne gadzety: ', gadzety)

print("\n\t\t\t\t**************************")
print("\t\t\t\t\t\tZADANIE 2")
print("\t\t\t\t**************************\n")

class Dodcal:

    A={1,2,3,4,5,6,7,8}
    B={2,4,6,8,10,12}
    print('Suma zbiorow A&B to: ', A|B)
    print('Czesc wspolna zbiorow A&B to: ',A&B)
    print('Roznica zbiorow A&B to: ',A-B)

    randomlista = random.sample(range(10, 30), 10)
    randomlistb = random.sample(range(10, 30), 10)
    print('\n', randomlista, '\n', randomlistb)
    # print('Suma zbiorow A&B to: ', randomlista & randomlistb)  -
    # NIESTETY POWYZSZY WERS NIE DZIALA I RZUCA BLEDEM "unsupported operand type(s) for &: 'list' and 'list'"
