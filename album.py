"""
Represents a music album or podcast series, including the years it was active.

Key concepts to implement:
  • Input validation in __init__ (fail-fast with a clear ValueError).
  • Defensive copy on both input and output so external code cannot corrupt
    the internal years list.
  • A *derived* property (debut_year) that computes its value from stored data
    rather than keeping a second field in sync.
"""

class Album:
    """Represents an album or series releasing content over one or more years."""

    def __init__(self, title: str, active: bool, years: list[int]) -> None:
        """Initialize an Album instance.

        Args:
            title: The title of the album or series.
            active: Whether the album or series is currently active.
            years: Non-empty list of years content was released.

        Raises:
            ValueError: If years is empty.
        """
        if not years:
            raise ValueError(f"Album '{title}' years list cannot be empty.")

        self._title = title
        self._active = active
        # Defensive copy on input
        self._years = list(years)

    @property
    def title(self) -> str:
        """str: The title of the album or series."""
        return self._title

    @property
    def active(self) -> bool:
        """bool: Whether the album or series is currently active."""
        return self._active

    @property
    def years(self) -> list[int]:
        """list[int]: A copy of the years released."""
        # Defensive copy on output
        return list(self._years)

    @property
    def debut_year(self) -> int:
        """int: The initial debut release year."""
        return self._years[0]

    def __str__(self) -> str:
        """Return formatted string: '<title> active = <active>, debut year: <first-year>'."""
        return f"{self._title} active = {self._active}, debut year: {self.debut_year}"