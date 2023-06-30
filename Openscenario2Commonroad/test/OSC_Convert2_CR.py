from osc_cr_converter.converter.osc2cr import Osc2CrConverter
from osc_cr_converter.utility.configuration import ConverterParams
from osc_cr_converter.utility.visualization import visualize_scenario

# scenario path and name
openscenario = '' # replace by /.../OpenSCENARIO2SUMO/Openscenario2Commonroad/OpenscenarioFiles/SimpleCurve.xosc


# build configuration
# config = ConverterParams()
config = ConverterParams.load('') # replace by /.../OpenSCENARIO2SUMO/Openscenario2Commonroad/test/Store.yaml

# convert OpenSCENARIO to CommonRoad
converter = Osc2CrConverter(config)
scenario = converter.run_conversion(openscenario)

# visualize the converted CommonRoad scenario
visualize_scenario(scenario, config)

