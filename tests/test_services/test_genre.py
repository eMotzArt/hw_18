import pytest
from unittest.mock import patch
from app.service import GenreService

class TestGenreService:
    @pytest.fixture(autouse=True)
    @patch.object(GenreService, '__init__', lambda self: None)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService()
        self.genre_service.dao = genre_dao

    def test_get_genres(self):
        all_genres = self.genre_service.get_genres()
        assert len(all_genres) > 0

    def test_get_genre_by_pk(self):
        genre = self.genre_service.get_genre_by_pk(2)
        assert genre is not None
        assert genre.id is not None

    def test_add_new_genre(self):
        data = {'name':  'new_Genre'}
        new_genre = self.genre_service.add_new_genre(**data)
        assert new_genre.id is not None


    def test_update_genre(self):
        data = {'name':  'changed_genre'}
        self.genre_service.update_genre(1, **data)

    def test_delete_genre(self):
        self.genre_service.delete_genre(1)
