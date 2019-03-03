from P4 import P4,P4Exception
from reaper_python import *

proj = RPR_EnumProjects(-1, "", 512) #gets the active project file name
#test commit
# Now search for the render path in the active project file
def getrenderPath(path):
    global renderPath
    with open(path) as f:
for line in f:
    if "RENDER_FILE" in line:
        x = line
renderPath = x.rsplit('\"',3)[1] #splits the line to get the clean path name

# Here we checkout the path in perforce if we have rendered
# files from the project before and saved the render path.
def docheckOut(path):
if path == "":
    print "RenderPath not specified"
 else:
    p4.run("edit", renderPath+"\...")


# Lets run the functions.
getrenderPath(proj[2])
doCheckout(renderPath)
