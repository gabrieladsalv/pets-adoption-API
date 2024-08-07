from typing import List
from src.models.sqlite.entities.pets import PetsTable
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface

class PetsRepository(PetsRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
        
    def list_pets(self) -> List[PetsTable]:
        with self.__db_connection as database:
            try:
                pets = database.session.query(PetsTable).all()
                return pets
            except NoResultFound:
                return []
                
                
    def delete_pets(self, pet:str) -> None:
        with self.__db_connection as database:
            try:
                pet = database.session.query(PetsTable).filter(PetsTable.pet_name == pet).delete()
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
        