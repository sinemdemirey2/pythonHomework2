"""
Define a class called Songs, it will show the lyrics of a song.
Its __init__() method should have two arguments:selfanf lyrics.lyricsis a list.
Inside your class create a method called sing_me_a_songthat prints each element of lyricson his own line. Define a varible:

happy_bday = Song(["May god bless you, ",
                   "Have a sunshine on you,",
                   "Happy Birthday to you !"])
Call the sing_me_songmehod on this variable.
"""
class Songs:
    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Songs(["May god bless you,", "Have a sunshine on you,", "Happy Birthday to you !"])

happy_bday.sing_me_a_song()