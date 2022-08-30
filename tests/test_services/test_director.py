import pytest
from unittest.mock import patch
from app.service import DirectorService

class TestDirectorService:
    @pytest.fixture(autouse=True)
    @patch.object(DirectorService, '__init__', lambda self: None)
    def genre_service(self, director_dao):
        self.director_service = DirectorService()
        self.director_service.dao = director_dao

    def test_get_directors(self):
        all_directors = self.director_service.get_directors()
        assert len(all_directors) > 0

    def test_get_director_by_pk(self):
        director = self.director_service.get_director_by_pk(2)
        assert director is not None
        assert director.id is not None

    def test_add_new_director(self):
        data = {'name':  'new_Genre'}
        new_director = self.director_service.add_new_director(**data)
        assert new_director.id is not None


    def test_update_director(self):
        data = {'name':  'changed_genre'}
        self.director_service.update_director(1, **data)

    def test_delete_director(self):
        self.director_service.delete_director(1)
