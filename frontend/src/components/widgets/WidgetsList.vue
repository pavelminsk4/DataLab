<template>
  <ul class="widgets">
    <li
      v-for="item in selectedWidgets"
      :key="item.i"
      :static="item.static"
      :class="[
        'widgets__item',
        item.name === 'top_10_countries_widget' && 'grow',
      ]"
    >
      <component
        v-if="item.isWidget"
        :is="item.widgetName"
        :is-open-widget="item.isShow"
        :widgets="availableWidgets"
        :widget-id="item.widgetId"
        :current-project="currentProject"
        :project-id="currentProject.id"
        :chart-type="item.chartType"
        :title="item.title"
        :available-widgets="availableWidgets"
      />
    </li>
  </ul>
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import VolumeWidget from '@/components/widgets/online/VolumeWidget'
import SummaryWidget from '@/components/widgets/online/SummaryWidget'
import Top10BrandsWidget from '@/components/widgets/online/Top10BrandsWidget'
import Top10CountriesWidget from '@/components/widgets/online/Top10CountriesWidget'
import Top10LanguagesWidget from '@/components/widgets/online/Top10LanguagesWidget'
import Top10AuthorsByVolumeWidget from '@/components/widgets/online/Top10AuthorsByVolumeWidget'
import SentimentForPeriodWidget from '@/components/widgets/online/SentimentForPeriodWidget'
import SentimentTop10AuthorsWidget from '@/components/widgets/online/SentimentTop10AuthorsWidget'
import SentimentTop10SourcesWidget from '@/components/widgets/online/SentimentTop10SourcesWidget'
import SentimentTop10LanguagesWidget from '@/components/widgets/online/SentimentTop10LanguagesWidget'
import SentimentTop10CountriesWidget from '@/components/widgets/online/SentimentTop10CountriesWidget'
import ContentVolumeTop5SourceWidget from '@/components/widgets/online/ContentVolumeTop5SourceWidget'
import ContentVolumeTop5AuthorsWidget from '@/components/widgets/online/ContentVolumeTop5AuthorsWidget'
import ContentVolumeTop5CountriesWidget from '@/components/widgets/online/ContentVolumeTop5CountriesWidget'
import WidgetSettingsModal from '@/components/project/modals/WidgetSettingsModal'
import InteractiveWidgetModal from '@/components/modals/InteractiveWidgetModal'

export default {
  name: 'WidgetsList',
  components: {
    InteractiveWidgetModal,
    WidgetSettingsModal,
    VolumeWidget,
    SummaryWidget,
    Top10BrandsWidget,
    Top10CountriesWidget,
    Top10LanguagesWidget,
    SentimentForPeriodWidget,
    Top10AuthorsByVolumeWidget,
    SentimentTop10AuthorsWidget,
    SentimentTop10SourcesWidget,
    SentimentTop10LanguagesWidget,
    SentimentTop10CountriesWidget,
    ContentVolumeTop5SourceWidget,
    ContentVolumeTop5AuthorsWidget,
    ContentVolumeTop5CountriesWidget,
  },
  props: {
    currentProject: {type: [Array, Object], required: false},
    selectedWidgets: {type: Array, required: true},
  },
  async created() {
    if (!this.availableWidgets) {
      await this[action.GET_AVAILABLE_WIDGETS](this.currentProject.id)
    }
  },
  computed: {
    ...mapGetters({
      availableWidgets: get.AVAILABLE_WIDGETS,
    }),
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
.widgets {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 30px;

  list-style: none;

  .widgets__item {
    width: calc(50% - 15px);

    .summary-widget__container {
      display: block;
    }
  }

  .grow {
    display: flex;
    width: 100%;
  }
}
</style>
