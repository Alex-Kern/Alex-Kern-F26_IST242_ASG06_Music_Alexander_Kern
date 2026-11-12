"""
A collection class that holds MusicTrack objects (Songs and Podcasts).

Design notes:
  • _tracks is kept private (single underscore) and exposed as a *copy*
    through the `tracks` property to protect encapsulation.
  • clear_playlist() uses list.clear() rather than rebinding to None or a new
    list, so the internal object reference stays valid.
  • sort_by_release_year() delegates to list.sort(), which in turn calls
    MusicTrack.__lt__ — the comparison logic defined in Part 3 pays off here.
  • __str__ uses a generator expression with str.join() for a concise
    multi-line string without building an intermediate list manually.
"""
from music_track import MusicTrack


class Playlist:
    """Manages an ordered collection of MusicTrack objects."""

    def __init__(self) -> None:
        """Initialize an empty Playlist."""
        self._tracks: list[MusicTrack] = []

    @property
    def tracks(self) -> list[MusicTrack]:
        """list[MusicTrack]: A copy of the internal tracks list."""
        return list(self._tracks)

    def add_track(self, track: MusicTrack) -> None:
        """Append a MusicTrack to the playlist.

        Args:
            track: The Song or Podcast instance to add.
        """
        self._tracks.append(track)

    def clear_playlist(self) -> None:
        """Remove all tracks from the playlist in place."""
        self._tracks.clear()

    def sort_by_release_year(self) -> None:
        """Sort tracks in place by ascending release year."""
        self._tracks.sort()

    def __str__(self) -> str:
        """Return each track on its own line, or empty string if empty."""
        return "\n".join(str(track) for track in self._tracks)