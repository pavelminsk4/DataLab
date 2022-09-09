import WorkspaceList from '@components/dashboard/DashboardList'
import CreateProjectScreen from '@components/project/CreateProjectScreen'
import WorkspaceScreen from '@components/workspace/WorkspaceScreen'

export const routes = [
  {
    name: 'Home',
    path: '',
    component: WorkspaceList,
  },

  {
    name: 'CreateProject',
    path: '/projects/create',
    component: CreateProjectScreen,
  },

  {
    name: 'Workspace',
    path: '/workspace/:workspaceId',
    component: WorkspaceScreen,
  },
]
