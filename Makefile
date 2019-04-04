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
