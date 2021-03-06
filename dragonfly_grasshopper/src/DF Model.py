# Dragonfly: A Plugin for Environmental Analysis (GPL)
# This file is part of Dragonfly.
#
# Copyright (c) 2020, Ladybug Tools.
# You should have received a copy of the GNU General Public License
# along with Dragonfly; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Create a Dragonfly Model, which can be translated to Honeybee model and sent
for simulation.
-

    Args:
        _buildings: A list of Dragonfly Building objects to be added to the Model.
            Note that at least one Building is necessary to make a simulate-able
            energy model.
        context_: Optional Dragonfly ContextShade objects to be added to the Model.
        _name_: Text to be used for the name and identifier of the Model. If no
            name is provided, it will be "unnamed".

    Returns:
        report: Reports, errors, warnings, etc.
        model: A Dragonfly Model object possessing all of the input geometry
            objects.
"""

ghenv.Component.Name = 'DF Model'
ghenv.Component.NickName = 'Model'
ghenv.Component.Message = '1.1.1'
ghenv.Component.Category = 'Dragonfly'
ghenv.Component.SubCategory = '0 :: Create'
ghenv.Component.AdditionalHelpFromDocStrings = '1'

try:  # import the core honeybee dependencies
    from honeybee.typing import clean_string
except ImportError as e:
    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))

try:  # import the core dragonfly dependencies
    from dragonfly.model import Model
except ImportError as e:
    raise ImportError('\nFailed to import dragonfly:\n\t{}'.format(e))

try:
    from ladybug_rhino.grasshopper import all_required_inputs
    from ladybug_rhino.config import units_system, tolerance, angle_tolerance
except ImportError as e:
    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))


if all_required_inputs(ghenv.Component):
    # set a default name
    name = clean_string(_name_) if _name_ is not None else 'unnamed'
    units = units_system()

    # create the model
    model = Model(name, _buildings, context_, units=units, tolerance=tolerance,
                  angle_tolerance=angle_tolerance)
    if _name_ is not None:
        model.display_name = _name_
