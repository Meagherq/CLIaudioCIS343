# -*- coding: utf-8 -*-
"""
@author: Brent Thompson & Quinn Meagher
"""

"""
Exception to be thrown when there is an error.
"""
class Audio_Exception(Exception):
   
    pass

"""
Child exception to be thrown when there is an audio file error.
"""
class Audio_File_Exception(Audio_Exception):
 
    pass

"""
Child exception to be thrown when there is an screen size error.
"""
class Screen_Size_Exception(Audio_Exception):
  
    pass