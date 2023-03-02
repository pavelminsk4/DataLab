import store from '@store'
import ModuleView from '@/views/ModuleView'
import OnlineWorkspacesView from '@/views/OnlineWorkspacesView'

import WorkspaceView from '@/components/workspace/WorkspaceView'
import ProjectExtraSettingsView from '@/components/project/ProjectExtraSettingsView'

import CreateWorkspaceView from '@/components/workspace/CreateWorkspaceView'
import CreateSearchScreen from '@/components/workspace/screens/CreateSearchScreen'
import CreateProjectScreen from '@/components/workspace/screens/CreateProjectScreen'
import CreateWorkspaceScreen from '@/components/workspace/screens/CreateWorkspaceScreen'
import CreateWorkspaceRightSide from '@/components/workspace/CreateWorkspaceRightSide'
import SearchResults from '@/components/SearchResults'

import SearchScreen from '@/components/project/screens/SearchScreen'
import AnalyticsScreen from '@/components/project/screens/AnalyticsScreen'

export default [
  {
    path: '/online-module',
    component: ModuleView,
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
        component: WorkspaceView,
      },

      {
        name: 'OnlineCreateWorkspace',
        path: 'workspace/:workspaceId/',
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
            props: {secondColumn: {step: 'step1'}},
          },
          {
            name: 'OnlineWorkspaceStep2',
            path: 'step2',
            components: {
              default: CreateProjectScreen,
              secondColumn: CreateWorkspaceRightSide,
            },
            beforeEnter: (to, from, next) => {
              if (to.name !== store.state.currentStep)
                return next({
                  name: 'OnlineWorkspaceStep1',
                  params: {workspaceId: to.params.workspaceId},
                })

              return next()
            },
            props: {
              default: (route) => ({workspaceId: route.params.workspaceId}),
              secondColumn: {step: 'step2'},
            },
          },
          {
            name: 'OnlineWorkspaceStep3',
            path: 'step3',
            components: {
              default: CreateSearchScreen,
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
              default: (route) => ({workspaceId: route.params.workspaceId}),
              secondColumn: {step: 'step3'},
            },
          },
        ],
      },

      {
        name: 'ProjectReports',
        path: 'workspace/:workspaceId/project/:projectId/',
        component: ProjectExtraSettingsView,
        children: [
          {
            name: 'Analytics',
            path: 'analytics',
            component: AnalyticsScreen,
          },
          {
            name: 'Search',
            path: 'search-settings',
            component: SearchScreen,
          },
        ],
      },
    ],
  },
]
