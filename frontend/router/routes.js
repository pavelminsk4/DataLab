import store from '@store'

import WorkspacesView from '@/components/dashboard/WorkspacesView'
import WorkspaceView from '@/components/workspace/WorkspaceView'

import CreateProjectView from '@/components/project/CreateProjectView'
import CreateWorkspaceView from '@/components/workspace/CreateWorkspaceView'
import CreateSearchScreen from '@/components/workspace/screens/CreateSearchScreen'
import CreateProjectScreen from '@/components/workspace/screens/CreateProjectScreen'
import CreateWorkspaceScreen from '@/components/workspace/screens/CreateWorkspaceScreen'
import CreateWorkspaceRightSide from '@/components/workspace/CreateWorkspaceRightSide'

import UserRolesScreen from '@/components/settings/UserRolesScreen'
import ProjectExtraSettingsView from '@/components/project/ProjectExtraSettingsView'

import SearchScreen from '@/components/project/screens/SearchScreen'
import AlertsScreen from '@/components/project/screens/AlertsScreen'
import RegularReportsScreen from '@/components/project/screens/RegularReportsScreen'
import RegularReportSettingsScreen from '@/components/project/screens/RegularReportSettingsScreen'
import AnalyticsScreen from '@/components/project/screens/AnalyticsScreen'
import AlertSettingsScreen from '@/components/project/screens/AlertSettingsScreen'

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
          secondColumn: CreateWorkspaceRightSide,
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
    component: CreateProjectView,
    children: [
      {
        name: 'ProjectStep1',
        path: 'project-step-1',
        component: CreateProjectScreen,
      },
      {
        name: 'ProjectStep2',
        path: 'project-step-2',
        component: CreateSearchScreen,
        beforeEnter: (to, from, next) => {
          if (to.name !== store.state.currentStep)
            return next({
              name: 'ProjectStep1',
              params: {workspaceId: to.params.workspaceId},
            })

          return next()
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
      {
        name: 'Alerts',
        path: 'alerts',
        component: AlertsScreen,
      },
      {
        name: 'NewAlert',
        path: 'create-new-alert',
        component: AlertSettingsScreen,
      },
      {
        name: 'UpdateAlert',
        path: 'update/:alertId/alert',
        component: AlertSettingsScreen,
      },
      {
        name: 'Reports',
        path: 'reports',
        component: RegularReportsScreen,
      },
      {
        name: 'NewRegularReport',
        path: 'create-new-regular-report',
        component: RegularReportSettingsScreen,
      },
      {
        name: 'UpdateRegularReport',
        path: 'update/:regularReportId/regular-report',
        component: RegularReportSettingsScreen,
      },
    ],
  },
]
