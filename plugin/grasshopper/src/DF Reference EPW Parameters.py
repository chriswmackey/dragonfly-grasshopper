# Dragonfly: A Plugin for Climate Modeling (GPL) started by Chris Mackey <chris@ladybug.tools> 
# This file is part of Dragonfly.
#
# You should have received a copy of the GNU General Public License
# along with Dragonfly; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>


"""
Use this component to generate refernce EPW site parameters that can be plugged into the "DF Run Urban Weather Generator" component.  If you are using standard files from the US Department of Energy, you should never need to use this component.  This component is onyl for when your data was recorded using non-standard means, such as an experiment that you have run in an actual urban canyon.
-

    Args:
        obstacle_height_: A number that represents the height in meters of objects that obstruct the view to the sky at the weather station site, such as trees and buildings.  The default is set to 0.1.
        _veg_coverage_: A number between 0 and 1 that represents that fraction of the reference EPW site that is covered in grass. If nothing is input here, a defailt of 0.9 will be used.
        _temp_height_: A number that represents the height in meters at which temperature is measured on the weather station.  The default is set to 10 meters as this is the standard measurement height for US Department of Energy EPW files.
        _wind_height_: A number that represents the height in meters at which wind speed is measured on the weather station.  The default is set to 10 meters as this is the standard measurement height for US Department of Energy EPW files.
    Returns:
        epw_site_par: Refernce EPW site parameters that can be plugged into the "DF Run Urban Weather Generator" component.
"""

ghenv.Component.Name = "DF Reference EPW Parameters"
ghenv.Component.NickName = 'RefEPWPar'
ghenv.Component.Message = 'VER 0.0.04\nAPR_08_2019'
ghenv.Component.Category = "DragonflyPlus"
ghenv.Component.SubCategory = "02::Urban Weather"
ghenv.Component.AdditionalHelpFromDocStrings = "4"


#Dragonfly check.
init_check = False

if init_check == True:
    epw_site_par = df_RefEpwPar(obstacle_height_, _veg_coverage_, _temp_height_, 
        _wind_height_)
