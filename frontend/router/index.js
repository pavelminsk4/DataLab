import { createRouter, createWebHistory } from 'vue-router'
import { routes } from '@router/routes'

const router = createRouter({
  history: createWebHistory(),
  mode: 'history',
  scrollBehavior() {
    return { left: 0, top: 0 }
  },
  routes
})

export default router
