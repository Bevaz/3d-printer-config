from jinja2 import Template

Filament = {'ABS', 'PLA'}
Quality = {'HighQuality', 'FastSpeed'}
Model = {'FDMi1', 'FDMi2'}

tempSimplify3D = 'Simplify3D/zbot_templ.fff'
saveSimplify3D = 'Simplify3D/Zbot_{0}_{1}_{2}.fff'

with open (tempSimplify3D, "r") as templFileSimplify3D:
    templDataSimplify3D=Template(templFileSimplify3D.read())

for filament in Filament:
     for quality in Quality:
          for model in Model:

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


               Simplify3DArgs = { 'defaultSpeed' : int(defaultSpeedHQ * 60) if quality == 'HighQuality' else int(defaultSpeedFS * 60),
                                  'maxXYSpeed' : int(maxXYSpeed * 60),
                                  'maxZSpeed' : int(maxZSpeed * 60),
                                  'printSizeX' : printSizeXi1 if model == 'FDMi1' else printSizeXi2,
                                  'printSizeY' : printSizeY,
                                  'printSizeZ' : printSizeZ,
                                  'firstLayerTemp' :  printTempABS + 5 if filament == 'ABS' else printTempPLA + 5,
                                  'otherLayerTemp' : printTempABS if filament == 'ABS' else printTempPLA,
                                  'infillPercentage' : infillPercentage,
                                }

               with open ( saveSimplify3D.format( model, quality, filament ), "w" ) as saveFile:
                    saveFile.write( templDataSimplify3D.render(Simplify3DArgs) )
