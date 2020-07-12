import glob
import cx_Freeze

def getItems(path):
	items=[]
	for item in glob.glob(path):
		if("." in item):#File
			items.append(item)
		else:#Folder
			items=items+(getItems(item+"\\*"))
	return(items)

gameName="BCounter"
executables = [cx_Freeze.Executable(gameName+".py")]
#includeFiles=getItems("*")

cx_Freeze.setup(
	name=gameName,
	options={
		"build_exe": {
			"packages":["pygame"]
		}
	},
	executables=executables
)