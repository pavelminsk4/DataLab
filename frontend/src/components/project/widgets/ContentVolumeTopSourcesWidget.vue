<template>
  <WidgetsLayout
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    test
  </WidgetsLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import WidgetsLayout from '@/components/layout/WidgetsLayout'

export default {
  name: 'ContentVolumeTopSources',
  components: {WidgetsLayout},
  props: {
    projectId: {
      type: [Number, String],
      required: true,
    },
    chartId: {
      type: String,
      default: 'line-chart',
    },
    datasetIdKey: {
      type: String,
      default: 'label',
    },
    width: {
      type: Number,
      default: 400,
    },
    height: {
      type: Number,
      default: 400,
    },
    cssClasses: {
      default: '',
      type: String,
    },
    styles: {
      type: Object,
      default: () => {},
    },
    plugins: {
      type: Array,
      default: () => [],
    },
  },
  created() {
    this[action.GET_CONTENT_VOLUME_TOP_SOURCES](this.projectId)
  },
  data() {
    return {
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
      },
    }
  },
  computed: {
    ...mapGetters({
      contentVolumeTopSources: get.CONTENT_VOLUME_TOP_SOURCES,
    }),
    chartData() {
      return {
        labels: [
          'January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
        ],
        datasets: [
          {
            label: [1, 2, 3, 4],
            backgroundColor: '#f87979',
            data: [40, 39, 10, 40, 39, 80, 40],
          },
          {
            label: [1, 2, 3, 4],
            backgroundColor: '#f87979',
            data: [40, 39, 10, 40, 39, 80, 40],
          },
        ],
      }
    },
    contentVolumeTopSourcesCollection() {
      let labelsCollection = []

      this.contentVolumeTopSources.forEach((el) => {
        Object.keys(el).forEach((i) =>
          labelsCollection.push({
            name: i,
            dates: el[i],
          })
        )
      })
      return labelsCollection
    },
    labels() {
      return this.contentVolumeTopSourcesCollection.map((el) => el.name)
    },
  },
  methods: {
    ...mapActions([action.GET_CONTENT_VOLUME_TOP_SOURCES]),
  },
}
</script>

<style scoped></style>
