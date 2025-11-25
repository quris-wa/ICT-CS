"""
Tests for movie recommender logic.
They check if recommendation works correctly.
"""

import unittest
from typing import List
from src.lab4.recommender import Movie, HistoryRecord, Recommender, parse_user_input


class FakeMovieReader:
    """
    Simple fake movie reader for tests.
    It does not read from file.
    """

    def __init__(self, movies: List[Movie]):
        self._movies = {m.movie_id: m for m in movies}

    def find_by_id(self, movie_id: int):
        """Return movie by id or None."""
        return self._movies.get(movie_id)

    def get_all(self):
        """Return list of all movies."""
        return list(self._movies.values())


class FakeHistoryReader:
    """
    Simple fake history reader for tests.
    It returns predefined history records.
    """

    def __init__(self, records: List[HistoryRecord]):
        self._records = list(records)

    def get_all(self):
        """Return list of all history records."""
        return list(self._records)


class RecommenderTests(unittest.TestCase):
    """
    Test class for Recommender.
    It checks main cases of the algorithm.
    """

    def setUp(self):
        """Create common test data for all tests."""
        self.movies = [
            Movie(1, "Мстители: Финал"),
            Movie(2, "Хатико"),
            Movie(3, "Дюна"),
            Movie(4, "Унесенные призраками"),
        ]
        self.movie_reader = FakeMovieReader(self.movies)

        self.histories = [
            HistoryRecord([2, 1, 3]),
            HistoryRecord([1, 4, 3]),
            HistoryRecord([2, 2, 2, 2, 2, 3]),
        ]
        self.history_reader = FakeHistoryReader(self.histories)

        self.recommender = Recommender(self.movie_reader, self.history_reader)

    def test_example_from_task_returns_dune(self):
        """
        Example from the task:
        user watched 2 and 4, result should be 'Дюна'.
        """
        user_movies = [2, 4]
        result = self.recommender.recommend(user_movies)

        self.assertIsNotNone(result)
        self.assertEqual("Дюна", result.title)

    def test_empty_user_list_returns_none(self):
        """
        If user has no movies, there is no recommendation.
        """
        result = self.recommender.recommend([])
        self.assertIsNone(result)

    def test_all_movies_already_watched(self):
        """
        If user watched all movies, there is nothing to recommend.
        """
        user_movies = [1, 2, 3, 4]
        result = self.recommender.recommend(user_movies)
        self.assertIsNone(result)

    def test_no_history_records(self):
        """
        If history is empty, there is no recommendation.
        """
        empty_history_reader = FakeHistoryReader([])
        recommender = Recommender(self.movie_reader, empty_history_reader)

        result = recommender.recommend([1, 2])
        self.assertIsNone(result)

    def test_parse_user_input(self):
        """
        Check that parse_user_input works with spaces and bad values.
        """
        line = " 1,  2, x,  3 , , 4 "
        numbers = parse_user_input(line)
        self.assertEqual([1, 2, 3, 4], numbers)


if __name__ == "__main__":
    unittest.main()
