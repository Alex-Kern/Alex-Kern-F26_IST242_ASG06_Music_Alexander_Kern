"""
Driver script demonstrating the complete Music Track hierarchy.

Run:
    python main.py

Expected output
---------------
Before sorting:
(Kendrick Lamar, Hip-Hop) DAMN. active = True,  debut year: 2017, duration: 03:40
(Alanis Morissette, Alternative) Jagged Little Pill active = False,  debut year: 1995, duration: 04:05
(Joe Rogan, Comedy) The Joe Rogan Experience active = True,  debut year: 2009, duration: 02:30:00 is explicit: True
(Sarah Koenig, Journalism) Serial active = False,  debut year: 2014, duration: 01:30:00 is explicit: False

After sorting:
(Alanis Morissette, Alternative) Jagged Little Pill active = False,  debut year: 1995, duration: 04:05
(Joe Rogan, Comedy) The Joe Rogan Experience active = True,  debut year: 2009, duration: 02:30:00 is explicit: True
(Sarah Koenig, Journalism) Serial active = False,  debut year: 2014, duration: 01:30:00 is explicit: False
(Kendrick Lamar, Hip-Hop) DAMN. active = True,  debut year: 2017, duration: 03:40
"""
from artist import Artist
from album import Album
from song import Song
from podcast import Podcast
from playlist import Playlist


def main() -> None:
    """Create sample tracks, add them to a Playlist, and sort by release year."""
    kendrick = Artist("Kendrick Lamar", "Hip-Hop")
    alanis = Artist("Alanis Morissette", "Alternative")
    rogan = Artist("Joe Rogan", "Comedy")
    koenig = Artist("Sarah Koenig", "Journalism")

    humble = Song(kendrick, Album("DAMN.", True, [2017, 2018]), 220.0)
    you_oughta_know = Song(
        alanis, Album("Jagged Little Pill", False, [1995, 1996]), 245.0
    )
    jre_ep = Podcast(
        rogan,
        Album("The Joe Rogan Experience", True, [2009, 2010]),
        9000.0,
        is_explicit=True,
    )
    serial_ep = Podcast(koenig, Album("Serial", False, [2014, 2015]), 5400.0)

    p = Playlist()
    for track in [humble, you_oughta_know, jre_ep, serial_ep]:
        p.add_track(track)

    print("Before sorting:")
    print(p)
    print()

    p.sort_by_release_year()

    print("After sorting:")
    print(p)


if __name__ == "__main__":
    main()