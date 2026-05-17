from abc import ABC,abstractmethod

#Abstract class

class Vehicle(ABC):

    @abstractmethod
    def engine_start(self):
        pass           # placeholder with abstract method with no implementation

    @abstractmethod
    def engine_performance(self):
        pass            # placeholder with abstract method with no implementation


    @abstractmethod
    def engine_stop(self):
        pass              # placeholder with abstract method with no implementation


# class for Implementation

class Hyundai_car(Vehicle):
   
    def engine_start(self):
        print("Car is starting properly. Tested and looks fine")

    
    def engine_performance(self):
        print("Performance efficiency is good")


   
    def engine_stop(self):
        print("After Brake, Car stops properly. No friction")


obj01 = Hyundai_car()
obj01.engine_performance()
obj01.engine_start()
obj01.engine_stop()