class ComponentController:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_component(self, component):
        cursor = self.db_connection.cursor()
        sql = "INSERT INTO Components (HWID, Name, Brand, Model, Year, Price) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (component.get_hwid(), component.get_name(), component.get_brand(), component.get_model(), component.get_year(), component.get_price()))
        self.db_connection.commit()

    def retrieve_component(self, hwid):
        cursor = self.db_connection.cursor()
        sql = "SELECT * FROM Components WHERE HWID = %s"
        cursor.execute(sql, (hwid,))
        return cursor.fetchone()

    def dynamic_retrieve_components(self, columns):
        cursor = self.db_connection.cursor()
        cols = ", ".join([str(column) for column in columns])
        sql = f"SELECT {cols} FROM Components"
        cursor.execute(sql)
        return cursor.fetchall()

    def retrieve_all_components(self):
        cursor = self.db_connection.cursor()
        sql = "SELECT * FROM Components"
        cursor.execute(sql)
        return cursor.fetchall()

    def retrieve_components_by_criteria(self, min_price=None, max_price=None, min_year=None, max_year=None):
        cursor = self.db_connection.cursor()
        sql = "SELECT * FROM Components"
        conditions = []
        params = []
        if min_price is not None:
            conditions.append("Price >= %s")
            params.append(min_price)
        if max_price is not None:
            conditions.append("Price <= %s")
            params.append(max_price)
        if min_year is not None:
            conditions.append("Year >= %s")
            params.append(min_year)
        if max_year is not None:
            conditions.append("Year <= %s")
            params.append(max_year)
        if conditions:
            sql += " WHERE " + " AND ".join(conditions)
        cursor.execute(sql, tuple(params))
        return cursor.fetchall()

    def update_component(self, component):
        cursor = self.db_connection.cursor()
        sql = "UPDATE Components SET Name = %s, Brand = %s, Model = %s, Year = %s, Price = %s WHERE HWID = %s"
        cursor.execute(sql, (component.get_name(), component.get_brand(), component.get_model(), component.get_year(), component.get_price(), component.get_hwid()))
        self.db_connection.commit()

    def delete_component(self, hwid):
        cursor = self.db_connection.cursor()
        sql = "DELETE FROM Components WHERE HWID = %s"
        cursor.execute(sql, (hwid,))
        self.db_connection.commit()

class CPUController:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.component_controller = ComponentController(db_connection)

    def create_cpu(self, cpu):
        self.component_controller.create_component(cpu)
        cursor = self.db_connection.cursor()
        sql = "INSERT INTO CPU (HWID, Cores, ClockSpeed, Chipset, TDP) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (cpu.get_hwid(), cpu.get_cores(), cpu.get_clock_speed(), cpu.get_chipset(), cpu.get_tdp()))
        self.db_connection.commit()

    def retrieve_cpu(self, hwid):
        cursor = self.db_connection.cursor()
        sql = "SELECT * FROM CPU WHERE HWID = %s"
        cursor.execute(sql, (hwid,))
        return cursor.fetchone()

    def retrieve_all_cpus(self):
        cursor = self.db_connection.cursor()
        sql = "SELECT * FROM CPU"
        cursor.execute(sql)
        return cursor.fetchall()

    def update_cpu(self, cpu):
        self.component_controller.update_component(cpu)
        cursor = self.db_connection.cursor()
        sql = "UPDATE CPU SET Cores = %s, ClockSpeed = %s, Chipset = %s, TDP = %s WHERE HWID = %s"
        cursor.execute(sql, (cpu.get_cores(), cpu.get_clock_speed(), cpu.get_chipset(), cpu.get_tdp(), cpu.get_hwid()))
        self.db_connection.commit()

    def delete_cpu(self, hwid):
        cursor = self.db_connection.cursor()
        sql = "DELETE FROM CPU WHERE HWID = %s"
        cursor.execute(sql, (hwid,))
        self.component_controller.delete_component(hwid)
        self.db_connection.commit()

class MotherboardController:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.component_controller = ComponentController(db_connection)

    def create_motherboard(self, motherboard):
        self.component_controller.create_component(motherboard)
        cursor = self.db_connection.cursor()
        sql = "INSERT INTO Motherboard (HWID, Chipset, PcieSlots, Size) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (motherboard.get_hwid(), motherboard.get_chipset(), motherboard.get_pcie_slots(), motherboard.get_size()))
        self.db_connection.commit()

    def retrieve_motherboard(self, hwid):
        cursor = self.db_connection.cursor()
        sql = "SELECT * FROM Motherboard WHERE HWID = %s"
        cursor.execute(sql, (hwid,))
        return cursor.fetchone()

    def retrieve_all_motherboards(self):
        cursor = self.db_connection.cursor()
        sql = "SELECT * FROM Motherboard"
        cursor.execute(sql)
        return cursor.fetchall()

    def update_motherboard(self, motherboard):
        self.component_controller.update_component(motherboard)
        cursor = self.db_connection.cursor()
        sql = "UPDATE Motherboard SET Chipset = %s, PcieSlots = %s, Size = %s WHERE HWID = %s"
        cursor.execute(sql, (motherboard.get_chipset(), motherboard.get_pcie_slots(), motherboard.get_size(), motherboard.get_hwid()))
        self.db_connection.commit()

    def delete_motherboard(self, hwid):
        cursor = self.db_connection.cursor()
        sql = "DELETE FROM Motherboard WHERE HWID = %s"
        cursor.execute(sql, (hwid,))
        self.component_controller.delete_component(hwid)
        self.db_connection.commit()

class GPUController:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.component_controller = ComponentController(db_connection)

    def create_gpu(self, gpu):
        self.component_controller.create_component(gpu)
        cursor = self.db_connection.cursor()
        sql = "INSERT INTO GPU (HWID, PcieSlots, Power) VALUES (%s, %s, %s)"
        cursor.execute(sql, (gpu.get_hwid(), gpu.get_pcie_slots(), gpu.get_power()))
        self.db_connection.commit()

    def retrieve_gpu(self, hwid):
        cursor = self.db_connection.cursor()
        sql = "SELECT * FROM GPU WHERE HWID = %s"
        cursor.execute(sql, (hwid,))
        return cursor.fetchone()

    def retrieve_all_gpus(self):
        cursor = self.db_connection.cursor()
        sql = "SELECT * FROM GPU"
        cursor.execute(sql)
        return cursor.fetchall()

    def update_gpu(self, gpu):
        self.component_controller.update_component(gpu)
        cursor = self.db_connection.cursor()
        sql = "UPDATE GPU SET PcieSlots = %s, Power = %s WHERE HWID = %s"
        cursor.execute(sql, (gpu.get_pcie_slots(), gpu.get_power(), gpu.get_hwid()))
        self.db_connection.commit()

    def delete_gpu(self, hwid):
        cursor = self.db_connection.cursor()
        sql = "DELETE FROM GPU WHERE HWID = %s"
        cursor.execute(sql, (hwid,))
        self.component_controller.delete_component(hwid)
        self.db_connection.commit()

class StorageController:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.component_controller = ComponentController(db_connection)

    def create_storage(self, storage):
        self.component_controller.create_component(storage)
        cursor = self.db_connection.cursor()
        sql = "INSERT INTO Storage (HWID, Capacity, Type, Interface, Size) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (storage.get_hwid(), storage.get_capacity(), storage.get_type(), storage.get_interface(), storage.get_size()))
        self.db_connection.commit()

    def retrieve_storage(self, hwid):
        cursor = self.db_connection.cursor()
        sql = "SELECT * FROM Storage WHERE HWID = %s"
        cursor.execute(sql, (hwid,))
        return cursor.fetchone()

    def retrieve_all_storages(self):
        cursor = self.db_connection.cursor()
        sql = "SELECT * FROM Storage"
        cursor.execute(sql)
        return cursor.fetchall()

    def update_storage(self, storage):
        self.component_controller.update_component(storage)
        cursor = self.db_connection.cursor()
        sql = "UPDATE Storage SET Capacity = %s, Type = %s, Interface = %s, Size = %s WHERE HWID = %s"
        cursor.execute(sql, (storage.get_capacity(), storage.get_type(), storage.get_interface(), storage.get_size(), storage.get_hwid()))
        self.db_connection.commit()

    def delete_storage(self, hwid):
        cursor = self.db_connection.cursor()
        sql = "DELETE FROM Storage WHERE HWID = %s"
        cursor.execute(sql, (hwid,))
        self.component_controller.delete_component(hwid)
        self.db_connection.commit()
