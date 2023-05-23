import store from '@store'

import TFSModuleView from '@/views/tweny-four-seven/TFSModuleView'
import TFSWorkspacesView from '@/views/tweny-four-seven/TFSWorkspacesView'
import CreateTFSView from '@/views/tweny-four-seven/CreateTFSView'
import TFSWorkspaceView from '@/views/tweny-four-seven/TFSWorkspaceView'

import CreateTFSWorkspace from '@/components/tweny-four-seven/CreateTFSWorkspace'
import CreateTFSProject from '@/components/tweny-four-seven/CreateTFSProject'
import CreateSearchTFS from '@/components/tweny-four-seven/CreateSearchTFS'
import CreateTFSRightSide from '@/components/tweny-four-seven/CreateTFSRightSide'
import TFSSearchResults from '@/components/tweny-four-seven/TFSSearchResults'

export default [
  {
    name: 'TwenyFourSeven',
    path: '/tweny-four-seven-module',
    component: TFSModuleView,
    redirect: () => ({name: 'TwenyFourSevenWorkspaces'}),
    children: [
      {
        name: 'TwenyFourSevenWorkspaces',
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
    name: 'TwenyFourSevenCreateWorkspace',
    path: '/tweny-four-seven-module/workspace/:workspaceId/create',
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
          console.log(to.params.workspaceId)
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
          secondColumn: TFSSearchResults,
        },
        props: {
          secondColumn: {step: 'step3'},
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
]
