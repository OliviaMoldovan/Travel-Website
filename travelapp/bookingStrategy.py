from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self) -> str:
        pass


class HotelStrategy(Strategy):
    def __init__(self, HotelPret, Durata):
        self.hotelPret = HotelPret
        self.durata = Durata

    def execute(self) -> str:
        pret = self.durata * self.hotelPret
        return pret


class AirplaneStrategy(Strategy):
    def __init__(self, AvionPret, NrAdulti, NrCopii):
        self.avionPret = AvionPret
        self.nrAdulti = NrAdulti
        self.nrCopii = NrCopii

    def execute(self) -> str:
        pret = self.avionPret * (self.nrAdulti + self.nrCopii * 0.5)
        return pret


class Default(Strategy):
    def __init__(self, HotelPret, Durata, AvionPret, NrAdulti, NrCopii):
        self.hotelPret = HotelPret
        self.durata = Durata
        self.avionPret = AvionPret
        self.nrAdulti = NrAdulti
        self.nrCopii = NrCopii

    def execute(self) -> str:
        pret = self.avionPret * (self.nrAdulti + self.nrCopii * 0.5) + (self.hotelPret * self.durata)
        return pret
