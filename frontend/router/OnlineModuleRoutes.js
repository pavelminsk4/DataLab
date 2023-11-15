import store from '@store'
import OnlineModuleView from '@views/OnlineModuleView'
import OnlineWorkspacesView from '@views/OnlineWorkspacesView'
import OnlineWorkspaceView from '@views/OnlineWorkspaceView'

import OnlineProjectDashboardView from '@views/OnlineProjectDashboardView'

import CreateWorkspaceView from '@components/workspace/CreateWorkspaceView'
import OnlineCreateSearchScreen from '@components/workspace/screens/OnlineCreateSearchScreen'
import CreateProjectScreen from '@components/workspace/screens/CreateProjectScreen'
import CreateWorkspaceScreen from '@components/workspace/screens/CreateWorkspaceScreen'
import CreateWorkspaceRightSide from '@components/workspace/CreateWorkspaceRightSide'
import SearchResults from '@components/SearchResults'

import OnlineSearch from '@components/project/search/OnlineSearch'
import OnlineProjectDashboard from '@components/project/dashboard/OnlineProjectDashboard'
import OnlineFeaturesView from '@views/online/OnlineFeaturesView'
import OnlineSummaryScreen from '@components/project/screens/online/OnlineSummaryScreen'
import OnlineSentimentScreen from '@components/project/screens/online/OnlineSentimentScreen'
import OnlineDemographyScreen from '@components/project/screens/online/OnlineDemographyScreen'
import OnlineInfluencersScreen from '@components/project/screens/online/OnlineInfluencersScreen'

export default [
  {
    path: '/online-module',
    component: OnlineModuleView,
    redirect: () => ({name: 'OnlineHome'}),
    children: [
      {
        name: 'OnlineHome',
        path: '',
        component: OnlineWorkspacesView,
      },

      {
        name: 'OnlineWorkspace',
        path: 'workspace/:workspaceId',
        component: OnlineWorkspaceView,
      },

      {
        name: 'OnlineCreateWorkspace',
        path: 'workspace/:workspaceId/create',
        component: CreateWorkspaceView,
        redirect: () => ({name: 'OnlineWorkspaceStep1'}),
        children: [
          {
            name: 'OnlineWorkspaceStep1',
            path: 'step1',
            components: {
              default: CreateWorkspaceScreen,
              secondColumn: CreateWorkspaceRightSide,
            },
            props: {
              default: {moduleName: 'Online'},
              secondColumn: {step: 'step1'},
            },
          },
          {
            name: 'OnlineWorkspaceStep2',
            path: 'step2',
            components: {
              default: CreateProjectScreen,
              secondColumn: CreateWorkspaceRightSide,
            },
            beforeEnter: (to, from, next) => {
              const workspaceId = to.params.workspaceId

              if (
                to.name !== store.state.currentStep &&
                workspaceId === 'new'
              ) {
                return next({
                  name: 'OnlineWorkspaceStep1',
                  params: {workspaceId},
                })
              }
              return next()
            },
            props: {
              default: (route) => ({
                workspaceId: route.params.workspaceId,
                moduleName: 'Online',
              }),
              secondColumn: {step: 'step2'},
            },
          },
          {
            name: 'OnlineWorkspaceStep3',
            path: 'step3',
            components: {
              default: OnlineCreateSearchScreen,
              secondColumn: SearchResults,
            },
            beforeEnter: (to, from, next) => {
              if (to.name !== store.state.currentStep) {
                const workspaceId = to.params.workspaceId
                if (workspaceId === 'new') {
                  return next({
                    name: 'OnlineWorkspaceStep1',
                    params: {workspaceId},
                  })
                } else {
                  return next({
                    name: 'OnlineWorkspaceStep2',
                    params: {workspaceId},
                  })
                }
              }

              return next()
            },
            props: {
              default: (route) => ({
                workspaceId: route.params.workspaceId,
                moduleName: 'Online',
              }),
              secondColumn: {step: 'step3', moduleName: 'Online'},
            },
          },
        ],
      },

      {
        name: 'ProjectReports',
        path: 'workspace/:workspaceId/project/:projectId/',
        component: OnlineProjectDashboardView,
        children: [
          {
            name: 'OnlineAnalytics',
            path: 'dashboard',
            component: OnlineProjectDashboard,
          },
          {
            name: 'OnlineSearch',
            path: 'search-settings',
            component: OnlineSearch,
          },
          {
            name: 'OnlineFeature',
            path: 'feature',
            component: OnlineFeaturesView,
            children: [
              {
                name: 'OnlineSummary',
                path: 'summary',
                component: OnlineSummaryScreen,
              },
              {
                name: 'OnlineSentiment',
                path: 'sentiment',
                component: OnlineSentimentScreen,
              },
              {
                name: 'OnlineDemography',
                path: 'demography',
                component: OnlineDemographyScreen,
              },
              {
                name: 'OnlineInfluencers',
                path: 'influencers',
                component: OnlineInfluencersScreen,
              },
            ],
          },
        ],
      },
    ],
  },
]
