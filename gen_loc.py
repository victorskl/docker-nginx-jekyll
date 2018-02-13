import os
basePath = "./repos"
basePath2 = "/repos"

try:
    listingFile = open("./conf.d/locations.file", "r")
    listingContents = listingFile.read()
except IOError:
    listingContents = ""


allList = os.listdir(basePath)
for f in allList:
	if os.path.isdir(basePath+"/" + f):
		if f not in listingContents:
			fh = open("./conf.d/locations.file", "a")
			fh.write("\nlocation " + "/"+ f +" {\n")
			fh.write("\talias " + basePath2 +"/"+ f +"/_site;\n")
			fh.write("\tauth_basic \"Restricted Content\";\n")
 			fh.write("\tauth_basic_user_file " + basePath2 + "/" + f + "/.htpasswd;\n")
			fh.write("}\n")
			fh.close()
