class Grep:
	def __init__(self, helpdisplay):
		self.helpdisplay = helpdisplay

	def run(self, *args):
		self.helpdisplay.display_help()
