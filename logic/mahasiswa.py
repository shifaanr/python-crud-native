from interface import MahasiswaAbstract
from entity.mahasiswa import MahasiswaEntity


class MahasiswaLogic:
    def __init__(self, repo: MahasiswaAbstract):
        self.repo = repo

    def create(self, entity: MahasiswaEntity):
        self.repo.create_mahasiswa(entity)

    def creates(self, entities: list[MahasiswaEntity]):
        for ent in entities:
            self.create(ent)

    def delete(self, nim: str):
        self.repo.delete_mahasiswa(nim)

    def get_all(self):
        return self.repo.get_all_mahasiswa()

    def update(self, nim, address, name: str):
        self.repo.update_mahasiswa(nim, address, name)
