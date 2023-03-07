import {createRouter, createWebHistory} from 'vue-router'
import {routes} from '@router/routes'
import OnlineModuleRoutes from '@router/OnlineModuleRoutes'
import SocialMediaRoutes from '@router/SocialMediaRoutes'

const router = createRouter({
  history: createWebHistory(),
  mode: 'history',
  scrollBehavior() {
    return {left: 0, top: 0}
  },
  routes: [...routes, ...OnlineModuleRoutes, ...SocialMediaRoutes],
})

export default router
