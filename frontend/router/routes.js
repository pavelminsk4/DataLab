import WorkspaceList from '@components/dashboard/DashboardList'
import CreateProjectScreen from '@components/project/CreateProjectScreen'
import WorkspaceScreen from '@components/workspace/WorkspaceScreen'

export const routes = [
  {
    name: 'Home',
    path: '/dashboard',
    component: WorkspaceList,
  },

  {
    name: 'CreateProject',
    path: '/workspace/create/lol/keke',
    component: CreateProjectScreen,
  },

  {
    name: 'Workspace',
    path: '/workspace/:workspaceId',
    component: WorkspaceScreen,
  },
]
