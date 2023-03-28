import store from '@store'

import CreateWorkspaceView from '@/components/workspace/CreateWorkspaceView'
import SocialModuleView from '@/views/SocialModuleView'
import SocialWorkspacesView from '@/views/SocialWorkspacesView'
import SocialWorkspaceView from '@/views/SocialWorkspaceView'
import SocialProjectDashboardView from '@/views/SocialProjectDashboardView'
import SocialProjectDashboard from '@/components/project/dashboard/SocialProjectDashboard'
import SocialSearch from '@/components/project/search/SocialSearch'

import SocialCreateSearchScreen from '@/components/workspace/screens/SocialCreateSearchScreen'
import CreateProjectScreen from '@/components/workspace/screens/CreateProjectScreen'
import CreateWorkspaceScreen from '@/components/workspace/screens/CreateWorkspaceScreen'
import CreateWorkspaceRightSide from '@/components/workspace/CreateWorkspaceRightSide'
import SearchResults from '@/components/SearchResults'

import SocialFeaturesView from '@/views/social/SocialFeaturesView'
import SocialSummaryScreen from '@/components/project/screens/social/SocialSummaryScreen'
import SocialSentimentScreen from '@/components/project/screens/social/SocialSentimentScreen'

export default [
  {
    path: '/social-media-module',
    component: SocialModuleView,
    redirect: () => ({name: 'SocialHome'}),
    children: [
      {
        name: 'SocialHome',
        path: '',
        component: SocialWorkspacesView,
      },

      {
        name: 'SocialWorkspace',
        path: 'workspace/:workspaceId',
        component: SocialWorkspaceView,
      },

      {
        name: 'SocialCreateWorkspace',
        path: 'workspace/:workspaceId/create',
        component: CreateWorkspaceView,
        redirect: () => ({name: 'SocialWorkspaceStep1'}),
        children: [
          {
            name: 'SocialWorkspaceStep1',
            path: 'step1',
            components: {
              default: CreateWorkspaceScreen,
              secondColumn: CreateWorkspaceRightSide,
            },
            props: {
              default: {moduleName: 'Social'},
              secondColumn: {step: 'step1'},
            },
          },
          {
            name: 'SocialWorkspaceStep2',
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
                  name: 'SocialWorkspaceStep1',
                  params: {workspaceId},
                })
              }
              return next()
            },
            props: {
              default: (route) => ({
                workspaceId: route.params.workspaceId,
                moduleName: 'Social',
              }),
              secondColumn: {step: 'step2'},
            },
          },
          {
            name: 'SocialWorkspaceStep3',
            path: 'step3',
            components: {
              default: SocialCreateSearchScreen,
              secondColumn: SearchResults,
            },
            beforeEnter: (to, from, next) => {
              if (to.name !== store.state.currentStep) {
                const workspaceId = to.params.workspaceId
                if (workspaceId === 'new') {
                  return next({
                    name: 'SocialWorkspaceStep1',
                    params: {workspaceId},
                  })
                } else {
                  return next({
                    name: 'SocialWorkspaceStep2',
                    params: {workspaceId},
                  })
                }
              }

              return next()
            },
            props: {
              default: (route) => ({
                workspaceId: route.params.workspaceId,
                moduleName: 'Social',
              }),
              secondColumn: {step: 'step3', moduleName: 'Social'},
            },
          },
        ],
      },

      {
        name: 'SocialProjectReports',
        path: 'workspace/:workspaceId/project/:projectId/',
        component: SocialProjectDashboardView,
        children: [
          {
            name: 'SocialDashboard',
            path: 'dashboard',
            component: SocialProjectDashboard,
          },
          {
            name: 'SocialSearch',
            path: 'search-settings',
            component: SocialSearch,
          },
          {
            name: 'SocialFeature',
            path: 'feature',
            component: SocialFeaturesView,
            children: [
              {
                name: 'SocialSummary',
                path: 'summary',
                component: SocialSummaryScreen,
              },
              {
                name: 'SocialSentiment',
                path: 'sentiment',
                component: SocialSentimentScreen,
              },
            ],
          },
        ],
      },
    ],
  },
]
