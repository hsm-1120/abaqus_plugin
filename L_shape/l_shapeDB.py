# Do not edit this file or it may not load correctly
# if you try to open it with the RSG Dialog Builder.

# Note: thisDir is defined by the Activator class when
#       this file gets executed

from rsg.rsgGui import *
from abaqusConstants import INTEGER, FLOAT
execDir = os.path.split(thisDir)[1]
dialogBox = RsgDialog(title='L_shape_joint', kernelModule='L_speciman', kernelFunction='l_specimen', includeApplyBtn=False, includeSeparator=True, okBtnText='OK', applyBtnText='Apply', execDir=execDir)
RsgGroupBox(name='GroupBox_1', p='DialogBox', text='parameter', layout='0')
RsgTextField(p='GroupBox_1', fieldType='String', ncols=12, labelText='name: ', keyword='s_name', default='')
RsgTextField(p='GroupBox_1', fieldType='Float', ncols=12, labelText='t1:      ', keyword='thickness_1', default='')
RsgTextField(p='GroupBox_1', fieldType='Float', ncols=12, labelText='t2:      ', keyword='thickness_2', default='')
RsgTextField(p='GroupBox_1', fieldType='Float', ncols=12, labelText='d1:     ', keyword='dim_1', default='')
RsgTextField(p='GroupBox_1', fieldType='Float', ncols=12, labelText='d2:     ', keyword='dim_2', default='')
RsgTextField(p='GroupBox_1', fieldType='Float', ncols=12, labelText='o1:     ', keyword='out_1', default='')
RsgTextField(p='GroupBox_1', fieldType='Float', ncols=12, labelText='o2:     ', keyword='out_2', default='')
RsgTextField(p='GroupBox_1', fieldType='Float', ncols=12, labelText='depth:', keyword='dep', default='')
RsgLabel(p='GroupBox_1', text='depth : extrude length', useBoldFont=True)
RsgGroupBox(name='GroupBox_4', p='DialogBox', text='figure', layout='0')
RsgIcon(p='GroupBox_4', fileName=r'L_shape.png')
dialogBox.show()