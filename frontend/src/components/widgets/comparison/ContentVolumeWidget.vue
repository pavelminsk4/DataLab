<template>
  <ContentVolumeWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :content-volume-widget-data="widgetData"
  />
</template>

<script>
import ContentVolumeWidget from '@/components/widgets/ContentVolumeWidget'

export default {
  name: 'ComparisonContentVolumeWidget',
  components: {ContentVolumeWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
    widgetData() {
      const formatedWidgetData = []
      this.widgetDetails.widgetData.map((project) => {
        const value = {}
        value[project.project] = project.data.map((el) => {
          return {
            post_count: el.created_count,
          }
        })
        formatedWidgetData.push(value)
      })
      return formatedWidgetData
    },
  },
}
</script>
