<template>
  <WidgetsLayout
    v-if="contentVolumeTopCountries"
    :title="widgets['content_volume_top_5_countries_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <LineChart :widget-data="contentVolumeTopCountries" class="line-chart" />
  </WidgetsLayout>
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import LineChart from '@/components/project/widgets/charts/LineChart'

export default {
  name: 'ContentVolumeTop5CountriesWidget',
  components: {LineChart, WidgetsLayout},
  props: {
    projectId: {
      type: [Number, String],
      required: true,
    },
    widgets: {
      type: [Array, Object],
      default: () => [],
    },
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
  computed: {
    ...mapGetters({
      contentVolumeTopCountries: get.CONTENT_VOLUME_TOP_COUNTRIES,
    }),
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
