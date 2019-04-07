#!/bin/bash
touch .env
echo "auth0_domain=${auth0_domain}" >> .env
echo "api_identifier=${api_identifier}" >> .env
