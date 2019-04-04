# Opensorcery
[![Build Status](https://travis-ci.org/opensorcery-io/opensorcery.svg?branch=master)](https://travis-ci.org/opensorcery-io/opensorcery)

## Development
The project uses Docker/Docker Compose to handle development environments. The setup is fairly simple:
1. `git clone` the repository
2. Ensure that you have docker installed.
3. from the root of the directory, run `make up`
4. Navigate to `localhost:8000` for Django.
5. Navigate also to `localhost:8080` for Vue.
5. great success

## Backend

### Automation
Automation here is a first class citizen, and we have a strong belief that all menial tasks can, should and will be automated. We utilise `Make` for development environment automation, as it allows for a consistent API to deal with, and allows various skilled operators to provide a simple interface for their (perhaps) complicated processes to be handled.

        A prime example of this would be that the average user doesn't need to 
        understand docker to run their local environment, by wrapping the 
        `docker-compose` binary with `Make`, all the user needs to know is 
        `make up` serves them their development environment.

#### Make Commands

Commands can be read by users by reading the [Makefile](https://github.com/opensorcery-io/opensorcery/blob/master/Makefile), otherwise, view the table below for a brief summary.

| command | description |
| ------- | ----------- |
| check_host_system_installs | Runs `which` against `binary` targets to check the host level |
| up | Runs `docker-compose up` to stand up a development environment |
| npm_add_package | Runs `npm install` with a user-provided keyword-arg in the form of `package=example` to install a package and add it to the `package.lock` files. |
| npm_update_packages | Runs `npm update --save` to update your `package.lock` files. |
| pip_update_packages | Runs `pip install --upgrade` with the `requirements.txt` file, and then `pip freeze` back into the `requirements.txt` file to upgrade all `python` dependencies. |

### Django
Django uses `settings.py` to configure itself, and as such, it will be home to a variety of secrets and whatnot. Some things will have to be set via `environmental variables` to work effectively. 

## Infrastructure
Infrastructure for the project is currently up in the air, mainly due to the fact that the project started off as a serverless project, before going back to non-serverless, then the use of containers for development has lead me (JohnVonNeumann) to believe that a transition to a containerised production environment makes the most sense. I don't have any interest in managing non-standard environments that have separate implementations/diverge from one another. However, I'm also not totally sold on the idea of running containers in production, because I am unsure of when they should actually be used and when their usage is a meme.

## Frontend
### Installing dependencies and updating the package.lock file
When installing a new package via NPM into the containers, care should be taken to do things the right way, as simply adding the package to your `package.json` file will result in a few issues, namely that the `package.lock` file will not be updated via the `docker-compose build` command. This gives you multiple options. The preferred method being:
        ```
        make npm_add_package package=examplepackagename
        ```
Alternatively, if you wish to do it manually, you can use:

        1. `docker-compose run frontend npm install "lolpackage" --save`
OR

        2. Add the package to your `package.json` file, then run `docker-compose run frontend npm install`

Either of these choices will update the `package.lock` file.

## Design

MVP/User mapping design/planning is being done via trello. Feel free to jump on it to have a browse at the overall planning of the application.
[Opensorcery - Trello](https://trello.com/b/HcEsFgUa/opensourcery)
