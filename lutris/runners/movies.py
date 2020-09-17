 """Runner for Watching Movies"""
import os
import stat
from lutris.runners.runner import Runner
from lutris.util import system
from gi.repository import GLib

#Based off lutris.runners.linux
class movies(Runner):
    human_name = "Movies"
    description = "Plays your local movies"
    platforms = ["Linux"]
    runner_executable = True
    game_options = []
    
    runner_options = [ 
        {
            "option": "folder",
            "type": "file",
            "default_path": GLib.UserDirectory.DIRECTORY_MUSIC,
            "label": "Directory",
            "help": "The folder containing your movies",
        },
#        {
#            "option": "prog",
#            "type": "program",
#            "default_program": os.
#            "label": "Video player"
#        },
    ]

    def __init__(self, config=None):
        super(movies, self).__init__(config)
        
        
        
    @property
    def name(self):
        
    def run(self, *args):
        
    
    def play(self):
        
    
