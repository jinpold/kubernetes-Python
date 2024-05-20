from abc import *
from abc import ABCMeta, abstractmethod

#추상화 클래스

class PrinterBase(metaclass=ABCMeta):
    @abstractmethod
    def print(self):
        pass

class ReaderBase(metaclass=ABCMeta):

    @abstractmethod
    def csv(self):
        pass

    @abstractmethod
    def xls(self):
        pass

    @abstractmethod
    def json(self):
        pass

    @abstractmethod
    def gmaps(self):
        pass

class ScraperBase(metaclass=ABCMeta):
    @abstractmethod
    def driver(self):
        pass