<template>
  <WidgetsList
    v-if="selectedWidgets"
    :current-project="currentProject"
    :selected-widgets="selectedWidgets"
    module-name="Online"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import {getWidgetDetails} from '@lib/utilities'

import WidgetsList from '@/components/widgets/WidgetsList'

export default {
  name: 'OnlineInfluencersScreen',
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
        return this.widgets
          .map((widget) => {
            if (this.availableWidgets[widget.name]) {
              return {
                widgetDetails: getWidgetDetails(
                  widget.name,
                  this.availableWidgets[widget.name],
                  this.currentProject.id
                ),
                isFullWidth: widget.isFullWidth,
              }
            }
          })
          .filter((widgets) => widgets)
      },
    },
  },
  async created() {
    this.widgets = [
      {name: 'top_sharing_sources', isFullWidth: false},
      {name: 'authors_by_country', isFullWidth: false},
      {name: 'overall_top_sources', isFullWidth: true},
      {name: 'sources_by_language', isFullWidth: false},
    ]
  },
  methods: {
    ...mapActions([action.UPDATE_AVAILABLE_WIDGETS]),
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
