#!/bin/bash
# Automation script used as a workaround for testing `docker-compose build`
# within the `travis` pipeline. From the local environment, users have a `.env`
# file present for the `docker-compose` build to ingest and supply the docker
# containers/django application with the required secrets. However, we can't
# log this via git, as this file contains secrets. So we dynamically generate it
# using the `before_script` travis directive, and source the environmental
# variables from the travis admin keychain.

# We ignore SC2154 here because the script merely generates a file, we are
# not using the bash, SC is idenitifying the vars as valid bash, not strings.

{
  # shellcheck disable=SC2154
  echo "api_url=${api_url}"
  # shellcheck disable=SC2154
  echo "client_id=${client_id}"
  # shellcheck disable=SC2154
  echo "frontend_redirect_url=${frontend_redirect_url}"
} >> frontend/.env
