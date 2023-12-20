from abc import ABC, abstractmethod
from entity.mahasiswa import MahasiswaEntity


class MahasiswaAbstract(ABC):
    def create_mahasiswa(self, mhs: MahasiswaEntity):
        ...

    def delete_mahasiswa(self, nim: str):
        ...

    def update_mahasiswa(self, nim: str, name, address):
        ...

    def get_all_mahasiswa(self):
        ...
