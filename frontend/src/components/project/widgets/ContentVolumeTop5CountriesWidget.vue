<template>
  <WidgetsLayout
    v-if="contentVolumeTopCountries && isGeneralWidget"
    :title="widgets['content_volume_top_5_countries_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :widget-data="contentVolumeTopCountries"
      :chart-type="chartType"
    />
  </WidgetsLayout>

  <ChartsView
    v-else
    :widget-data="contentVolumeTopCountries"
    :chart-type="chartType"
  />
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/project/widgets/charts/ChartsView'

export default {
  name: 'ContentVolumeTop5CountriesWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    projectId: {
      type: [Number, String],
      required: true,
    },
    widgets: {
      type: [Array, Object],
      default: () => [],
    },
    chartType: {
      type: String,
      required: true,
    },
    isGeneralWidget: {
      type: Boolean,
      default: true,
    },
  },
  computed: {
    ...mapGetters({
      contentVolumeTopCountries: get.CONTENT_VOLUME_TOP_COUNTRIES,
    }),
  },
  created() {
    this[action.GET_CONTENT_VOLUME_TOP_COUNTRIES]({
      projectId: this.projectId,
      value: {
        author_dim_pivot:
          this.widgets['content_volume_top_5_countries_widget']
            .author_dim_pivot || null,
        language_dim_pivot:
          this.widgets['content_volume_top_5_countries_widget']
            .language_dim_pivot || null,
        country_dim_pivot:
          this.widgets['content_volume_top_5_countries_widget']
            .country_dim_pivot || null,
        sentiment_dim_pivot:
          this.widgets['content_volume_top_5_countries_widget']
            .sentiment_dim_pivot || null,
        source_dim_pivot:
          this.widgets['content_volume_top_5_countries_widget']
            .source_dim_pivot || null,
        smpl_freq:
          this.widgets['content_volume_top_5_countries_widget']
            .aggregation_period,
      },
    })
  },
  methods: {
    ...mapActions([action.GET_CONTENT_VOLUME_TOP_COUNTRIES]),
  },
}
</script>

<style scoped>
.line-chart {
  overflow: hidden;
  height: 100%;
  width: 100%;
}
</style>
