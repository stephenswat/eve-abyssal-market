import { createApp } from 'vue/dist/vue.esm-bundler'
import { createRouter, createWebHashHistory } from 'vue-router'
import * as bootstrap from 'bootstrap'

import App from './App.vue'
import HomePage from './components/pages/HomePage.vue'
import FaqPage from './components/pages/FaqPage.vue'
import AppraisalPage from './components/pages/AppraisalPage.vue'
import ModuleListPage from './components/pages/ModuleListPage.vue'

import './scss/styles.scss'

const Legal = { template: '<div>About</div>' }
const Support = { template: '<div>About</div>' }
const Profile = { template: '<div>Profile</div>' }
const Scopes = { template: '<div>Scopes</div>' }
const Module = { template: '<div>Module</div>' }
const Statistics = { template: '<div>Statistics</div>' }

// auth/login
// auth/logout
// auth/callback
// auth/profile
// module/?
// list/?
// creator/?

// robots?


const routes = [
    { path: '/', component: HomePage },
    { path: '/faq', component: FaqPage },
    { path: '/legal', component: Legal },
    { path: '/support', component: Support },
    { path: '/profile', component: Profile },
    { path: '/scopes', component: Scopes },
    { path: '/appraisal', component: AppraisalPage },
    { path: '/statistics', component: Statistics },
    { path: '/module/:id', component: Module },
    { path: '/list/:id', component: ModuleListPage },
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

const app = createApp(App)

app.use(router)
app.mount('#app')
