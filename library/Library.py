# -*- coding: utf-8 -*-
"""
@author: Brent Thompson & Quinn Meagher
"""

import glob

class Library:
  """
  Constructor.
  """
  def __init__(self):
      self.q = []
      pass
  
  """
  Searchs the media folder for .wav files then returns a list.
  """
  def listSongs(self):
      self.songs = []
      for file in glob.glob("*.wav"):
          self.songs.append(file)
      return self.songs

  """
  Returns queue
  """
  def listQ(self):
      return self.q
  
  """
  Adds a track to the queue if it exists in the media.
  """ 
  def addTrack(self, path):
      for file in glob.glob("*.wav"):
         if(file == path):
             self.q.append(path)
      pass
  
  """
  If the queue has songs, return the name of the next song and remove it from the list.
  """
  def nextTrack(self):
      if (len(self.q) > 0):
          self.next = self.q[0]
          del self.q[0]
      return self.next
  
  """
  Clear the queue of all songs.
  """
  def clear(self):
      del self.q[:]
      pass