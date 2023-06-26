<template>
  <WidgetsList
    v-if="selectedWidgets"
    :selected-widgets="selectedWidgets"
    module-name="Social"
  />
</template>

<script>
import {getWidgetDetails} from '@lib/utilities'

import WidgetsList from '@/components/widgets/WidgetsList'

export default {
  name: 'TestWidget',
  components: {
    WidgetsList,
  },
  computed: {
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
            minHeight: 400,
          },
        ]
      },
    },
  },
  created() {
    this.widgetData = JSON.parse(document.getElementById('context').textContent)
  },
}
</script>
