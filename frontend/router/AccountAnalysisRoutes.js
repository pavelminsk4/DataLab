import store from '@store'

import AccountAnalysisModuleView from '@/views/AccountAnalysisModuleView'
import AccountAnalysisWorkspacesView from '@/views/AccountAnalysisWorkspacesView'
import CreateAccountAnalysisView from '@/views/CreateAccountAnalysisView'

import CreateAccountAnalysisProject from '@/components/account-analysis/CreateAccountAnalysisProject'
import CreateAccountAnalysisWorkspace from '@/components/account-analysis/CreateAccountAnalysisWorkspace'
import CreateAccountAnalysisRightSide from '@/components/account-analysis/CreateAccountAnalysisRightSide'
import AccountAnalysisWorkspaceView from '@/components/account-analysis/AccountAnalysisWorkspaceView'

import AccountAnalysisView from '@/views/account-analysis/AccountAnalysisView'
import AccountAnalysisDashboardScreen from '@/components/account-analysis/screens/AccountAnalysisDashboardScreen'

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
    path: '/account-analysis-module/features',
    component: AccountAnalysisView,
    redirect: () => ({name: 'AccountAnalysisDashBoard'}),
    children: [
      {
        name: 'AccountAnalysisDashboard',
        path: 'dashboard',
        component: AccountAnalysisDashboardScreen,

        beforeEnter: (to, from, next) => {
          if (!store.state.accountAnalysis.currentProjectId)
            return next({name: 'AccountAnalysis'})
          return next()
        },
      },
    ],
  },
]
