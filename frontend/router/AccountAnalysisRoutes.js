import AccountAnalysisModuleView from '@/views/AccountAnalysisModuleView'
import CreateAccountAnalysisView from '@/views/CreateAccountAnalysisView'

import CreateAccountAnalysisProject from '@/components/account-analysis/CreateAccountAnalysisProject'
import CreateAccountAnalysisWorkspace from '@/components/account-analysis/CreateAccountAnalysisWorkspace'
import CreateAccountAnalysisRightSide from '@/components/account-analysis/CreateAccountAnalysisRightSide'

export default [
  {
    name: 'AccountAnalysis',
    path: '/account-analysis-module',
    component: AccountAnalysisModuleView,
  },

  {
    name: 'AccountAnalysisCreateWorkspace',
    path: '/account-analysis-module/workspace/:workspaceId/create',
    component: CreateAccountAnalysisView,
    redirect: () => ({name: 'AccountAnalysisWorkspaceStep1'}),
    children: [
      {
        name: 'AccountAnalysisWorkspaceStep1',
        path: 'step1',
        components: {
          default: CreateAccountAnalysisWorkspace,
          secondColumn: CreateAccountAnalysisRightSide,
        },
        props: {
          default: {moduleName: 'AccountAnalysis'},
          secondColumn: {step: 'step1'},
        },
      },
      {
        name: 'AccountAnalysisWorkspaceStep2',
        path: 'step2',
        components: {
          default: CreateAccountAnalysisProject,
          secondColumn: CreateAccountAnalysisRightSide,
        },
        props: {
          secondColumn: {step: 'step2'},
        },
      },
    ],
  },
]
