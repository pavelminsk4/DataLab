<template>
  <WidgetsList
    v-if="selectedWidgets"
    :current-project="currentProject"
    :selected-widgets="selectedWidgets"
    module-name="Comparison"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'
import {comparisonWidgetsList} from '@/lib/constants'

import WidgetsList from '@/components/widgets/WidgetsList'
import {stringToPascalCase} from '@/lib/utilities'

const {mapActions, mapState} = createNamespacedHelpers('comparison/widgets')

export default {
  name: 'ComparisonSummaryScreen',
  components: {
    WidgetsList,
  },
  props: {
    currentProject: {type: [Array, Object], required: false},
    projectsModule: {type: String, required: true},
  },
  computed: {
    ...mapState(['summary']),

    selectedWidgets() {
      if (!this.summary.widgets.length) return
      return comparisonWidgetsList[this.projectsModule].summary
        .map((widget) => {
          const foundWidget = this.summary.widgets.find(
            (el) => el.widget_name === widget.name
          )

          if (foundWidget) {
            return {
              widgetDetails: {
                ...foundWidget.description,
                widgetData: foundWidget.projects_data,
                widgetName: stringToPascalCase(foundWidget.widget_name),
              },
              isFullWidth: widget.isFullWidth,
              isShowDeleteBtn: false,
              isShowSettingsBtn: false,
              minHeight: widget.minHeight || 400,
            }
          }
        })
        .filter((widgets) => widgets)
    },
  },
  created() {
    this[action.GET_SUMMARY_WIDGETS](this.currentProject.id)
  },
  methods: {
    ...mapActions([action.GET_SUMMARY_WIDGETS]),
  },
}
</script>
