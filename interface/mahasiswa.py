from abc import ABC, abstractmethod
from entity.mahasiswa import MahasiswaEntity

class MahasiswaAbstract(ABC):
    def create_mahasiswa(self, mhs: MahasiswaEntity):
        ...

    def delete_mahasiswa(self, nim: str):
        ...

    def get_all_mahasiswa(self):
        ...