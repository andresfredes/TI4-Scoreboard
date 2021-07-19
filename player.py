# Copyright 2021, Andres Fredes, <andres.hector.fredes@gmail.com>
# 
# This file is part of TI4-Scoreboard.
# 
#     TI4-Scoreboard is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
# 
#     TI4-Scoreboard is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
# 
#     You should have received a copy of the GNU General Public License
#     along with TI4-Scoreboard.  If not, see <https://www.gnu.org/licenses/>.

class Player(object):
    def __init__(self, num):
        super().__init__()
        self.num = num
        self.name = ""
        self.faction = None
        self.colour = ""
        self.score = 0
        self.strat_card = 0
        self.passed = False
        self.card_used = False
        self.is_turn = False
