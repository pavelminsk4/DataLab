import store from '@store'

import WorkspacesView from '@/components/dashboard/WorkspacesView'
import WorkspaceView from '@/components/workspace/WorkspaceView'

import CreateWorkspaceView from '@/components/workspace/CreateWorkspaceView'
import CreateSearchScreen from '@/components/workspace/screens/CreateSearchScreen'
import CreateProjectScreen from '@/components/workspace/screens/CreateProjectScreen'
import CreateWorkspaceScreen from '@/components/workspace/screens/CreateWorkspaceScreen'
import CreateWorkspaceRightSide from '@/components/workspace/CreateWorkspaceRightSide'
import SearchResults from '@/components/SearchResults'

import UserRolesScreen from '@/components/settings/UserRolesScreen'
import ProjectExtraSettingsView from '@/components/project/ProjectExtraSettingsView'

import SearchScreen from '@/components/project/screens/SearchScreen'
import AnalyticsScreen from '@/components/project/screens/AnalyticsScreen'

export const routes = [
  {
    path: '/',
    component: WorkspacesView,
  },

  {
    name: 'Home',
    path: '/dashboard',
    component: WorkspacesView,
  },

  {
    name: 'CreateWorkspace',
    path: '/workspace/new/',
    component: CreateWorkspaceView,
    children: [
      {
        name: 'Step1',
        path: 'step1',
        components: {
          default: CreateWorkspaceScreen,
          secondColumn: CreateWorkspaceRightSide,
        },
        props: {secondColumn: {step: 'step1'}},
      },
      {
        name: 'Step2',
        path: 'step2',
        components: {
          default: CreateProjectScreen,
          secondColumn: CreateWorkspaceRightSide,
        },
        beforeEnter: (to, from, next) => {
          if (to.name !== store.state.currentStep) return next({name: 'Step1'})

          return next()
        },
        props: {secondColumn: {step: 'step2'}},
      },
      {
        name: 'Step3',
        path: 'step3',
        components: {
          default: CreateSearchScreen,
          secondColumn: SearchResults,
        },
        beforeEnter: (to, from, next) => {
          if (to.name !== store.state.currentStep) return next({name: 'Step1'})

          return next()
        },
        props: {secondColumn: {step: 'step3'}},
      },
    ],
  },

  {
    name: 'CreateProject',
    path: '/workspace/:workspaceId/project/new/',
    component: CreateWorkspaceView,
    children: [
      {
        name: 'WorkspaceStep2',
        path: 'step2',
        components: {
          default: CreateProjectScreen,
          secondColumn: CreateWorkspaceRightSide,
        },
        props: {
          default: (route) => ({workspaceId: +route.params.workspaceId}),
          secondColumn: {step: 'step2'},
        },
      },
      {
        name: 'WorkspaceStep3',
        path: 'step3',
        components: {
          default: CreateSearchScreen,
          secondColumn: SearchResults,
        },
        beforeEnter: (to, from, next) => {
          if (to.name !== store.state.currentStep)
            return next({
              name: 'WorkspaceStep2',
              params: {workspaceId: to.params.workspaceId},
            })

          return next()
        },
        props: {
          default: (route) => ({workspaceId: +route.params.workspaceId}),
          secondColumn: {step: 'step3'},
        },
      },
    ],
  },

  {
    name: 'Workspace',
    path: '/workspace/:workspaceId',
    component: WorkspaceView,
  },

  {
    name: 'UserRoles',
    path: '/user-roles',
    component: UserRolesScreen,
  },

  {
    name: 'ProjectReports',
    path: '/workspace/:workspaceId/project/:projectId/',
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
]
