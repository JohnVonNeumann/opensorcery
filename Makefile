PACKAGES=docker docker-compose aws

# check_host_system_installs:
# Runs `which` against program targets to ensure that the users development
# environment contains all the necessary packages.
#
# Environmental Variables:
# 	PACKAGES: A space separated list of packages required in the users
# 			  environment.
check_host_system_installs:
	for package in $(PACKAGES); do \
		which $$package ; \
	done

# up:
# Runs `docker-compose up` to serve a local development environment to users.
up:
	docker-compose up

# npm_add_package:
# Runs npm install and saves the output to the `package.lock` file, within the
# `frontend` docker container. Allows you to maintain a clean environment.
#
# Params:
# 	package: The name of an npm package you wish to install and save to the
# 			 package.lock file.
#
# Warning: Args in makefiles must be passsed via the command-line in the form of
# 		   keyword args. So you would provide it via package=lolpackagename.
npm_add_package:
	docker-compose run frontend npm install $(package) --save
