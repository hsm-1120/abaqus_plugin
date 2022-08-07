# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2020 replay file
# Internal Version: 2019_09_14-01.49.31 163176
# Run by huson on Sat Aug  6 11:16:06 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
def l_specimen(s_name, thickness_1, thickness_2, dim_1, dim_2, out_1, out_2, dep):
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.Line(point1=(0, 0), point2=(thickness_1, 0))
    s.HorizontalConstraint(entity=g[2], addUndoState=False)
    s.Line(point1=(thickness_1, 0), point2=(thickness_1, -(dim_1 - thickness_2)))
    s.VerticalConstraint(entity=g[3], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
    s.Line(point1=(thickness_1, -(dim_1 - thickness_2)), point2=(dim_2, -(dim_1 - thickness_2)))
    s.HorizontalConstraint(entity=g[4], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
    s.Line(point1=(dim_2, -(dim_1 - thickness_2)), point2=(dim_2, -dim_1))
    s.VerticalConstraint(entity=g[5], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
    s.Line(point1=(dim_2, -dim_1), point2=(0, -dim_1))
    s.HorizontalConstraint(entity=g[6], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
    s.Line(point1=(0, -dim_1), point2=(0, 0))
    s.VerticalConstraint(entity=g[7], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
    p = mdb.models['Model-1'].Part(name=s_name + '-joint', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts[s_name + '-joint']
    p.BaseSolidExtrude(sketch=s, depth=dep)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts[s_name + '-joint']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
    s1.setPrimaryObject(option=STANDALONE)
    s1.rectangle(point1=(0, 0), point2=(dim_2 - thickness_1, dim_1 - thickness_2))
    p = mdb.models['Model-1'].Part(name=s_name + '-pull', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts[s_name + '-pull']
    p.BaseSolidExtrude(sketch=s1, depth=dep)
    s1.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts[s_name + '-pull']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
    s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.Line(point1=(0, 0), point2=(out_1, 0))
    s.HorizontalConstraint(entity=g[2], addUndoState=False)
    s.Line(point1=(out_1, 0), point2=((out_1, -dim_1)))
    s.VerticalConstraint(entity=g[3], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
    s.Line(point1=(out_1, -dim_1), point2=(dim_2 + out_1, -dim_1))
    s.HorizontalConstraint(entity=g[4], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[3], entity2=g[4], addUndoState=False)
    s.Line(point1=(dim_2 + out_1, -dim_1), point2=(dim_2 + out_1, -(dim_1 + out_2)))
    s.VerticalConstraint(entity=g[5], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
    s.Line(point1=(dim_2 + out_1, -(dim_1 + out_2)), point2=(0, -(dim_1 + out_2)))
    s.HorizontalConstraint(entity=g[6], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[5], entity2=g[6], addUndoState=False)
    s.Line(point1=(0, -(dim_1 + out_2)), point2=(0, 0))
    s.VerticalConstraint(entity=g[7], addUndoState=False)
    s.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
    p = mdb.models['Model-1'].Part(name=s_name + '-base', dimensionality=THREE_D, 
        type=DEFORMABLE_BODY)
    p = mdb.models['Model-1'].parts[s_name + '-base']
    p.BaseSolidExtrude(sketch=s, depth=dep)
    s.unsetPrimaryObject()
    p = mdb.models['Model-1'].parts[s_name + '-base']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model-1'].sketches['__profile__']
