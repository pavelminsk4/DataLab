<template>
  <WidgetsList
    v-if="!demography.isLoading"
    :current-project="currentProject"
    :selected-widgets="selectedWidgets"
    module-name="Comparison"
  />
  <div v-else class="spinner">
    <BaseSpinner />
  </div>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'
import {comparisonWidgetsList} from '@/lib/constants'
import {stringToPascalCase} from '@/lib/utilities'

import WidgetsList from '@/components/widgets/WidgetsList'
import BaseSpinner from '@/components/BaseSpinner'

const {mapActions, mapState} = createNamespacedHelpers('comparison/widgets')

export default {
  name: 'ComparisonDemographyScreen',
  components: {
    WidgetsList,
    BaseSpinner,
  },
  props: {
    currentProject: {type: [Array, Object], required: false},
    projectsModule: {type: String, required: true},
  },
  computed: {
    ...mapState(['demography']),

    selectedWidgets() {
      if (!this.demography.widgets.length) return
      return comparisonWidgetsList[this.projectsModule].demography
        .map((widget) => {
          const foundWidget = this.demography.widgets.find(
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
    this[action.GET_DEMOGRAPHY_WIDGETS](this.currentProject.id)
  },
  methods: {
    ...mapActions([action.GET_DEMOGRAPHY_WIDGETS]),
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
