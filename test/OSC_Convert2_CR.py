from osc_cr_converter.converter.osc2cr import Osc2CrConverter
from osc_cr_converter.utility.configuration import ConverterParams
from osc_cr_converter.utility.visualization import visualize_scenario

# scenario path and name
openscenario = '/home/tianzheng/Documents/ASAMFiles/SimpleCurveScenario1/SimpleCurve.xosc'
# openscenario = '/home/tianzheng/Documents/Github/commonroad-openscenario-converter/scenarios/from_esmini/xosc/pedestrian_collision.xosc'

# build configuration
# config = ConverterParams()
config = ConverterParams.load('/home/tianzheng/Documents/Github/commonroad-openscenario-converter/test/SimpleCurve.yaml')

# convert OpenSCENARIO to CommonRoad
converter = Osc2CrConverter(config)
scenario = converter.run_conversion(openscenario)

# visualize the converted CommonRoad scenario
visualize_scenario(scenario, config)

