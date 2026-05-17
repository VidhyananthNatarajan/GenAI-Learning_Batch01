from Learn_BaseClass import BaseClass

class Method_Overridding(BaseClass):

    def method01(self):
        print("Logic changed")

obj02 = Method_Overridding()

obj02.method01()