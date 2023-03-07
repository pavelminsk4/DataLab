import store from '@store'
import SocialModuleView from '@/views/SocialModuleView'
import SocialWorkspacesView from '@/views/SocialWorkspacesView'
import SocialWorkspaceView from '@/views/SocialWorkspaceView'

import ProjectExtraSettingsView from '@/components/project/ProjectExtraSettingsView'

import CreateWorkspaceView from '@/components/workspace/CreateWorkspaceView'
import SocialCreateSearchScreen from '@/components/workspace/screens/SocialCreateSearchScreen'
import CreateProjectScreen from '@/components/workspace/screens/CreateProjectScreen'
import CreateWorkspaceScreen from '@/components/workspace/screens/CreateWorkspaceScreen'
import CreateWorkspaceRightSide from '@/components/workspace/CreateWorkspaceRightSide'
import SearchResults from '@/components/SearchResults'

import SearchScreen from '@/components/project/screens/SearchScreen'
import AnalyticsScreen from '@/components/project/screens/AnalyticsScreen'

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
              secondColumn: {step: 'step3'},
            },
          },
        ],
      },

      {
        name: 'SocialProjectReports',
        path: 'workspace/:workspaceId/project/:projectId/',
        component: ProjectExtraSettingsView,
        children: [
          {
            name: 'SocialAnalytics',
            path: 'analytics',
            component: AnalyticsScreen,
          },
          {
            name: 'SocialSearch',
            path: 'search-settings',
            component: SearchScreen,
          },
        ],
      },
    ],
  },
]
