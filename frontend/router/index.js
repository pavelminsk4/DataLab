import {createRouter, createWebHistory} from 'vue-router'
import {routes} from '@router/routes'
import OnlineModuleRoutes from '@router/OnlineModuleRoutes'
import SocialMediaRoutes from '@router/SocialMediaRoutes'
import AlertsModuleRoutes from '@router/AlertsModuleRoutes'
import AccountAnalysisRoutes from '@router/AccountAnalysisRoutes'
import TwentyFourSevenRoutes from '@router/TwentyFourSevenRoutes'
import LegalRoutes from '@router/LegalRoutes'
import ComparisonModuleRoutes from '@router/ComparisonModuleRoutes'

const router = createRouter({
  history: createWebHistory(),
  mode: 'history',
  scrollBehavior() {
    return {left: 0, top: 0}
  },
  routes: [
    ...routes,
    ...OnlineModuleRoutes,
    ...SocialMediaRoutes,
    ...AlertsModuleRoutes,
    ...AccountAnalysisRoutes,
    ...TwentyFourSevenRoutes,
    ...LegalRoutes,
    ...ComparisonModuleRoutes,
  ],
})

export default router
