from lib.graphics import OpenGL3lib

ProFontWindows = "data/fonts/ProFontWinTweaked/ProFontWindows.ttf"
DigitalItalicFont = "data/fonts/DS-Digital-ItalicST.ttf"
Vera = "data/fonts/ttf-bitstream-vera-1.10/Vera.ttf"
VeraB = "data/fonts/ttf-bitstream-vera-1.10/VeraMoBd.ttf"

FONT_SIZE_VSMALL 	= 11
FONT_SIZE_13PT	 	= 13
FONT_SIZE_14PT		= 14
FONT_SIZE_15PT 		= 15
FONT_SIZE_LARGE 	= 17
FONT_SIZE_VLARGE 	= 20
FONT_SIZE_XLARGE 	= 35
FONT_SIZE_XXLARGE 	= 40

TXT_COLOR_WHITE 	= (255,255,255)
TXT_COLOR_PINK 		= (254,0,254)
TXT_COLOR_GREY 		= (128,128,128)
TXT_COLOR_TURQUOISE = (0,255,255)
TXT_COLOR_GREEN = (0,213,0)
TXT_COLOR_ORANGE = (211,62,33)


PROFONTWINDOWS_VSMALL_WHITE = 		None
PROFONTWINDOWS_VSMALL_TURQUOISE = 	None

PROFONTWINDOWS_SMALL_WHITE = 		None
PROFONTWINDOWS_SMALL_TURQUOISE = 	None
PROFONTWINDOWS_SMALL_GREEN =	 	None

PROFONTWINDOWS_MED_WHITE = 			None
PROFONTWINDOWS_MED_GREY = 			None
PROFONTWINDOWS_MED_TURQUOISE = 		None

PROFONTWINDOWS_LARGE_WHITE = 		None
PROFONTWINDOWS_LARGE_PINK  = 		None
PROFONTWINDOWS_LARGE_GREY  = 		None
PROFONTWINDOWS_LARGE_TURQUOISE  = 	None

PROFONTWINDOWS_VLARGE_WHITE = 		None

DIGITAL_ITAL_MED_ORANGE = 		None
DIGITAL_ITAL_XXLARGE_ORANGE = 	None

VERA_VSMALL_ORANGE = None
VERA_VSMALL_BOLD_ORANGE = None
VERA_13PT_BOLD_ORANGE = None
VERA_15PT_BOLD_ORANGE = None
VERA_14PT_BOLD_ORANGE = None

#def __init__(self,fontName,fontSize, fontColor = (255,255,255), antialias = True, fontKerning = 0):
def initFonts():
	
	fontKerning = 0
	antialias = True
	
	global PROFONTWINDOWS_VSMALL_WHITE 
	global PROFONTWINDOWS_VSMALL_TURQUOISE

	global PROFONTWINDOWS_SMALL_WHITE
	global PROFONTWINDOWS_SMALL_TURQUOISE 
	global PROFONTWINDOWS_SMALL_GREEN

	global PROFONTWINDOWS_MED_WHITE
	global PROFONTWINDOWS_MED_GREY
	global PROFONTWINDOWS_MED_TURQUOISE

	global PROFONTWINDOWS_LARGE_WHITE
	global PROFONTWINDOWS_LARGE_PINK
	global PROFONTWINDOWS_LARGE_GREY
	global PROFONTWINDOWS_LARGE_TURQUOISE

	global PROFONTWINDOWS_VLARGE_WHITE
	
	global DIGITAL_ITAL_MED_ORANGE
	global DIGITAL_ITAL_XXLARGE_ORANGE
	
	global ARIAL_CONDENSED_SMALL_ORANGE
	
	global VERA_VSMALL_ORANGE
	global VERA_VSMALL_BOLD_ORANGE
	global VERA_14PT_BOLD_ORANGE
	global VERA_13PT_BOLD_ORANGE
	global VERA_15PT_BOLD_ORANGE
	

	PROFONTWINDOWS_VSMALL_WHITE = 		OpenGL3lib.GL_Font(ProFontWindows, FONT_SIZE_VSMALL, TXT_COLOR_WHITE, antialias, fontKerning)
	PROFONTWINDOWS_VSMALL_TURQUOISE = 	OpenGL3lib.GL_Font(ProFontWindows, FONT_SIZE_VSMALL, TXT_COLOR_TURQUOISE, antialias, fontKerning)

	PROFONTWINDOWS_SMALL_WHITE = 		OpenGL3lib.GL_Font(ProFontWindows, FONT_SIZE_13PT, TXT_COLOR_WHITE, antialias, fontKerning+1)
	PROFONTWINDOWS_SMALL_TURQUOISE = 	OpenGL3lib.GL_Font(ProFontWindows, FONT_SIZE_13PT, TXT_COLOR_TURQUOISE, antialias, fontKerning+1)
	PROFONTWINDOWS_SMALL_GREEN =	 	OpenGL3lib.GL_Font(ProFontWindows, FONT_SIZE_13PT, TXT_COLOR_GREEN, antialias, fontKerning+1)

	PROFONTWINDOWS_MED_WHITE = 			OpenGL3lib.GL_Font(ProFontWindows, FONT_SIZE_15PT, TXT_COLOR_WHITE, antialias, fontKerning)
	PROFONTWINDOWS_MED_GREY = 			OpenGL3lib.GL_Font(ProFontWindows, FONT_SIZE_15PT, TXT_COLOR_GREY, antialias, fontKerning)
	PROFONTWINDOWS_MED_TURQUOISE = 		OpenGL3lib.GL_Font(ProFontWindows, FONT_SIZE_15PT, TXT_COLOR_TURQUOISE, antialias, fontKerning)

	PROFONTWINDOWS_LARGE_WHITE = 		OpenGL3lib.GL_Font(ProFontWindows, FONT_SIZE_LARGE, TXT_COLOR_WHITE, antialias, fontKerning)
	PROFONTWINDOWS_LARGE_PINK  = 		OpenGL3lib.GL_Font(ProFontWindows, FONT_SIZE_LARGE, TXT_COLOR_PINK, antialias, fontKerning)
	PROFONTWINDOWS_LARGE_GREY  = 		OpenGL3lib.GL_Font(ProFontWindows, FONT_SIZE_LARGE, TXT_COLOR_GREY, antialias, fontKerning)
	PROFONTWINDOWS_LARGE_TURQUOISE  = 	OpenGL3lib.GL_Font(ProFontWindows, FONT_SIZE_LARGE, TXT_COLOR_TURQUOISE, antialias, fontKerning)

	PROFONTWINDOWS_VLARGE_WHITE = 		OpenGL3lib.GL_Font(ProFontWindows, FONT_SIZE_VLARGE, TXT_COLOR_WHITE, antialias, fontKerning)
	
	DIGITAL_ITAL_MED_ORANGE = 			OpenGL3lib.GL_Font(DigitalItalicFont, FONT_SIZE_XLARGE, TXT_COLOR_ORANGE, antialias, -4)
	DIGITAL_ITAL_XXLARGE_ORANGE =		OpenGL3lib.GL_Font(DigitalItalicFont, FONT_SIZE_XXLARGE, TXT_COLOR_ORANGE, antialias, -2)
	
	VERA_VSMALL_ORANGE = 				OpenGL3lib.GL_Font(Vera, FONT_SIZE_VSMALL, TXT_COLOR_ORANGE, antialias, 0)
	VERA_VSMALL_BOLD_ORANGE = 			OpenGL3lib.GL_Font(VeraB, FONT_SIZE_VSMALL, TXT_COLOR_ORANGE, antialias, 0)
	VERA_13PT_BOLD_ORANGE = 			OpenGL3lib.GL_Font(VeraB, FONT_SIZE_13PT, TXT_COLOR_ORANGE, antialias, 0)
	VERA_14PT_BOLD_ORANGE = 			OpenGL3lib.GL_Font(VeraB, FONT_SIZE_14PT, TXT_COLOR_ORANGE, antialias, 0)
	VERA_15PT_BOLD_ORANGE = 			OpenGL3lib.GL_Font(VeraB, FONT_SIZE_15PT, TXT_COLOR_ORANGE, antialias, 0)
	