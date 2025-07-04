# Dragonfly: A Plugin for Environmental Analysis (GPL)
# This file is part of Dragonfly.
#
# Copyright (c) 2025, Ladybug Tools.
# You should have received a copy of the GNU Affero General Public License
# along with Dragonfly; If not, see <http://www.gnu.org/licenses/>.
# 
# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>

"""
Create Dragonfly window parameters with instructions for repeating rectangular
windows of a fixed width and height.
_
This effectively fills a wall with windows at the specified width, height
and separation.
-

    Args:
        _win_height_: A number for the target height of the windows. Note that, if the
            window_height is larger than the height of the wall, the generated
            windows will have a height equal to the wall height in order
            to avoid having windows extend outside the wall face. (Default:
            2 meters).
        _win_width_: A number for the target width of the windows. Note that, if the
            window_width is larger than the width of the wall, the generated
            windows will have a width equal to the wall width in order to avoid
            having windows extend outside the wall face. (Default: 1.5 meters).
        _sill_height_: A number for the target height above the bottom edge of the face
            to start the apertures. Note that, if the window height is too large
            to acoomodate the sill height input here, the window height will
            take precedence and the sill height will be smaller than this
            value. (Default: 0.8 meters).
        _horiz_separ_: A number for the horizontal separation between individual aperture
            centerlines.  If this number is larger than the parent face's length,
            only one aperture will be produced. (Default: 3 meters).

    Returns:
        win_par: Window Parameters that can be applied to a Dragonfly object
            using the "DF Apply Facade Parameters" component.
"""

ghenv.Component.Name = "DF Repeating Window Width Height Parameters"
ghenv.Component.NickName = 'RepeatingWHPar'
ghenv.Component.Message = '1.9.0'
ghenv.Component.Category = "Dragonfly"
ghenv.Component.SubCategory = '0 :: Create'
ghenv.Component.AdditionalHelpFromDocStrings = "5"

try:  # import the core dragonfly dependencies
    from dragonfly.windowparameter import RepeatingWindowWidthHeight
except ImportError as e:
    raise ImportError('\nFailed to import dragonfly:\n\t{}'.format(e))

try:
    from ladybug_rhino.config import conversion_to_meters
    from ladybug_rhino.grasshopper import turn_off_old_tag
except ImportError as e:
    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))
turn_off_old_tag(ghenv.Component)


# set defaults for any blank inputs
conversion = conversion_to_meters()
_win_height_ = _win_height_ if _win_height_ is not None else 2.0 / conversion
_win_width_ = _win_width_ if _win_width_ is not None else 1.5 / conversion
_sill_height_ = _sill_height_ if _sill_height_ is not None else 0.8 / conversion
_horiz_separ_ = _horiz_separ_ if _horiz_separ_ is not None else 3.0 / conversion

# create the window parameters
if _win_height_ != 0 and _win_width_ != 0:
    win_par = RepeatingWindowWidthHeight(
        _win_height_, _win_width_, _sill_height_, _horiz_separ_)