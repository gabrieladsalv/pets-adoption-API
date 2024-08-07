import pytest
from .person_creator_controller import PersonCreatorController


class MockPeopleRepository:
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int):
        pass

def test_create():
    person_info = {
        'first_name': 'John',
        'last_name': 'Doe',
        'age': 30,
        'pet_id': 2
    }
    
    controller = PersonCreatorController(MockPeopleRepository())
    response = controller.create(person_info)

    assert response['data']['type'] == 'person'
    assert response['data']['id'] == person_info['id']
    assert response['data']['attributes'] == person_info
    

def test_create_error():
    person_info = {
        'first_name': 'John3',
        'last_name': 'Doe',
        'age': 30,
        'pet_id': 2
    }
    
    controller = PersonCreatorController(MockPeopleRepository())
    with pytest.raises(Exception):
        controller.create(person_info)
