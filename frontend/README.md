# frontend

> Vue.js SPA frontend that ingests from API interfaced backend

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```
---

## Instructions around initial setup

The `vue.js` SPA setup was originally done using a tutorial from [Auth0](https://auth0.com/blog/building-modern-applications-with-django-and-vuejs/#bootstrapping-front-end)and it utilised what is essentially a deprecated method for creating the project. As a result of moving to the new `@vue/cli` tool, we have to do a few extra things to get the old CLI commands working.

        1. docker-compose run frontend npm install @vue/cli --save-dev
        2. docker-compose run frontend npm install @vue/cli-init --save-dev

This allows us to run the original command:

        docker-compose run frontend vue init webpack frontend

With the final command being slightly different (requires path traversal through `/node_modules` as we didn't `global` install the packages.

---

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
