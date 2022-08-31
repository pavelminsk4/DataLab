import WorkspaceList from '@components/dashboard/DashboardList'
import CreateProjectScreen from '@/components/project/CreateProjectScreen'

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
]
