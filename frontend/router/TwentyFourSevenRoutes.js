import store from '@store'

import TFSModuleView from '@/views/twenty-four-seven/TFSModuleView'
import TFSWorkspacesView from '@/views/twenty-four-seven/TFSWorkspacesView'
import CreateTFSView from '@/views/twenty-four-seven/CreateTFSView'
import TFSWorkspaceView from '@/views/twenty-four-seven/TFSWorkspaceView'
import TFSDashboardView from '@/views/twenty-four-seven/TFSDashboardView'

import CreateTFSWorkspace from '@/components/twenty-four-seven/CreateTFSWorkspace'
import CreateTFSProject from '@/components/twenty-four-seven/CreateTFSProject'
import CreateSearchTFS from '@/components/twenty-four-seven/CreateSearchTFS'
import CreateTFSRightSide from '@/components/twenty-four-seven/CreateTFSRightSide'
import SearchResults from '@/components/SearchResults'

import TFSDashboardScreen from '@/components/twenty-four-seven/screens/TFSDashboardScreen'

export default [
  {
    name: 'TwentyFourSeven',
    path: '/twenty-four-seven-module',
    component: TFSModuleView,
    redirect: () => ({name: 'TwentyFourSevenWorkspaces'}),
    children: [
      {
        name: 'TwentyFourSevenWorkspaces',
        path: '',
        component: TFSWorkspacesView,
      },

      {
        name: 'TFSWorkspace',
        path: 'workspace/:workspaceId',
        component: TFSWorkspaceView,
      },
    ],
  },

  {
    name: 'TwentyFourSevenCreateWorkspace',
    path: '/twenty-four-seven-module/workspace/:workspaceId/create',
    component: CreateTFSView,
    redirect: () => ({name: 'TFSWorkspaceStep1'}),
    children: [
      {
        name: 'TFSWorkspaceStep1',
        path: 'step1',
        components: {
          default: CreateTFSWorkspace,
          secondColumn: CreateTFSRightSide,
        },
        props: {
          default: {moduleName: 'TFS'},
          secondColumn: {step: 'step1'},
        },
        params: {step: 'step1'},
      },
      {
        name: 'TFSWorkspaceStep2',
        path: 'step2',
        components: {
          default: CreateTFSProject,
          secondColumn: CreateTFSRightSide,
        },
        props: {
          default: {moduleName: 'TFS'},
          secondColumn: {step: 'step2'},
        },
        params: {step: 'step2'},
        beforeEnter: (to, from, next) => {
          const workspaceId = to.params.workspaceId
          const currentStep = `TFSWorkspaceStep${store.state.newTFSWorkspace.step}`

          if (to.name !== currentStep && workspaceId === 'new') {
            return next({
              name: 'TFSWorkspaceStep1',
              params: {workspaceId},
            })
          }
          return next()
        },
      },
      {
        name: 'TFSWorkspaceStep3',
        path: 'step3',
        components: {
          default: CreateSearchTFS,
          secondColumn: SearchResults,
        },
        props: {
          secondColumn: {step: 'step3', moduleName: 'TFS'},
          default: (route) => ({
            workspaceId: route.params.workspaceId,
            moduleName: 'TFS',
          }),
        },
        params: {step: 'step3'},
        beforeEnter: (to, from, next) => {
          if (to.name !== store.state.newTFSProject.step) {
            const workspaceId = to.params.workspaceId
            if (workspaceId === 'new') {
              return next({
                name: 'TFSWorkspaceStep1',
                params: {workspaceId},
              })
            } else {
              return next({
                name: 'TFSWorkspaceStep2',
                params: {workspaceId},
              })
            }
          }

          return next()
        },
      },
    ],
  },

  {
    name: 'TFSDashboard',
    path: '/twenty-four-seven/workspace/:workspaceId/project/:projectId/',
    component: TFSDashboardView,
    redirect: () => ({name: 'TFSDashboardScreen'}),
    children: [
      {
        name: 'TFSDashboardScreen',
        path: 'dashboard',
        component: TFSDashboardScreen,
      },
    ],
  },
]
