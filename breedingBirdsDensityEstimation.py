from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFeatureSink)
from qgis import processing
import pandas as pd

def getSppPoints():
    return sppPoints
def countPtsInPolys(sppPoints):
    """
    Counts spp points within grid squares
    """
    countLayer = processing.run(
        "native.Count Points in Polygon",
        {
        'CLASSFIELD' : '',
        'FIELD' : 'NUMPOINTS',
        'OUTPUT' : 'TEMPORARY_OUTPUT',
        'POINTS' : 'sppPoints',
        'POLYGONS' : 'memory://memory?geometry=Polygon&crs=EPSG:27700&field=id:int8(0,0)&field=left:double(0,0)&field=top:double(0,0)&field=right:double(0,0)&field=bottom:double(0,0)&uid={64e1c832-26eb-46e9-ac8d-35149f5b447a}',
        'WEIGHT' : ''
        }
    )
        
def randomSelection():
    """
    Randomly selects qrid squares
    
    Returns index of selected grid squares
    """
    rSelectedFeatures = processing.run(
        "native.Random Selection"
        {
        'INPUT' : 'Polygon?crs=EPSG:27700&field=id:long(0,0)&field=left:double(0,0)&field=top:double(0,0)&field=right:double(0,0)&field=bottom:double(0,0)&field=NUMPOINTS:double(0,0)&uid={2d375fb3-a64f-439f-952a-319fde49a1d4}',
        'METHOD' : 1,
        'NUMBER' : 25
        }
    )
    
def densityEstimate():
    """
    Returns density estimate per 1km squared
    """
    
    # number of birds counted in randomly selected grid squares
    sumRS = sum
    # random selection count (number of randomly selected grid squares counted)
    countRS = count
    # total count (total number of grid squares)
    countT = count
    
    return ((sumRS/countRS)*countT)*1000

def densityEstimateWrapper(gridTypes,layerNms,verbose = TRUE):
    """
    Wrapper function for density estimate
    
    Returns: dataframe populated with density estimates and exports as csv
    """
    
    df = pd.dataframe
    for gridName in gridTypes:
        
        for sppLyr in layerNms:
            
            idx = vectorLayer.fields().indexOf('BTO Code')
            sppNames = vectorLayer.uniqueValues(idx)
            
            for spp in sppNames:
                sppPoints = getSppPoints()
                countPtsInPolys(sppPoints)
                randomSelection
                
                df[0,sppLyr] = gridName
                df[1,sppLyr] = layerNms
                df[2,sppLyr] = sppName
                df[3,sppLyr] = densityEstimate()
                
                if verbose == TRUE:
                    print("")
                    print(
                    "gridName = ",gridName,
                    ", sppName = ",sppName,
                    ", densityEstimate = ",densityEstimate
                    )
                    print(df[,sppLyr])
                    print("")
            
        df.to_csv(path/gridName,".csv")

layerNms = [
    "BTO codes - Red List Species",
    "BTO codes - Amber List Species",
    "BTO codes - Green List Species"
    ]
gridTypes = ['1 km Buffer Grid','Site Boundary Grid']
# Need to extract data for each species - turn into layer?
densityEstimateWrapper(gridTypes,layerNms,verbose = TRUE)