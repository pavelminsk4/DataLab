import {createRouter, createWebHistory} from 'vue-router'
import store from '@store'
import {action, get} from '@store/constants'

import {routes} from '@router/routes'
import OnlineModuleRoutes from '@router/OnlineModuleRoutes'
import SocialMediaRoutes from '@router/SocialMediaRoutes'
import AlertsModuleRoutes from '@router/AlertsModuleRoutes'
import AccountAnalysisRoutes from '@router/AccountAnalysisRoutes'
import TwentyFourSevenRoutes from '@router/TwentyFourSevenRoutes'
import LegalRoutes from '@router/LegalRoutes'
import WidgetsRoutes from '@router/WidgetsRoutes'
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
    ...WidgetsRoutes,
    ...ComparisonModuleRoutes,
  ],
})

router.beforeEach(async (to, from, next) => {
  const publicPathPages = ['/login']
  const publicNamePages = ['ReportWidgetView', 'Legal', 'Privacy', 'Terms']
  const authRequired =
    !publicPathPages.includes(to.path) && !publicNamePages.includes(to.name)

  let user = store.getters[get.USER_INFO]

  if (authRequired && !user) {
    user = await store.dispatch(action.GET_USER_INFORMATION)

    if (!user.id) window.location.href = '/accounts/login/'
    else next()
  } else next()
})

export default router
