import WidgetsView from '@views/WidgetsView'

export default [
  {
    name: 'ReportWidgetView',
    path: '/api/reports/:widgetScreenshot/:projectId/',
    component: WidgetsView,
  },
]
