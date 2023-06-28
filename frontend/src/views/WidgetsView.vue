<template>
  <WidgetsList
    v-if="selectedWidgets"
    :selected-widgets="selectedWidgets"
    listWidth="100vw"
    module-name="Social"
    class="widget-screen"
  />
</template>

<script>
import {mapState} from 'vuex'
import {getWidgetDetails} from '@lib/utilities'

import WidgetsList from '@/components/widgets/WidgetsList'

export default {
  name: 'WidgetsView',
  components: {
    WidgetsList,
  },
  computed: {
    ...mapState(['widgets']),
    projectId() {
      return this.$route.params.projectId
    },
    selectedWidgets: {
      get() {
        if (!this.widgetData) return

        const widgetName = Object.keys(this.widgetData.widget)[0]
        const widgetDetails = getWidgetDetails(
          widgetName,
          this.widgetData.widget[widgetName],
          this.projectId,
          'Social'
        )

        return [
          {
            widgetDetails: {
              ...widgetDetails,
              widgetData: this.widgetData.data,
            },
            isShowDeleteBtn: false,
            isShowSettingsBtn: false,
            minHeight: '100vh',
          },
        ]
      },
    },
  },
  created() {
    this.widgetData = JSON.parse(document.getElementById('context').textContent)
    this.widgets.hasAnimation = false
  },
}
</script>
