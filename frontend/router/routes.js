import store from '@store'

import WorkspaceList from '@/components/dashboard/DashboardList'
import WorkspaceView from '@/components/workspace/WorkspaceView'

import CreateSearchScreen from '@/components/workspace/screens/CreateSearchScreen'
import CreateProjectScreen from '@/components/workspace/screens/CreateProjectScreen'
import CreateWorkspaceScreen from '@/components/workspace/screens/CreateWorkspaceScreen'
import CreateWorkspaceView from '@/components/workspace/CreateWorkspaceView'
import CreateProjectView from '@/components/project/CreateProjectView'

import ProjectReports from '@/components/project/screens/ProjectReports'

export const routes = [
  {
    path: '/',
    component: WorkspaceList,
  },

  {
    name: 'Home',
    path: '/dashboard',
    component: WorkspaceList,
  },

  {
    name: 'CreateWorkspace',
    path: '/workspace/new/',
    component: CreateWorkspaceView,
    children: [
      {
        name: 'Step1',
        path: 'step1',
        component: CreateWorkspaceScreen,
      },
      {
        name: 'Step2',
        path: 'step2',
        component: CreateProjectScreen,
        beforeEnter: (to, from, next) => {
          if (to.name !== store.state.currentStep) next({name: 'Step1'})

          next()
        },
      },
      {
        name: 'Step3',
        path: 'step3',
        component: CreateSearchScreen,
        beforeEnter: (to, from, next) => {
          if (to.name !== store.state.currentStep) next({name: 'Step1'})

          next()
        },
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
            next({
              name: 'ProjectStep1',
              params: {workspaceId: to.params.workspaceId},
            })

          next()
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
    name: 'ProjectReports',
    path: '/workspace/:workspaceId/project/:projectId',
    component: ProjectReports,
  },
]
