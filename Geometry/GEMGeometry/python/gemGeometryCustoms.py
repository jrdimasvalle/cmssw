import FWCore.ParameterSet.Config as cms

## change the current default GEM geometry

## GE1/1 in 2019 scenario
def custom_GE11_8partitions_v2(process):
    mynum = process.XMLIdealGeometryESSource.geomXMLFiles.index('Geometry/MuonCommonData/data/v4/gemf.xml')
    process.XMLIdealGeometryESSource.geomXMLFiles.remove('Geometry/MuonCommonData/data/v4/gemf.xml')
    process.XMLIdealGeometryESSource.geomXMLFiles.insert(mynum,'Geometry/MuonCommonData/data/v5/gemf.xml')
    
    mynum = process.XMLIdealGeometryESSource.geomXMLFiles.index('Geometry/MuonCommonData/data/v2/muonGemNumbering.xml')
    process.XMLIdealGeometryESSource.geomXMLFiles.remove('Geometry/MuonCommonData/data/v2/muonGemNumbering.xml')
    process.XMLIdealGeometryESSource.geomXMLFiles.insert(mynum,'Geometry/MuonCommonData/data/v5/muonGemNumbering.xml')
    return process
