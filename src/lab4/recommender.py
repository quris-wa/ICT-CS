from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Optional, Iterable
import sys



@dataclass
class Movie:
    """
    Movie object with id and title.
    It keeps simple information about a film.
    """
    movie_id: int
    title: str


@dataclass
class HistoryRecord:
    """
    One user watching history.
    It stores a list of movie ids watched by one person.
    """
    movie_ids: List[int]



class MovieFileReader:
    """
    This class reads movies from a text file.
    Each line has: id,title
    """
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.movies: Dict[int, Movie] = {}
        self._load()

    def _load(self) -> None:
        """Read file line by line and load movies into a dictionary."""
        with self.file_path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",", 1)
                if len(parts) != 2:
                    continue

                id_str, title = parts
                id_str = id_str.strip()
                title = title.strip()

                if not id_str or not title:
                    continue

                try:
                    movie_id = int(id_str)
                except ValueError:
                    continue

                self.movies[movie_id] = Movie(movie_id=movie_id, title=title)

    def find_by_id(self, movie_id: int) -> Optional[Movie]:
        """Return movie object by id. Return None if not found."""
        return self.movies.get(movie_id)

    def get_all(self) -> Iterable[Movie]:
        """Return list of all movies."""
        return self.movies.values()


class HistoryFileReader:
    """
    This class reads watching history from a text file.
    Each line is a list of movie ids: 2,1,3
    """
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.records: List[HistoryRecord] = []
        self._load()

    def _load(self) -> None:
        with self.file_path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",")

                movie_ids: List[int] = []
                for part in parts:
                    part = part.strip()
                    if not part:
                        continue
                    try:
                        movie_ids.append(int(part))
                    except ValueError:
                        continue

                if movie_ids:
                    self.records.append(HistoryRecord(movie_ids=movie_ids))

    def get_all(self) -> List[HistoryRecord]:
        """Return list of all history records."""
        return list(self.records)



class Recommender:
    """
    This class gives a movie recommendation.
    It uses watching history from many users.
    The idea: find users who watched similar movies.
    """

    def __init__(self, movie_reader: MovieFileReader, history_reader: HistoryFileReader):
        self.movie_reader = movie_reader
        self.history_reader = history_reader

    def recommend(self, user_movie_ids: List[int]) -> Optional[Movie]:
        """
        Recommend one movie for the current user.
        """
        user_movie_ids = list(dict.fromkeys(user_movie_ids))
        if not user_movie_ids:
            return None

        watched = set(user_movie_ids)
        user_size = len(watched)

        scores: Dict[int, float] = {}

        for record in self.history_reader.get_all():
            history_set = set(record.movie_ids)

            common_count = sum(1 for m in watched if m in history_set)
            similarity = common_count / user_size

            if similarity < 0.5:
                continue

            for movie_id in record.movie_ids:
                if movie_id in watched:
                    continue
                scores[movie_id] = scores.get(movie_id, 0.0) + similarity

        if not scores:
            return None

        best_movie_id = max(scores.items(), key=lambda kv: kv[1])[0]
        return self.movie_reader.find_by_id(best_movie_id)


def parse_user_input(line: str) -> List[int]:
    """
    Convert a string like "2, 4 , 1" into a list of numbers.
    """
    result: List[int] = []
    for part in line.split(","):
        part = part.strip()
        if not part:
            continue
        try:
            result.append(int(part))
        except ValueError:
            continue
    return result


def main() -> None:
    movie_reader = MovieFileReader(Path("movies.txt"))
    history_reader = HistoryFileReader(Path("history.txt"))
    recommender = Recommender(movie_reader, history_reader)

    line = sys.stdin.readline()
    if not line:
        return

    user_movie_ids = parse_user_input(line.strip())
    movie = recommender.recommend(user_movie_ids)

    if movie is not None:
        print(movie.title)
    else:
        print("Нет рекомендаций")


if __name__ == "__main__":
    main()
