from flask_restx import reqparse

movie_parser = reqparse.RequestParser()
movie_parser.add_argument('title', type=str, help='Movie title', nullable=False, required=True)
movie_parser.add_argument('description', type=str, help='Movie description', nullable=True, required=True)
movie_parser.add_argument('trailer', type=str, help='Trailer link', nullable=True, required=True)
movie_parser.add_argument('year', type=int, help='Release year', nullable=False, required=True)
movie_parser.add_argument('rating', type=float, help='Movie rating', nullable=False, required=True)
movie_parser.add_argument('genre_id', type=int, help='Genre id', nullable=False, required=True)
movie_parser.add_argument('director_id', type=int, help='Director id', nullable=False, required=True)


movie_query_parser = reqparse.RequestParser()
movie_query_parser.add_argument('director_id', type=int, help='director_id for filtering')
movie_query_parser.add_argument('genre_id', type=int, help='genre_id for filtering')
