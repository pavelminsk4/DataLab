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
  name: 'ComparisonSentimentScreen',
  components: {
    WidgetsList,
  },
  props: {
    currentProject: {type: [Array, Object], required: false},
    projectsModule: {type: String, required: true},
  },
  computed: {
    ...mapState(['sentiment']),

    selectedWidgets() {
      if (!this.sentiment.widgets.length) return
      return comparisonWidgetsList[this.projectsModule].sentiment
        .map((widget) => {
          const foundWidget = this.sentiment.widgets.find(
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
    this[action.GET_SENTIMENT_WIDGETS](this.currentProject.id)
  },
  methods: {
    ...mapActions([action.GET_SENTIMENT_WIDGETS]),
  },
}
</script>
