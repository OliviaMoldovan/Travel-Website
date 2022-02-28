"The Command Pattern Concept"
from abc import ABCMeta, abstractmethod

from travelapp.models import Book, Holiday, User, Airplane, Hotel


class ICommand(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    "The command interface, that all commands will implement"

    @staticmethod
    @abstractmethod
    def execute():
        "The required execute method that all command objects will use"


class Invoker:
    "The Invoker Class"

    def __init__(self):
        self._commands = {}

    def register(self, book, command):
        "Register commands in the Invoker"
        self._commands[book] = command

    def execute(self, book):
        "Execute any registered commands"
        if book in self._commands.keys():
            self._commands[book].execute()
        else:
            print(f"Command [{book}] not recognised")


class Receiver:
    "The Receiver"

    def __init__(self, holiday_id, user):
        self.holiday_id = holiday_id
        self.user = user

    @staticmethod
    def run_command(self):
        "A set of instructions to run"
        holidayFinal = Holiday.objects.get(ID=self.holiday_id)
        book = Book(DataInceperii=holidayFinal.Data,
                    Durata=holidayFinal.Durata,
                    NrAdulti=holidayFinal.NrAdulti,
                    NrCopii=0,
                    Pret=holidayFinal.Pret,
                    Avion_id=holidayFinal.Avion,
                    Hotel_id=holidayFinal.Hotel,
                    Client_id=self.user,
                    Destinatie=holidayFinal.Destinatie)
        book.save()


class BookCommand(ICommand):  # pylint: disable=too-few-public-methods
    """A Command object, that implements the ICommand interface and
    runs the command on the designated receiver"""

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.run_command(self.receiver)
