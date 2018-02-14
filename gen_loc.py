import os.path
import shlex
from subprocess import Popen, PIPE

repos_path = "./repos"
repos_path_in_container = "/repos"
locations_file = "./conf.d/locations.file"


def do_cmd(cmd):
    print cmd
    process = Popen(shlex.split(cmd), stdout=PIPE, stderr=PIPE)
    out, err = process.communicate()


def main():

    with open(locations_file, "w") as loc_file:

        dir_list = os.listdir(repos_path)

        for site in dir_list:

            site_path = repos_path + "/" + site
            is_auth = os.path.isfile(site_path + "/" + ".htpasswd")

            if os.path.isdir(site_path) and site[0] != '.':

                cmd = "jekyll build -s " + site_path + " -d " + site_path + "/_site" + " -b /" + site
                do_cmd(cmd)

                loc_file.write("\nlocation " + "/" + site + " {\n")
                loc_file.write("\talias " + repos_path_in_container + "/" + site + "/_site;\n")

                if is_auth:
                    loc_file.write("\tauth_basic \"Restricted Content\";\n")
                    loc_file.write("\tauth_basic_user_file " + repos_path_in_container + "/" + site + "/.htpasswd;\n")

                loc_file.write("}\n")

    loc_file.close()


if __name__ == '__main__':
    main()
    print "Done"
