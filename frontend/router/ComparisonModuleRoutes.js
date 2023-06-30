import store from '@store'

import ComparisonModuleView from '@/views/comparison/ComparisonModuleView'
import CreateComparisonView from '@/views/comparison/CreateComparisonView'
import CreateComparisonWorkspace from '@/components/comparison/CreateComparisonWorkspace'
import CreateComparisonProject from '@/components/comparison/CreateComparisonProject'
import CreateComparisonRightSide from '@/components/comparison/CreateComparisonRightSide'
import CreateDefineComparison from '@/components/comparison/CreateDefineComparison'

export default [
  {
    name: 'Comparison',
    path: '/comparison',
    component: ComparisonModuleView,
  },
  {
    name: 'ComparisonCreateWorkspace',
    path: '/comparison-module/workspace/:workspaceId/create',
    component: CreateComparisonView,
    redirect: () => ({name: 'ComparisonWorkspaceStep1'}),
    children: [
      {
        name: 'ComparisonWorkspaceStep1',
        path: 'step1',
        components: {
          default: CreateComparisonWorkspace,
          secondColumn: CreateComparisonRightSide,
        },
        params: {step: 'step1'},
        props: {
          default: {moduleName: 'Comparison '},
          secondColumn: {step: 'step1'},
        },
      },
      {
        name: 'ComparisonWorkspaceStep2',
        path: 'step2',
        components: {
          default: CreateComparisonProject,
          secondColumn: CreateComparisonRightSide,
        },
        params: {step: 'step2'},
        beforeEnter: (to, from, next) => {
          const workspaceId = to.params.workspaceId
          const {step} = store.state.comparison.newWorkspace

          if (workspaceId === 'new' && step !== 2) {
            return next({
              name: 'ComparisonWorkspaceStep1',
              params: {workspaceId},
            })
          }
          return next()
        },
        props: {
          default: (route) => ({
            workspaceId: route.params.workspaceId,
            moduleName: 'Comparison',
          }),
          secondColumn: {step: 'step2'},
        },
      },
      {
        name: 'ComparisonWorkspaceStep3',
        path: 'step3',
        components: {
          default: CreateDefineComparison,
          secondColumn: CreateComparisonRightSide,
        },

        params: {step: 'step3'},
        beforeEnter: (to, from, next) => {
          const {step} = store.state.comparison.newWorkspace

          if (step !== 3) {
            const workspaceId = to.params.workspaceId
            if (workspaceId === 'new') {
              return next({
                name: 'ComparisonWorkspaceStep1',
                params: {workspaceId},
              })
            } else {
              return next({
                name: 'ComparisonWorkspaceStep2',
                params: {workspaceId},
              })
            }
          }

          return next()
        },
        props: {
          default: (route) => ({
            workspaceId: route.params.workspaceId,
            moduleName: 'Comparison',
          }),
          secondColumn: {step: 'step3'},
        },
      },
    ],
  },
]