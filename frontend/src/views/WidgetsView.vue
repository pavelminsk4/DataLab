<template>
  <WidgetsList
    v-if="selectedWidgets"
    :selected-widgets="selectedWidgets"
    listWidth="100vw"
    :module-name="widgetData.module_name"
  />
</template>

<script>
import {mapState, mapActions} from 'vuex'
import {action} from '@store/constants'
import {getWidgetDetails} from '@lib/utilities'
import {MODES} from '@lib/constants'

import WidgetsList from '@components/widgets/WidgetsList'

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
          this.widgetData.module_name
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
    this[action.UPDATE_MODE](MODES.CREATE_REPORT)
  },
  methods: {
    ...mapActions([action.UPDATE_MODE]),
  },
}
</script>
