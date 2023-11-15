import store from '@store'

import AccountAnalysisModuleView from '@views/account-analysis/AccountAnalysisModuleView'
import AccountAnalysisWorkspacesView from '@views/account-analysis/AccountAnalysisWorkspacesView'
import CreateAccountAnalysisView from '@views/account-analysis/CreateAccountAnalysisView'
import AccountAnalysisWorkspaceView from '@views/account-analysis/AccountAnalysisWorkspaceView'

import CreateAccountAnalysisProject from '@components/account-analysis/CreateAccountAnalysisProject'
import CreateAccountAnalysisWorkspace from '@components/account-analysis/CreateAccountAnalysisWorkspace'
import CreateAccountAnalysisRightSide from '@components/account-analysis/CreateAccountAnalysisRightSide'

import AccountAnalysisView from '@views/account-analysis/AccountAnalysisView'
import AccountAnalysisDashboardScreen from '@components/account-analysis/screens/AccountAnalysisDashboardScreen'
import AccountAnalysisOptimizationScreen from '@components/account-analysis/screens/AccountAnalysisOptimizationScreen'
import AccountAnalysisPostsScreen from '@components/account-analysis/screens/AccountAnalysisPostsScreen'
import AccountAnalysisFollowersScreen from '@components/account-analysis/screens/AccountAnalysisFollowersScreen'

export default [
  {
    name: 'AccountAnalysis',
    path: '/account-analysis-module',
    component: AccountAnalysisModuleView,
    redirect: () => ({name: 'AccountAnalysisWorkspaces'}),
    children: [
      {
        name: 'AccountAnalysisWorkspaces',
        path: '',
        component: AccountAnalysisWorkspacesView,
      },

      {
        name: 'AccountAnalysisWorkspace',
        path: 'workspace/:workspaceId',
        component: AccountAnalysisWorkspaceView,
      },
    ],
  },

  {
    name: 'AccountAnalysisCreateWorkspace',
    path: '/account-analysis-module/workspace/:workspaceId/create',
    component: CreateAccountAnalysisView,
    redirect: () => ({name: 'AccountAnalysisWorkspaceStep1'}),
    children: [
      {
        name: 'AccountAnalysisWorkspaceStep1',
        path: 'step1',
        components: {
          default: CreateAccountAnalysisWorkspace,
          secondColumn: CreateAccountAnalysisRightSide,
        },
        props: {
          default: {moduleName: 'AccountAnalysis'},
          secondColumn: {step: 'step1'},
        },
        params: {step: 'step1'},
      },
      {
        name: 'AccountAnalysisWorkspaceStep2',
        path: 'step2',
        components: {
          default: CreateAccountAnalysisProject,
          secondColumn: CreateAccountAnalysisRightSide,
        },
        props: {
          secondColumn: {step: 'step2'},
        },
        params: {step: 'step2'},
        beforeEnter: (to, from, next) => {
          const currentStep = `AccountAnalysisWorkspaceStep${store.state.newAccountAnalysisWorkspace.step}`
          const workspaceId = to.params.workspaceId

          if (to.name !== currentStep && workspaceId === 'new') {
            return next({
              name: 'AccountAnalysisWorkspaceStep1',
              params: {workspaceId},
            })
          }
          return next()
        },
      },
    ],
  },

  {
    name: 'AccountAnalysisFeatures',
    path: '/account-analysis-module/workspace/:workspaceId/project/:projectId/features',
    component: AccountAnalysisView,
    redirect: () => ({name: 'AccountAnalysisDashboard'}),
    children: [
      {
        name: 'AccountAnalysisDashboard',
        path: 'dashboard',
        component: AccountAnalysisDashboardScreen,
      },
      {
        name: 'AccountAnalysisOptimization',
        path: 'optimization',
        component: AccountAnalysisOptimizationScreen,
      },
      {
        name: 'AccountAnalysisPosts',
        path: 'posts',
        component: AccountAnalysisPostsScreen,
      },
      {
        name: 'AccountAnalysisFollowers',
        path: 'followers',
        component: AccountAnalysisFollowersScreen,
      },
    ],
  },
]
