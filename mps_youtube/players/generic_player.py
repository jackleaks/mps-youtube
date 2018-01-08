import os
import subprocess

from .. import config

from ..player import Player

#
# This class can be used as a templete for new players
#
# NOTE:
# If you're defining a new player donot forget
# to add player to assign_player() function in util.
#


class generic_player(Player):
    def _generate_real_playerargs(self, song, override, stream, isvideo, softrepeat):
        '''Generates player arguments to called using Popen

        '''
        args = config.PLAYERARGS.get.strip().split()

        ############################################
        # Define your arguments below this line

        ###########################################

        return [config.PLAYER.get] + args + [stream['url']]

    def clean_up(self):
        ''' Cleans up temp files after process exits.

        '''
        pass

    def launch_player(self, cmd, song, songdata):

        ##################################################
        # Change this however you want

        with open(os.devnull, "w") as devnull:
            self.p = subprocess.Popen(cmd, shell=False, stderr=devnull)
        returncode = self.p.wait()

        ##################################################

        # Donot forget self.stop()
        self.next()

    def _help(self, short=True):
        ''' Help keys shown when the song is played.

        See mpv.py for reference.

        '''
        pass
