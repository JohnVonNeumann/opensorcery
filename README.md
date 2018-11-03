# Opensorcery
[![Build Status](https://travis-ci.org/opensorcery-io/opensorcery.svg?branch=master)](https://travis-ci.org/opensorcery-io/opensorcery)

## Development
The project uses Docker/Docker Compose to handle development environments. The setup is fairly simple:
1. `git clone` the repository
2. Ensure that you have docker installed.
3. from the root of the directory, run `docker-compose up`
4. Navigate to `localhost:8000` for Django.
5. Navigate also to `localhost:8080` for Vue.
5. great success

## Backend

### Django
Django uses `settings.py` to configure itself, and as such, it will be home to a variety of secrets and whatnot. Some things will have to be set via `environmental variables` to work effectively. 

## Infrastructure
Seeing as the project is heavily reliant on Infrastructure (possibly moreso than usual, due to the major abstraction of it) I've included all the necessary setup components as well as the obvious code. My knowledge only covers AWS at this point in time.
### Sceptre
We use Sceptre to handle test infrastructure. You can find it located at `/sceptre`. Although this probably won't continue to be a thing for very long, Sceptre is effectively a wrapper around Cloudformation, with the original idea being that people could run their own dev envs on AWS, this, I realised, is stupid, the new Docker configuration will be far better suited towards development environments and will help maintain consistency across platforms.

## Frontend
### Installing dependencies and updating the package.lock file
When installing a new package via NPM into the containers, care should be taken to do things the right way, as simply adding the package to your `package.json` file will result in a few issues, namely that the `package.lock` file will not be updated via the `docker-compose build` command. This gives you two options. These are:
1. `docker-compose run frontend npm install "lolpackage" --save`
OR
2. Add the package to your `package.json` file, then run `docker-compose run frontend npm install" 

Either of these choices will update the `package.lock` file.

## Design

MVP/User mapping design/planning is being done via trello. Feel free to jump on it to have a browse at the overall planning of the application.
[Opensorcery - Trello](https://trello.com/b/HcEsFgUa/opensourcery)
