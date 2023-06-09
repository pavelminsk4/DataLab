import store from '@store'
import ComparisonModuleView from '@/views/ComparisonModuleView'

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
        props: {
          default: {moduleName: 'Comparison '},
          secondColumn: {step: 'step1'},
        },
        params: {step: 'step1'},
      },
      {
        name: 'ComparisonWorkspaceStep2',
        path: 'step2',
        components: {
          default: CreateComparisonProject,
          secondColumn: CreateComparisonRightSide,
        },
        props: {
          default: {moduleName: 'Comparison'},
          secondColumn: {step: 'step2'},
        },
        params: {step: 'step2'},
        beforeEnter: (to, from, next) => {
          const workspaceId = to.params.workspaceId
          const {step} = store.state.comparison.newWorkspace

          if (step !== 2 && workspaceId === 'new') {
            return next({
              name: 'ComparisonWorkspaceStep1',
              params: {workspaceId},
            })
          }
          return next()
        },
      },
      {
        name: 'ComparisonWorkspaceStep3',
        path: 'step3',
        components: {
          default: CreateDefineComparison,
          secondColumn: CreateComparisonRightSide,
        },
        props: {
          default: {moduleName: 'Comparison'},
          secondColumn: {step: 'step3'},
        },
        params: {step: 'step3'},
        // beforeEnter: (to, from, next) => {
        //   const {step} = store.state.comparison.newWorkspace
        //   const workspaceId = to.params.workspaceId

        //   if (step !== 3) {
        //     return next({
        //       name: 'ComparisonWorkspaceStep1',
        //       params: {workspaceId},
        //     })
        //   } else return next()
        // },
      },
    ],
  },
]
