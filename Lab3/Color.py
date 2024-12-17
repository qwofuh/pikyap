class Color:

    def __init__(self):
        self.color = ""

    @property
    def colorName(self):
        return self.color
    
    @colorName.setter
    def colorName(self, color:str):
        self.color = color