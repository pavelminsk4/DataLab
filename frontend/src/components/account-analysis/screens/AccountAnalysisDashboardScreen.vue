<template>
  <WidgetsList
    v-if="selectedWidgets.length"
    :current-project="currentProject"
    :selected-widgets="selectedWidgets"
    module-name="AccountAnalysis"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'

import {accountAnalysisWidgetsList} from '@/lib/constants'
import {getWidgetDetails} from '@lib/utilities'
import {stringToPascalCase} from '@/lib/utilities'

import WidgetsList from '@/components/widgets/WidgetsList'

const {mapActions, mapGetters} = createNamespacedHelpers('accountAnalysis')

export default {
  name: 'AccountAnalysisDashboardScreen',
  components: {WidgetsList},
  props: {
    currentProject: {type: Object, required: true},
    currentTab: {type: String, required: true},
  },
  computed: {
    ...mapGetters({
      availableWidgets: get.AVAILABLE_WIDGETS,
    }),
    selectedWidgets: {
      get() {
        const tab = stringToPascalCase(this.currentTab)

        if (!this.availableWidgets) return
        return accountAnalysisWidgetsList[tab].dashboard
          .map((widget) => {
            if (this.availableWidgets[widget.name]) {
              return {
                widgetDetails: getWidgetDetails(
                  widget.name,
                  this.availableWidgets[widget.name],
                  this.currentProject.id,
                  this.currentProject.source
                ),
                isFullWidth: widget.isFullWidth,
                isShowDeleteBtn: false,
                minHeight: widget.minHeight || 400,
              }
            }
          })
          .filter((widgets) => widgets)
      },
    },
  },
  created() {
    if (!this.availableWidgets.length && this.currentProject) {
      this[action.GET_AVAILABLE_WIDGETS](this.currentProject.id)
    }
  },
  methods: {
    ...mapActions([action.GET_AVAILABLE_WIDGETS]),
  },
}
</script>
