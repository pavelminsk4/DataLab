<template>
  <WidgetsList
    v-if="!sentiment.isLoading"
    :current-project="currentProject"
    :selected-widgets="selectedWidgets"
    :comparisonModule="projectsModule"
    module-name="Comparison"
  />
  <div v-else class="spinner">
    <BaseSpinner />
  </div>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'
import {comparisonWidgetsList} from '@lib/constants'
import {stringToPascalCase} from '@lib/utilities'

import WidgetsList from '@components/widgets/WidgetsList'
import BaseSpinner from '@components/BaseSpinner'

const {mapActions, mapState} = createNamespacedHelpers('comparison/widgets')

export default {
  name: 'ComparisonSentimentScreen',
  components: {
    WidgetsList,
    BaseSpinner,
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
                currentModule: 'Comparison',
                widgetId: foundWidget.widget_id,
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

<style lang="scss" scoped>
.spinner {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 100%;
  height: 50vh;
}
</style>
