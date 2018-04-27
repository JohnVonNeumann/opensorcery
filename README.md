# Opensorcery
[![Build Status](https://travis-ci.org/JohnVonNeumann/opensorcery.svg?branch=master)](https://travis-ci.org/JohnVonNeumann/opensorcery)
## Backend

### Django
Django uses `settings.py` to configure itself, and as such, it will be home to a variety of secrets and whatnot. Some things will have to be set via `environmental variables` to work effectively. 

## Infrastructure
Seeing as the project is heavily reliant on Infrastructure (possibly moreso than usual, due to the major abstraction of it) I've included all the necessary setup components as well as the obvious code. My knowledge only covers AWS at this point in time.
### Sceptre
We use Sceptre to handle test infrastructure. You can find it located at `/sceptre`

## Design

MVP/User mapping design/planning is being done via trello. Feel free to jump on it to have a browse at the overall planning of the application.
[Opensorcery - Trello](https://trello.com/b/HcEsFgUa/opensourcery)
