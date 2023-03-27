<template>
  <WidgetsList
    v-if="selectedWidgets"
    :current-project="currentProject"
    :selected-widgets="selectedWidgets"
    module-name="Social"
  />
</template>

<script>
import {mapGetters, createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'
const {mapActions, mapGetters: mapGettersSocial} =
  createNamespacedHelpers('social/widgets')

import {getWidgetDetails} from '@lib/utilities'

import WidgetsList from '@/components/widgets/WidgetsList'

export default {
  name: 'SocialSummaryScreen',
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
    ...mapGettersSocial({
      socialWidgets: get.SOCIAL_WIDGETS,
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
      {name: 'summary'},
      {name: 'sentiment'},
      {name: 'content_volume'},
      {name: 'top_keywords'},
      {name: 'top_authors'},

      {name: 'gender_volume'},
    ]
    if (!this.availableWidgets) {
      await this[action.GET_AVAILABLE_WIDGETS](this.currentProject.id)
    }
  },
  methods: {
    ...mapActions([
      action.GET_AVAILABLE_WIDGETS,
      action.UPDATE_AVAILABLE_WIDGETS,
    ]),
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
