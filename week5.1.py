class Device:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


class Smartphone(Device):
    def __init__(self, brand, model, year, os, storage):
        
        super().__init__(brand, model, year)
        self.os = os
        self.storage = storage

    def make_call(self, number):
        print(f"Calling {number}...")

    def display_info(self):
        super().display_info()
        print(f"Operating System: {self.os}")
        print(f"Storage: {self.storage} GB")

