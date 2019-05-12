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

# npm_update_packages:
# Runs `npm update` and saves the output to the `package{-lock}.json` files.
npm_update_packages:
	docker-compose run frontend npm update --save

# pip_update_packages:
# Runs 'pip install --upgrade" from the `requirements.txt` file, before running
# a `pip freeze` and piping it back into the `requirements.txt` file. This is
# effectively an upgrade.
pip_update_packages:
	docker-compose run backend bash -c "pip install -r requirements.txt --upgrade && pip freeze > requirements.txt"

# django_migrate:
# Runs a 'python manage.py migrate' with `docker-compose` to apply migrations
# present in the project. This is a pain in the arse command because auto
# applying the migrations is generally a bad idea.
django_migrate:
	docker-compose run backend python manage.py migrate

# django_test:
# Runs a 'python manage.py test' with `docker-compose` to run all django based
# tests.
django_test:
	docker-compose run backend python manage.py test

# django_makemigrations:
# Runs a 'python manage.py makemigrations' with `docker-compose` to generate
# new migrations as a result of updates to the applications models.
django_makemigrations:
	docker-compose run backend python manage.py makemigrations

# docker_clean_all:
# Cleans all images, containers and anything related to docker. This shouldn't
# be used if your machine contains anything critical on docker not related to
# the project, it will remove everything. I use it when I'm testing new things
# to do with migrations or the like where I need a *clean* start.
docker_clean_all:
	docker system prune --all
