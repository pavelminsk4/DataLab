<template>
  <WidgetsList
    v-if="selectedWidgets"
    :current-project="currentProject"
    :selected-widgets="selectedWidgets"
    module-name="Online"
  />
</template>

<script>
import {mapGetters, createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'
import {getWidgetDetails} from '@lib/utilities'
import {onlineWidgetsList} from '@lib/constants'

import WidgetsList from '@components/widgets/WidgetsList'

const {mapActions} = createNamespacedHelpers('online')

export default {
  name: 'OnlineDemographyScreen',
  components: {
    WidgetsList,
  },
  props: {
    currentProject: {type: [Array, Object], required: false},
  },
  computed: {
    ...mapGetters({
      availableWidgets: get.AVAILABLE_WIDGETS,
    }),
    selectedWidgets: {
      get() {
        if (!this.availableWidgets) return
        return onlineWidgetsList.demography
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
    if (!this.availableWidgets) {
      this[action.GET_AVAILABLE_WIDGETS](this.currentProject.id)
    }
  },
  methods: {
    ...mapActions([action.GET_AVAILABLE_WIDGETS]),
  },
}
</script>

<style lang="scss" scoped>
.summary {
  display: flex;
  flex-direction: column;
  gap: 30px;
}
.summary__header {
  display: flex;
  justify-content: space-between;

  .btn-report {
    align-self: flex-end;
  }
}
</style>
