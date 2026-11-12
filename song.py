"""
Concrete subclass of MusicTrack representing a standard music track.

Song adds no new fields beyond what MusicTrack already stores.  Its only
responsibility is to:
  1. Call super().__init__() to let MusicTrack do the storage work.
  2. Implement play_time_formatted() in MM:SS format.
     Return the duration as 'MM:SS' (both parts zero-padded).

        Examples
        --------
        220 seconds → '03:40'
        65  seconds → '01:05'
        
  3. Override __str__ for a human-readable representation.
     Return '(<artist>) <album>, duration: <MM:SS>'.

        Example:
            (Kendrick Lamar, Hip-Hop) DAMN. active = True,  debut year: 2017,
            duration: 03:40
"""
from artist import Artist
from album import Album
from music_track import MusicTrack


class Song(MusicTrack):
    """Is a standard musical track with MM:SS duration formatting."""

    def __init__(self, artist: Artist, album: Album, duration_seconds: float) -> None:
        """Initialize a Song instance by delegating to MusicTrack.

        Args:
            artist: The Artist instance associated with the song.
            album: The Album instance containing the song.
            duration_seconds: The duration of the song in seconds.
        """
        super().__init__(artist, album, duration_seconds)

    def play_time_formatted(self) -> str:
        """Return the track duration formatted as 'MM:SS'."""
        total_seconds = int(self.duration_seconds)
        minutes, seconds = divmod(total_seconds, 60)
        return f"{minutes:02d}:{seconds:02d}"

    def __str__(self) -> str:
        """Return formatted string: '(<artist>) <album>, duration: <MM:SS>'."""
        return f"({self.artist}) {self.album}, duration: {self.play_time_formatted()}"