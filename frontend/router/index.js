import {createRouter, createWebHistory} from 'vue-router'
import {routes} from '@router/routes'
import onlineModuleRoutes from '@router/OnlineModuleRoutes'

const router = createRouter({
  history: createWebHistory(),
  mode: 'history',
  scrollBehavior() {
    return {left: 0, top: 0}
  },
  routes: [...routes, ...onlineModuleRoutes],
})

export default router
