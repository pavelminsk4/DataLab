import WorkspaceList from '@components/dashboard/DashboardList'
import WorkspaceScreen from '@components/workspace/WorkspaceScreen'

import CreateSearchScreen from '@components/workspace/new/CreateSearchScreen'
import CreateProjectScreen from '@components/workspace/new/CreateProjectScreen'
import CreateWorkspaceScreen from '@components/workspace/new/CreateWorkspaceScreen'
import CreateWorkspaceView from '@components/workspace/CreateWorkspaceView'

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
      },
      {
        name: 'Step3',
        path: 'step3',
        component: CreateSearchScreen,
      },
    ],
  },

  {
    name: 'Workspace',
    path: '/workspace/:workspaceId',
    component: WorkspaceScreen,
  },
]
