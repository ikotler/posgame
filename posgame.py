#!/usr/bin/env python3
# Copyright (c) 2020, Itzik Kotler
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    1. Redistributions of source code must retain the above copyright notice, this
#       list of conditions and the following disclaimer.
#
#    2. Redistributions in binary form must reproduce the above copyright notice,
#       this list of conditions and the following disclaimer in the documentation
#       and/or other materials provided with the distribution.
#
#    3. Neither the name of the copyright holder nor the names of its
#       contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import time
import collections
import random
import msvcrt

##########
# Consts #
##########

WIN_DEV = "//./LCLD9/"

# I'm sure there's a better way to implement it, but it works :-)
A_GOOD_PLACE_IN_THE_MIDDLE = "\t\t\t\t\t\t\t\t "

###########
# Classes #
###########

class POSDisplay:
    def __init__(self, path):
        self.dev = open(path, 'w+t')

    def clear(self):
        self.dev.write('\x1f')
        self.dev.flush()

    def write(self, buf):
        self.dev.write(buf)
        self.dev.flush()

    def cursor_off(self):
        self.dev.write('\x14')
        self.dev.flush()

#############
# Functions #
#############

def banner(scr):
    scr.clear()
    scr.write(" WELCOME TO POSGAME\n* * * * * * * * * *")
    time.sleep(2)

def countdown(scr, n):
    for i in range(n, 0, -1):
        scr.clear()
        scr.write("{}{}".format(A_GOOD_PLACE_IN_THE_MIDDLE,i))
        time.sleep(1)

    scr.clear()
    scr.write("{}GO!".format(A_GOOD_PLACE_IN_THE_MIDDLE))
    time.sleep(1)

def main():
    buf = collections.deque(maxlen=19)
    gap = False
    cur_avatar_chr = 'o'
    cur_avatar_life = 3
    cur_hiscore = 0
    scr = POSDisplay(WIN_DEV)

    # Init buffer/map
    for i in range(0, 19):
        buf.append('_')

    banner(scr)
    countdown(scr, 3)

    while True:
        cur_scroll_chr = '_'

        scr.clear()
        scr.cursor_off()

        # Draw the current map
        scr.write(cur_avatar_chr + ''.join(buf))

        time.sleep(1)

        # Reset avatar char regardless if it's '-' or 'X'
        cur_avatar_chr = 'o'

        # User Input?
        if msvcrt.kbhit():
            ch = msvcrt.getch()

            if (ch == b'q'):
                scr.clear()
                scr.write("THANKS FOR PLAYING!")
                break

            # User Input && Avatar next to a bomb
            if (buf[0] == '.'):
                if (ch == b' '):
                    print("YES")
                    cur_avatar_chr = '-' 
                    cur_hiscore += 10
        else:

            # No Input && Avatar next to a bomb
            if (buf[0] == '.'):
                print("OUCH!")
                cur_avatar_chr = 'X'
                cur_avatar_life -= 1

                if cur_avatar_life == 0:
                    scr.clear()
                    scr.write("GAME OVER!\nYOUR SCORE: {}".format(cur_hiscore))
                    break

        # Following bomb, we must generate a landing pad
        if gap == True:
            gap = False
        else:
            if (random.random() < 0.5):
                cur_scroll_chr = '.'
                gap = True

        buf.append(cur_scroll_chr)

        cur_hiscore += 1

###############
# Entry Point #
###############

if __name__ == "__main__":
    main()
