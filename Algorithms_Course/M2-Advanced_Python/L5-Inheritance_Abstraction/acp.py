from abc import ABC, abstractmethod

# Abstract parent class
class Instrument(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

# Child class
class Guitar(Instrument):
    def __init__(self):
        super().__init__("Guitar")

    def sound(self):
        print(self.name, "makes the sound: Strum Strum")

# Child class
class Piano(Instrument):
    def __init__(self):
        super().__init__("Piano")

    def sound(self):
        print(self.name, "makes the sound: Ting Ting")

# Child class
class Drum(Instrument):
    def __init__(self):
        super().__init__("Drum")

    def sound(self):
        print(self.name, "makes the sound: Boom Boom")

# Create objects
guitar = Guitar()
piano = Piano()
drum = Drum()

# Display sounds
guitar.sound()
piano.sound()
drum.sound()