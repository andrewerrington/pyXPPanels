import logging
import decimal
D = decimal.Decimal

from lib.graphics import OpenGL3lib
from lib.graphics import graphicsGL3 as graphics
from lib.graphics import fonts

from lib.network import XPlaneUDPServer
from lib.general import conversionFunctions


class BK_ADF_KR87(graphics.Container):
	XPlaneDataDispatcher = None
	
	def __init__(self,position, size, XPlaneDataDispatcher, batchImageRenderer, texture, name = "BK_ADF_KR87"):
		graphics.Container.__init__(self,position, size, name)
		
		self.testMode = False
		self.XPlaneDataDispatcher = XPlaneDataDispatcher
		self.XPlaneDataDispatcher.requestXPDref(313, "sim/cockpit/radios/adf1_stdby_freq_hz[0]")
		self.XPlaneDataDispatcher.requestXPDref(314, "sim/cockpit2/radios/actuators/adf1_power[0]")
		
		self.layer = 1
		
		TXT_FMT_3DIG_PREC2 = '{:06.2f}'
		TXT_FMT_3DIG_PREC3 = '{:07.3f}'
		
		x_DME_txt 		= 10
		x_ADF_actFrequ 	= 125
		x_ADF_sbyFrequ 	= 280
		x_DME_time 		= 302
		y_frequencies 	= -18
		#-------------------------------------------------------------------------------------------------
		# Background 
		#-------------------------------------------------------------------------------------------------
		self.ADF_BGD = graphics.ImagePanel(texture, batchImageRenderer, self.layer,(0,0),[399,68],[0,2048-186], "ADF_BGD")
		self.ADF_BGD.resize((399,68))
		self.addItem(self.ADF_BGD, (199.5,0), False)
		
		# ADF Active Frequency text
		self.ADF_ACT_FREQU_Text = graphics.TextField(fonts.DIGITAL_ITAL_MED_ORANGE)
		self.ADF_ACT_FREQU_Text.setTextFormat('{:03.0f}')
		self.ADF_ACT_FREQU_Text.setTextDataSource(self.XPlaneDataDispatcher,(101,0))
		self.addItem(self.ADF_ACT_FREQU_Text, (x_ADF_actFrequ,y_frequencies), False)
		
		# ADF standby Frequency text
		self.ADF_SBY_FREQU_Text = graphics.TextField(fonts.DIGITAL_ITAL_MED_ORANGE)
		self.ADF_SBY_FREQU_Text.setTextFormat('{:03.0f}')
		self.ADF_SBY_FREQU_Text.setTextDataSource(self.XPlaneDataDispatcher,(313,0))
		self.addItem(self.ADF_SBY_FREQU_Text, (x_ADF_sbyFrequ,y_frequencies), False)
		
		# ADF ANT indicator
		self.ADF_ANT_Indicator = graphics.TextField(fonts.VERA_VSMALL_BOLD_ORANGE)
		self.ADF_ANT_Indicator.setText('ANT')
		self.addItem(self.ADF_ANT_Indicator, (x_ADF_actFrequ-75,y_frequencies+17), False)
		
		# ADF ADF indicator
		self.ADF_ADF_Indicator = graphics.TextField(fonts.VERA_VSMALL_BOLD_ORANGE)
		self.ADF_ADF_Indicator.setText('ADF')
		self.addItem(self.ADF_ADF_Indicator, (x_ADF_actFrequ-75,y_frequencies+5), False)
		
		# ADF BFO indicator
		self.ADF_BFO_Indicator = graphics.TextField(fonts.VERA_VSMALL_BOLD_ORANGE)
		self.ADF_BFO_Indicator.setText('BFO')
		self.addItem(self.ADF_BFO_Indicator, (x_ADF_actFrequ+75,y_frequencies+17), False)

		
	def draw(self):
		powered = self.XPlaneDataDispatcher.getData(314,0)  # 0 = off, 1 = antenna, 2 = on, 3 = tone, 4 = test
		if powered >= 1.0 :
			self.ADF_BGD.setVisible(True)
			self.ADF_ACT_FREQU_Text.setVisible(True)
			self.ADF_SBY_FREQU_Text.setVisible(True)
			if powered == 1.0 :
				self.ADF_ANT_Indicator.setVisible(True)
				self.ADF_ADF_Indicator.setVisible(False)
				self.ADF_BFO_Indicator.setVisible(False)
			elif powered == 3.0 :
				self.ADF_ANT_Indicator.setVisible(False)
				self.ADF_ADF_Indicator.setVisible(True)
				self.ADF_BFO_Indicator.setVisible(True)
			else:
				self.ADF_ANT_Indicator.setVisible(False)
				self.ADF_ADF_Indicator.setVisible(True)
				self.ADF_BFO_Indicator.setVisible(False)
			
		else:
			self.ADF_BGD.setVisible(False)
			self.ADF_ACT_FREQU_Text.setVisible(False)
			self.ADF_SBY_FREQU_Text.setVisible(False)
			self.ADF_ANT_Indicator.setVisible(False)
			self.ADF_ADF_Indicator.setVisible(False)
			self.ADF_BFO_Indicator.setVisible(False)
		
		super(BK_ADF_KR87,self).draw()

