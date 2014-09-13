# -*- coding: utf-8 -*-
#
# Copyright (C) 2014 Thomas Amland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import os
from functools import partial
from polling import *


def _walker_recursive(top):
    for root, dirs, files in os.walk(top):
        if dirs or files:
            for d in dirs:
                if hidden(d):
                    dirs.remove(d)
            dirs = (os.path.join(root, _)  for _ in dirs)
            files = (os.path.join(root, _) for _ in files if not hidden(_))
            yield dirs, files


class LocalPoller(PollerBase):
    interval = 4
    make_snapshot = partial(FileSnapshot, walker=_walker_recursive)

