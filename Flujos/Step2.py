# -*- coding: UTF-8 -*-
from __main__ import vtk, qt, ctk, slicer

class Step2(ctk.ctkWorkflowWidgetStep, ) :
    """Step implemented using the derivation approach"""
    
    def __init__(self, stepid):
        self.initialize(stepid)
        self.setName( '2. Name of %s' % self.id() )
        self.setDescription( 'This is the description of %s.' % self.id() )
    
    def createUserInterface(self):
        self.__layout = qt.QFormLayout( self )
        self.__layout.addRow("",qt.QWidget())
        self.__layout.addRow("",qt.QWidget())
        self.__layout.addRow("",qt.QWidget())
 
        
        self.nombreLabel = qt.QLabel("         Nombre:")
        self.nombreTextEdit = qt.QLineEdit()
        self.nombreTextEdit.setFixedWidth(200)
        self.nombreTextEdit.textChanged.connect(self.textchanged1)
        self.__layout.addRow(self.nombreLabel,self.nombreTextEdit)
        self.contrasenaLabeL =  qt.QLabel("         Password:")
        self.contrasenaTextEdit = qt.QLineEdit()
        self.contrasenaTextEdit.setFixedWidth(200)
        self.contrasenaTextEdit.setEchoMode(qt.QLineEdit.Password)
        self.contrasenaTextEdit.textChanged.connect(self.textchanged2)
        self.__layout.addRow(self.contrasenaLabeL,self.contrasenaTextEdit)

        qt.QTimer.singleShot(0, self.killButton)
    
    def onEntry(self, comingFrom, transitionType):
        super(Step2, self).onEntry(comingFrom, transitionType)
        print('onEntry - step %s' % self.id())
    
    def onExit(self, goingTo, transitionType):
        super(Step2, self).onExit(goingTo, transitionType)
        print('onExit - step %s' % self.id())
    
    def validate(self, desiredBranchId):
        validationSuceeded = True
        super(Step2, self).validate(validationSuceeded, desiredBranchId)
        print('Validate - step %s' % self.id())

    def killButton(self):
        # hide useless button
        bl = slicer.util.findChildren(text='Step4')
        bl[0].hide()

    def textchanged1(self,text):
        self.name = text

    def textchanged2(self,text):
        self.contra = text


