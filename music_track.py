"""
Abstract base class for all music tracks (Songs and Podcasts).

Design decisions to implement:
  • ABC makes it impossible to instantiate MusicTrack directly — you can only
    create concrete subclasses that implement every @abstractmethod.
  • Common fields (artist, album, duration_seconds) live here so that Song and
    Podcast do not each need to repeat them.
  • release_year is a *derived* property delegating to Album.debut_year; the
    year is not stored a second time.
  • play_time_formatted() is abstract because Song and Podcast format time
    differently (MM:SS vs HH:MM:SS).
  • total_play_time() is concrete because the calculation is identical for all
    track types: duration × number of plays.
  • @functools.total_ordering generates <=, >, >= automatically from __eq__ and
    __lt__, giving us full comparison support with minimal code.
  • __hash__ is defined to stay consistent with __eq__ (Python sets __hash__ to
    None when you define __eq__, making objects unhashable unless you fix it).
"""
from abc import ABC, abstractmethod
from artist import Artist
from album import Album


class MusicTrack(ABC):
    """Abstract base class representing a generic music or audio track."""

    def __init__(self, artist: Artist, album: Album, duration_seconds: float) -> None:
        """Initialize common track attributes.

        Args:
            artist: The Artist instance associated with the track.
            album: The Album instance associated with the track.
            duration_seconds: The duration of the track in seconds.
        """
        self._artist = artist
        self._album = album
        self._duration_seconds = float(duration_seconds)

    @property
    def artist(self) -> Artist:
        """Artist: The artist or creator of the track."""
        return self._artist

    @property
    def album(self) -> Album:
        """Album: The album or collection containing the track."""
        return self._album

    @property
    def duration_seconds(self) -> float:
        """float: Track duration in seconds."""
        return self._duration_seconds

    @property
    def release_year(self) -> int:
        """int: The release year derived from the album's debut year."""
        return self._album.debut_year

    @abstractmethod
    def play_time_formatted(self) -> str:
        """Return a human-readable string representation of the track's duration."""
        pass

    def total_play_time(self, num_plays: int) -> float:
        """Calculate total duration in seconds over a given number of plays.

        Args:
            num_plays: The number of times the track is played.

        Returns:
            Total play duration in seconds.
        """
        return self._duration_seconds * num_plays