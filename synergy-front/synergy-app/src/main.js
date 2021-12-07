import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'


import gql from 'graphql-tag'

Vue.config.productionTip = false

import { ApolloClient } from 'apollo-client'
import { createHttpLink } from 'apollo-link-http'
import { InMemoryCache } from 'apollo-cache-inmemory'
import VueApollo from 'vue-apollo'

// HTTP connection to the API
const httpLink = createHttpLink({
// You should use an absolute URL here
uri: 'http://127.0.0.1:8000/api/',
})

// Cache implementation
const cache = new InMemoryCache()

// Create the apollo client
const apolloClient = new ApolloClient({
link: httpLink,
cache,
})

const apolloProvider = new VueApollo({
defaultClient: apolloClient,
})

new Vue({
  apolloProvider,
  vuetify,
  render: h => h(App)
}).$mount('#app')

Vue.use(VueApollo)

console.log("Я здесь!!!!!!!!!!!!!!!")
console.log(gql`query {occupations {id, name, companyName, positionName}}`)


