# Dragonfly: A Plugin for Climate Modeling (GPL) started by Chris Mackey <chris@ladybug.tools> 
# This file is part of Dragonfly.
#
# You should have received a copy of the GNU General Public License
# along with Dragonfly; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Use this component to generate a Typology from building solids.
-

    Args:
        _geo: A list of closed breps that represent the geometry of the buildings in the urban area that fall under this typology.
        _program: One of the 16 building programs listed from the "DF Bldg Programs" component.  The following options are available:
            FullServiceRestaurant
            Hospital
            LargeHotel
            LargeOffice
            MediumOffice
            MidRiseApartment
            OutPatient
            PrimarySchool
            QuickServiceRestaurant
            SecondarySchool
            SmallHotel
            SmallOffice
            StandAloneRetail
            StripMall
            SuperMarket
            Warehouse
        _age: An integer that sets the age of the buildings represented by this typology.  This is used to determine what constructions make up the walls, roofs, and windows based on international building codes over the last several decades.  Choose from the following options:
            Pre-1980's
            1980's-Present
            New Construction
        _flr_to_flr_: A number that sets the average distance between floors for the building typology.  This will be used to compute the total floor area of the building, which ultimately determines the influence that the typology has on the urban microclimate.
        _fract_canyon_: A number between 0 and 1 that represents the fraction of the building's waste heat from air conditioning that gets rejected into the urban canyon (as opposed to through rooftop equipment or into a ground source loop).  The default is set to 0.5.
        _run: Set to "True" to run the component and generate a building typology.
    Returns:
        read_me: ...
        typology: A Dragonfly building typology object that can be plugged into the "DF City" component.
        -------------: ...
        footprints: The building geometry as projected onto the world XY plane.  This is used to determine the site coverage ratio and to perform a weighted-average of the building heights.
        floors: A list of breps representing the floors of the typology.
        facades: A list of breps representing the exposed facade area of the building breps.  These will be used to calculate the facade-to-site ratio.
"""

ghenv.Component.Name = "DF Building Typology"
ghenv.Component.NickName = 'BldgTypology'
ghenv.Component.Message = 'VER 0.0.04\nAPR_04_2019'
ghenv.Component.Category = "DragonflyPlus"
ghenv.Component.SubCategory = "00::Create"
ghenv.Component.AdditionalHelpFromDocStrings = "1"


_fract_canyon_ = 0
_age = "NewConstruction"
init_check = False

if init_check == True and _run == True:
    typology, footprints, floors, facades = df_BuildingTypology.from_geometry(_geo, 
        _program, _age, _flr_to_flr_, _fract_canyon_)