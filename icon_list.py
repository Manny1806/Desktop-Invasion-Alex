import os

class IconList():
    def __init__(self):
        self.icon_list = []
        for root, dirs, files in os.walk("./images/icons"):  
            for filename in files:
                self.icon_list.append(filename)