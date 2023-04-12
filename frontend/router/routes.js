import MainView from '@/views/MainView'
import ReportsView from '@/views/ReportsView'

import CreateReportView from '@/views/CreateReportView'
import CreateReportRightSide from '@/components/reports/CreateReportRightSide'
import CreateReportName from '@/components/reports/CreateReportName'
import CreateReportSetTime from '@/components/reports/CreateReportSetTime'
import CreateReportAddProject from '@/components/reports/CreateReportAddProject'
import CreateReportChooseTemplate from '@/components/reports/CreateReportChooseTemplate'
import ReportsSettingsTemplate from '@/components/reports/ReportsSettingsTemplate'
import CreateReportEditReport from '@/components/reports/CreateReportEditReport'

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

  {
    name: 'Reports',
    path: '/reports',
    component: ReportsView,
  },

  {
    name: 'CreateReport',
    path: '/reports/create',
    component: CreateReportView,
    redirect: () => ({name: 'ReportStep1'}),
    children: [
      {
        name: 'ReportStep1',
        path: 'step1',
        components: {
          default: CreateReportName,
          secondColumn: CreateReportRightSide,
        },
        props: {
          secondColumn: {step: 'step1'},
        },
      },
      {
        name: 'ReportStep2',
        path: 'step2',
        components: {
          default: CreateReportSetTime,
          secondColumn: CreateReportRightSide,
        },
        props: {
          secondColumn: {step: 'step2'},
        },
      },
      {
        name: 'ReportStep3',
        path: 'step3',
        component: CreateReportAddProject,
      },

      {
        name: 'ReportStep4',
        path: 'step4',
        components: {
          default: CreateReportChooseTemplate,
          secondColumn: ReportsSettingsTemplate,
        },
      },

      {
        name: 'ReportStep5',
        path: 'step5',
        components: {
          default: CreateReportEditReport,
          // secondColumn: `<template>mm</template>`,
        },
      },
    ],
  },
]
