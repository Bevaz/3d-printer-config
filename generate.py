from jinja2 import Template, StrictUndefined
from os import mkdir

saveDir = 'shippable/'

for path in {'', 'Simplify3D', 'Cura', 'Slic3r', 'KISSlicer', 'Marlin' }:
    try:
        mkdir(saveDir + path)
    except OSError:
        pass

Filament = {'ABS', 'PLA'}
Quality = {'HighQuality', 'FastSpeed'}
Model = {'FDMi1', 'FDMi2'}
Apps = {'Simplify3D', 'Cura', 'Slic3r', 'KISSlicer_materials', 'KISSlicer_printers', 'KISSlicer_styles', 'KISSlicer_supports', 'Marlin' }

nozzleSize = 0.4
layerHeight = 0.24
printTempABS = 250
printTempPLA = 210
defaultSpeedHQ = 15
defaultSpeedFS = 30
maxXYSpeed = 80
maxZSpeed = 3.5
printSizeXi1 = 150
printSizeXi2 = 250
printSizeY = 150
printSizeZ = 140
infillPercentage = 30
perimeterOutlines = 3
solidLayers = 4

templ = {}
save = {}
templData = {}
templFile = {}

templ[ 'Simplify3D' ] = 'Simplify3D/zbot_templ.fff'
save[ 'Simplify3D' ] = saveDir + 'Simplify3D/Zbot_{0}_{1}_{2}.fff'

templ[ 'Cura' ] = 'Cura/zbot_templ.ini'
save[ 'Cura' ] = saveDir + 'Cura/Zbot_{0}_{1}_{2}.ini'

templ[ 'Slic3r' ] = 'Slic3r/zbot_templ.ini'
save[ 'Slic3r' ] = saveDir + 'Slic3r/Zbot_{0}_{1}_{2}.ini'

templ[ 'KISSlicer_materials' ] = 'KISSlicer/_materials_templ.ini'
save[ 'KISSlicer_materials' ] = saveDir + 'KISSlicer/_materials_{0}_{2}.ini'
templ[ 'KISSlicer_printers' ] = 'KISSlicer/_printers_templ.ini'
save[ 'KISSlicer_printers' ] = saveDir + 'KISSlicer/_printers_{0}_{2}.ini'
templ[ 'KISSlicer_styles' ] = 'KISSlicer/_styles_templ.ini'
save[ 'KISSlicer_styles' ] = saveDir + 'KISSlicer/_styles_{0}_{2}.ini'
templ[ 'KISSlicer_supports' ] = 'KISSlicer/_supports_templ.ini'
save[ 'KISSlicer_supports' ] = saveDir + 'KISSlicer/_supports_{0}_{2}.ini'

templ[ 'Marlin' ] = 'Marlin/zbot_templ.patch'
save[ 'Marlin' ] = saveDir + 'Marlin/Zbot_{0}.patch'

for app in Apps:
    with open (templ[ app ], "r") as templFile[ app ]:
        templData[ app ]=Template(templFile[ app ].read(), undefined=StrictUndefined)

for filament in Filament:
     for quality in Quality:
          for model in Model:
               args = {}
               args[ 'Simplify3D' ] = {
                    'modelName' : model,
                    'layerHeight' : layerHeight,
                    'nozzleSize' : nozzleSize,
                    'width' : nozzleSize * 1.2,
                    'perimeterOutlines' : perimeterOutlines,
                    'solidLayers' : solidLayers,
                    'defaultSpeed' : int(defaultSpeedHQ * 60) if quality == 'HighQuality' else int(defaultSpeedFS * 60),
                    'maxXYSpeed' : int(maxXYSpeed * 60),
                    'maxZSpeed' : int(maxZSpeed * 60),
                    'printSizeX' : printSizeXi1 if model == 'FDMi1' else printSizeXi2,
                    'printSizeY' : printSizeY,
                    'printSizeZ' : printSizeZ,
                    'firstLayerTemp' :  printTempABS + 5 if filament == 'ABS' else printTempPLA + 5,
                    'otherLayerTemp' : printTempABS if filament == 'ABS' else printTempPLA,
                    'infillPercentage' : infillPercentage,
                                      }

               args[ 'Cura' ] = {
                    'modelName' : model,
                    'layerHeight' : layerHeight,
                    'nozzleSize' : nozzleSize,
                    'wallThickness' : round(perimeterOutlines * nozzleSize, 1 ),
                    'solidLayerThickness' : round(solidLayers * layerHeight, 1),
                    'defaultSpeed' : defaultSpeedHQ if quality == 'HighQuality' else defaultSpeedFS,
                    'maxXYSpeed' : maxXYSpeed,
                    'maxZSpeed' : maxZSpeed,
                    'printSizeX' : printSizeXi1 if model == 'FDMi1' else printSizeXi2,
                    'printSizeY' : printSizeY,
                    'printSizeZ' : printSizeZ,
                    'firstLayerTemp' :  printTempABS + 5 if filament == 'ABS' else printTempPLA + 5,
                    'otherLayerTemp' : printTempABS if filament == 'ABS' else printTempPLA,
                    'infillPercentage' : infillPercentage,
                                }

               args[ 'Slic3r' ] = {
                    'modelName' : model,
                    'layerHeight' : layerHeight,
                    'nozzleSize' : nozzleSize,
                    'perimeterOutlines' : perimeterOutlines,
                    'solidLayers' : solidLayers,
                    'defaultSpeed' : defaultSpeedHQ if quality == 'HighQuality' else defaultSpeedFS,
                    'maxXYSpeed' : maxXYSpeed,
                    'maxZSpeed' : maxZSpeed,
                    'printSizeX' : printSizeXi1 if model == 'FDMi1' else printSizeXi2,
                    'printSizeY' : printSizeY,
                    'printSizeZ' : printSizeZ,
                    'firstLayerTemp' :  printTempABS + 5 if filament == 'ABS' else printTempPLA + 5,
                    'otherLayerTemp' : printTempABS if filament == 'ABS' else printTempPLA,
                    'infillPercentage' : infillPercentage,
                                }

               args[ 'KISSlicer_materials' ] = {
                    'modelName' : model,
                    'layerHeight' : layerHeight,
                    'nozzleSize' : nozzleSize,
                    'width' : nozzleSize * 1.2,
                    'perimeterOutlines' : perimeterOutlines,
                    'solidLayerThickness' : round(solidLayers * layerHeight, 1),
                    'maxXYSpeed' : maxXYSpeed,
                    'maxZSpeed' : maxZSpeed,
                    'printSizeX' : printSizeXi1 if model == 'FDMi1' else printSizeXi2,
                    'printSizeY' : printSizeY,
                    'printSizeZ' : printSizeZ,
                    'printCenterX' : int(printSizeXi1 / 2) if model == 'FDMi1' else int(printSizeXi2 / 2),
                    'printCenterY' : int(printSizeY / 2),
                    'firstLayerTemp' :  printTempABS + 5 if filament == 'ABS' else printTempPLA + 5,
                    'otherLayerTemp' : printTempABS if filament == 'ABS' else printTempPLA,
                    'infillPercentage' : infillPercentage,
                                }
               args[ 'KISSlicer_printers' ] = args[ 'KISSlicer_materials' ]
               args[ 'KISSlicer_styles' ] = args[ 'KISSlicer_materials' ]
               args[ 'KISSlicer_supports' ] = args[ 'KISSlicer_materials' ]

               args[ 'Marlin' ] = {
                    'modelName' : model,
                    'printSizeX' : printSizeXi1 + 5 if model == 'FDMi1' else printSizeXi2 + 5,
                    'printSizeY' : printSizeY,
                    'printSizeZ' : printSizeZ,
                                }


               for app in Apps:
                    with open ( save[ app ].format( model, quality, filament ), "w" ) as saveFile:
                         saveFile.write( templData[ app ].render( args[ app ] ) )
