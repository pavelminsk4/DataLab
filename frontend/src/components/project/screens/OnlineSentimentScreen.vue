<template>
  <WidgetsList
    v-if="selectedWidgets"
    :current-project="currentProject"
    :selected-widgets="selectedWidgets"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import {getWidgetDetails} from '@lib/utilities'

import WidgetsList from '@/components/widgets/WidgetsList'

export default {
  name: 'OnlineSentimentScreen',
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
      {name: 'sentiment_number_of_results'},
      {name: 'sentiment_diagram'},
      {name: 'sentiment_top_10_authors_widget'},
      {name: 'top_keywords'},
      {name: 'sentiment_top_10_sources_widget', isFullWidth: true},
      {name: 'sentiment_top_10_countries_widget'},
      {name: 'sentiment_top_10_languages_widget'},
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
