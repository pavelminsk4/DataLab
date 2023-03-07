import MainView from '@/views/MainView'

import UserRolesScreen from '@/components/settings/UserRolesScreen'

export const routes = [
  {
    name: 'MainView',
    path: '/',
    component: MainView,
  },

  {
    name: 'UserRoles',
    path: '/user-roles',
    component: UserRolesScreen,
  },
]
