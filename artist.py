"""
Represents a musical artist or podcast creator.

This is the simplest class in the hierarchy — no dependencies, no validation.
It introduces two core Python OOP conventions:
  1. The single leading-underscore (_name) signals a non-public attribute.
  2. @property exposes a clean public getter without allowing direct mutation.
"""

class Artist:
    """Represents an artist or creator associated with a track or album."""

    def __init__(self, name: str, genre: str) -> None:
        """Initialize an Artist instance with name and genre.

        Args:
            name: The name of the artist or show creator.
            genre: The primary musical or content genre.
        """
        self._name = name
        self._genre = genre

    @property
    def name(self) -> str:
        """str: The name of the artist."""
        return self._name

    @property
    def genre(self) -> str:
        """str: The primary genre of the artist."""
        return self._genre

    def __str__(self) -> str:
        """Return a string representation in the format '<name>, <genre>'."""
        return f"{self._name}, {self._genre}"