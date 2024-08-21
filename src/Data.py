import pygame 
import os
import random




def ReadFile(Path):
  """Reads settings from a text file and returns a dictionary.

  Args:
    Path: The path to the settings file.

  Returns:
    A dictionary containing the settings.
  """

  Setting = {}
  with open(Path, 'r', encoding='utf-8') as file:
    for Line in file:
      Line = Line.strip()
      if '=' in Line:
        Key, Value = Line.split('=')
        Setting[Key] = Value
  return Setting

# Ví dụ sử dụng:
GameSetting = 'Data\\Game\\Settings.txt'
ReadGameSetting = ReadFile(GameSetting)

GameWidth = int(ReadGameSetting['GameWidth'])
GameHeight = int(ReadGameSetting['GameHeight'])
GameFill = str(ReadGameSetting['GameFill'])








