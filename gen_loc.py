import os
import os.path

basePath = "./repos"
basePath2 = "/repos"
locations_file = "./conf.d/locations.file"

if not os.path.exists(locations_file):
    fh = open(locations_file, "w")
    fh.close()

try:
    listingFile = open(locations_file, "r")
    listingContents = listingFile.read()
except IOError:
    listingContents = ""


allList = os.listdir(basePath)
for f in allList:
	if os.path.isdir(basePath+"/" + f) and f[0]!='.':
		if f not in listingContents:
			fh = open(locations_file, "a")
			fh.write("\nlocation " + "/"+ f +" {\n")
			fh.write("\talias " + basePath2 +"/"+ f +"/_site;\n")
			fh.write("\tauth_basic \"Restricted Content\";\n")
 			fh.write("\tauth_basic_user_file " + basePath2 + "/" + f + "/.htpasswd;\n")
			fh.write("}\n")
			fh.close()

print "Done"
