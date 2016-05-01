# These imports auto-inject nppsftp.py as a valid sublime plugin
# if placed in the /Packages folder.
import sublime, sublime_plugin

'''
Class containing individual run commands for the entire plugin.
'''
class FTPCommand(sublime_plugin.TextCommand):
	
	'''
	Generic run command prepends "Hello, World!" to the
	start of a document.
	'''
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World!")
