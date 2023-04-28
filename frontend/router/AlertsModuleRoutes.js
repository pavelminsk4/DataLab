import store from '@store'

import AlertsView from '@/views/AlertsView'
import CreateAlertName from '@/components/alerts/CreateAlertName'
import CreateAlertView from '@/views/CreateAlertView'
import CreateAlertRightSide from '@/components/alerts/CreateAlertRightSide'
import CreateAlertAddProject from '@/components/alerts/CreateAlertAddProject'
import SetAlertTrigger from '@/components/alerts/SetAlertTrigger'

export default [
  {
    name: 'Alerts',
    path: '/alerts',
    component: AlertsView,
  },

  {
    name: 'CreateAlert',
    path: '/alerts/create',
    component: CreateAlertView,
    redirect: () => ({name: 'AlertStep1'}),
    children: [
      {
        name: 'AlertStep1',
        path: 'step1',
        components: {
          default: CreateAlertName,
          secondColumn: CreateAlertRightSide,
        },
        props: {
          secondColumn: {step: 'step1'},
        },
      },
      {
        name: 'AlertStep2',
        path: 'step2',
        components: {
          default: SetAlertTrigger,
          secondColumn: CreateAlertRightSide,
        },
        props: {
          secondColumn: {step: 'step2'},
        },
        beforeEnter: (to, from, next) => {
          const {step} = store.state.alerts.newAlert
          if (step === 2) {
            next()
          } else {
            next('/alerts/create')
          }
        },
      },
      {
        name: 'AlertStep3',
        path: 'step3',
        component: CreateAlertAddProject,
        beforeEnter: (to, from, next) => {
          const {step} = store.state.alerts.newAlert
          if (step === 3) {
            next()
          } else {
            next('/alerts/create')
          }
        },
      },
    ],
  },
]
