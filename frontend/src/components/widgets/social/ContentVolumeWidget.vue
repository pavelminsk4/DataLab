<template>
  <component
    :is="widgetWrapper"
    :title="widgets.content_volume.title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :labels="labels"
      :chart-values="chartValues"
      :chart-type="chartType"
      :is-display-legend="false"
    />
  </component>
</template>

<script>
import {mapGetters, createNamespacedHelpers} from 'vuex'
import {get} from '@store/constants'
import {action} from '@store/constants'
import {defaultDate} from '@/lib/utilities'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/charts/ChartsView'

const {mapActions, mapGetters: mapGettersSocial} =
  createNamespacedHelpers('social/widgets')

export default {
  name: 'SocialContentVolumeWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    isWidget: {type: Boolean, default: true},
    volume: {type: [Array, Object], default: () => []},
    projectId: {type: [String, Number], required: true},
    widgetId: {type: Number, required: true},
    chartType: {type: String, required: true},
    isGeneralWidget: {type: Boolean, default: true},
  },
  computed: {
    ...mapGettersSocial({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    ...mapGetters({
      widgets: get.AVAILABLE_WIDGETS,
    }),
    widgetWrapper() {
      return this.isWidget ? 'WidgetsLayout' : 'div'
    },
    contentVolumeWidgetData() {
      return this.socialWidgets.contentVolume
    },
    labels() {
      return this.contentVolumeWidgetData.map((el) =>
        defaultDate(el.creation_date)
      )
    },
    chartValues() {
      return [
        {
          color: '#516BEE',
          data: this.contentVolumeWidgetData.map((el) => el.created_count),
        },
      ]
    },
  },
  created() {
    if (!this.contentVolumeWidgetData.length) {
      this[action.GET_CONTENT_VOLUME_WIDGET]({
        projectId: this.projectId,
        value: {
          author_dim_pivot:
            this.widgets.content_volume.author_dim_pivot || null,
          language_dim_pivot:
            this.widgets.content_volume.language_dim_pivot || null,
          country_dim_pivot:
            this.widgets.content_volume.country_dim_pivot || null,
          sentiment_dim_pivot:
            this.widgets.content_volume.sentiment_dim_pivot || null,
          source_dim_pivot:
            this.widgets.content_volume.source_dim_pivot || null,
          smpl_freq: this.widgets.content_volume.aggregation_period,
        },
        widgetId: this.widgetId,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_CONTENT_VOLUME_WIDGET]),
  },
}
</script>
