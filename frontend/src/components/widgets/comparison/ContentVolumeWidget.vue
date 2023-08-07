<template>
  <ContentVolumeWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :content-volume-widget-data="widgetData"
    :colors="colors"
  />
</template>

<script>
import ContentVolumeWidget from '@/components/widgets/ContentVolumeWidget'
import {COMPARISON_COLORS} from '@lib/constants'

export default {
  name: 'ComparisonContentVolumeWidget',
  components: {ContentVolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    widgetData() {
      const formattedWidgetData = []
      this.widgetDetails.widgetData.map((project) => {
        const value = {}
        value[project.project] = project.data.map((item) => {
          return {
            date: item.date,
            post_count: item.created_count,
          }
        })
        formattedWidgetData.push(value)
      })

      return formattedWidgetData
    },
  },
  created() {
    this.colors = COMPARISON_COLORS
  },
}
</script>
