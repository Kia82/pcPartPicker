class Component:
    def __init__(self, hwid, name, brand, model, year, price):
        self.hwid = hwid
        self.name = name
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def get_hwid(self):
        return self.hwid

    def get_name(self):
        return self.name

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_price(self):
        return self.price

class CPU(Component):
    def __init__(self, hwid, name, brand, model, year, price, cores, clock_speed, chipset, tdp):
        super().__init__(hwid, name, brand, model, year, price)
        self.cores = cores
        self.clock_speed = clock_speed
        self.chipset = chipset
        self.tdp = tdp

    def get_cores(self):
        return self.cores

    def get_clock_speed(self):
        return self.clock_speed

    def get_chipset(self):
        return self.chipset

    def get_tdp(self):
        return self.tdp

class Motherboard(Component):
    def __init__(self, hwid, name, brand, model, year, price, chipset, pcie_slots, size):
        super().__init__(hwid, name, brand, model, year, price)
        self.chipset = chipset
        self.pcie_slots = pcie_slots
        self.size = size

    def get_chipset(self):
        return self.chipset

    def get_pcie_slots(self):
        return self.pcie_slots

    def get_size(self):
        return self.size

class GPU(Component):
    def __init__(self, hwid, name, brand, model, year, price, pcie_slots, power):
        super().__init__(hwid, name, brand, model, year, price)
        self.pcie_slots = pcie_slots
        self.power = power

    def get_pcie_slots(self):
        return self.pcie_slots

    def get_power(self):
        return self.power

class Storage(Component):
    def __init__(self, hwid, name, brand, model, year, price, capacity, type, interface, size):
        super().__init__(hwid, name, brand, model, year, price)
        self.capacity = capacity
        self.type = type
        self.interface = interface
        self.size = size

    def get_capacity(self):
        return self.capacity

    def get_type(self):
        return self.type

    def get_interface(self):
        return self.interface

    def get_size(self):
        return self.size