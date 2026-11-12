"""
Concrete subclass of MusicTrack representing a podcast episode.

Podcast differs from Song in two ways:
  1. It has one extra field: is_explicit (bool), defaulting to False.
     The default value replaces Java-style constructor overloading — one
     __init__ handles both the explicit and non-explicit cases.
  2. play_time_formatted() returns 'HH:MM:SS' instead of 'MM:SS', because
     podcast episodes are typically longer than an hour.

    Return the duration as 'HH:MM:SS' (all parts zero-padded).

        Examples
        --------
        9000 seconds → '02:30:00'
        5400 seconds → '01:30:00'
        3661 seconds → '01:01:01'

 3. Override __str__ for a human-readable representation.
        Return '(<artist>) <album>, duration: <HH:MM:SS> is explicit: <bool>'.

        Example:
            (Joe Rogan, Comedy) The Joe Rogan Experience active = True,
             debut year: 2009, duration: 02:30:00 is explicit: True
"""
from artist import Artist
from album import Album
from music_track import MusicTrack


class Podcast(MusicTrack):
    """Represents a podcast episode with HH:MM:SS formatting and explicit flag."""

    def __init__(
        self,
        artist: Artist,
        album: Album,
        duration_seconds: float,
        is_explicit: bool = False,
    ) -> None:
        """Initialize a Podcast instance.

        Args:
            artist: The Artist (host/creator) associated with the podcast.
            album: The Album (show/series) containing the episode.
            duration_seconds: The duration of the episode in seconds.
            is_explicit: Whether the episode contains explicit content. Defaults to False.
        """
        super().__init__(artist, album, duration_seconds)
        self._is_explicit = is_explicit

    @property
    def is_explicit(self) -> bool:
        """bool: Whether the episode contains explicit content."""
        return self._is_explicit

    def play_time_formatted(self) -> str:
        """Return the episode duration formatted as 'HH:MM:SS'."""
        total_seconds = int(self.duration_seconds)
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def __str__(self) -> str:
        """Return formatted string: '(<artist>) <album>, duration: <HH:MM:SS> is explicit: <bool>'."""
        return (
            f"({self.artist}) {self.album}, "
            f"duration: {self.play_time_formatted()} is explicit: {self._is_explicit}"
        )