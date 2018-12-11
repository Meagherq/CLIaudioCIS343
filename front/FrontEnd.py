"""
@author: Brent Thompson & Quinn Meagher
"""

import curses
import curses.textpad

from library.Library import Library
import sys, os

class FrontEnd:
  """
  Constructor.
  """
    def __init__(self, player):
        self.player = player
        os.chdir("./media")
        self.library = Library()
        
        try:
            self.player.play(sys.argv[1])
        except Exception:
            raise Exception.Audio_File_Exception
        
        try:
            curses.wrapper(self.menu)
        except Exception:
            raise Exception.Screen_Size_Exception
  """
  Holds the run loops for the program. Allows the user to
  change the current playing song add songs to a queue and more
  """
    def menu(self, args):
        self.stdscr = curses.initscr()
        self.stdscr.border()
        self.stdscr.addstr(0,0, "cli-audio",curses.A_REVERSE)
        self.stdscr.addstr(5,10, "c - Change current song")
        self.stdscr.addstr(6,10, "p - Play/Pause")
        self.stdscr.addstr(7,10, "l - Library")
        self.stdscr.addstr(8,10, "n - Next song in Queue")
        self.stdscr.addstr(9,10, "d - Clear Queue")
        self.stdscr.addstr(10,10, "q - Add song to Queue")
        self.stdscr.addstr(11,10, "a - List Queue")
        
        self.stdscr.addstr(13,10, "ESC - Quit")
        self.updateSong()
        self.stdscr.refresh()
        while True:
            c = self.stdscr.getch()
            if c == 27:
                self.quit()
                
            elif c == ord('p'):
                self.player.pause()
                
            elif c == ord('c'):
                self.changeSong()
                self.updateSong()
                self.stdscr.touchwin()
                self.stdscr.refresh()
                
            elif c == ord('l'):
                self.stdscr.addstr(18,10, str(self.library.listSongs()))
                    
            elif c == ord('n'):
                self.player.stop()
                
                try:
                    self.player.play(self.library.nextTrack())
                except Exception:
                    raise Exception.Audio_File_Exception
                    
                self.updateSong()
                
            elif c == ord('d'):
                self.library.clear()
                
            elif c == ord('q'):
                self.addSong()
                
            elif c == ord('a'):
                self.q = self.library.listQ()
                self.stdscr.addstr(17,50, "Song in Queue                                    ")
                self.x = 18
                for song in self.q:
                    self.stdscr.addstr(self.x,50, song)
                    self.x = self.x + 1 
              
  """
  Updates the song playing on the GUI 
  """
    def updateSong(self):
        self.stdscr.addstr(15,10, "                                        ")
        self.stdscr.addstr(15,10, "Now playing: " + self.player.getCurrentSong())
        
  """
  Allows the user to enter the name of a song they want to play.
  """
    def changeSong(self):
        changeWindow = curses.newwin(5, 40, 5, 50)
        changeWindow.border()
        changeWindow.addstr(0,0, "What is the file path?", curses.A_REVERSE)
        self.stdscr.refresh()
        curses.echo()
        path = changeWindow.getstr(1,1, 30)
        curses.noecho()
        del changeWindow
        self.stdscr.touchwin()
        self.stdscr.refresh()
        self.player.stop()
        try:
            self.player.play(path.decode(encoding="utf-8"))
        except Exception:
            raise Exception.Audio_File_Exception
  """
  Allows the users to enter a song to add to the queue.
  """        
    def addSong(self):
        changeWindow = curses.newwin(5, 40, 5, 50)
        changeWindow.border()
        changeWindow.addstr(0,0, "What is the file path to add?", curses.A_REVERSE)
        self.stdscr.refresh()
        curses.echo()
        path = changeWindow.getstr(1,1, 30)
        curses.noecho()
        del changeWindow
        self.stdscr.touchwin()
        self.stdscr.refresh()
        self.library.addTrack(path)
  """
  Quits the app.
  """
    def quit(self):
        self.player.stop()
        exit()
