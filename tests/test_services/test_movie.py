import pytest
from unittest.mock import patch
from app.service import MovieService

class TestMovieService:
    @pytest.fixture(autouse=True)
    @patch.object(MovieService, '__init__', lambda self: None)
    def genre_service(self, movie_dao):
        self.movie_service = MovieService()
        self.movie_service.dao = movie_dao


    def test_get_movies(self):
        all_movies = self.movie_service.get_movies()
        assert len(all_movies) > 0

    def test_get_movie_by_pk(self):
        movie = self.movie_service.get_movie_by_pk(2)
        assert movie is not None
        assert movie.id is not None

    def test_add_new_movie_with_names(self):
        data = {'some': 'data'}
        new_movie = self.movie_service.add_new_movie_with_names(**data)
        assert new_movie is not None
        assert new_movie.id is not None

    def test_add_new_movie(self):
        data = {'some': 'data'}
        new_movie = self.movie_service.add_new_movie(**data)
        assert new_movie is not None
        assert new_movie.id is not None

    def test_update_movie(self):
        data = {'some': 'data'}
        self.movie_service.update_movie(2, **data)

    def test_delete_movie(self):
        self.movie_service.delete_movie(2)