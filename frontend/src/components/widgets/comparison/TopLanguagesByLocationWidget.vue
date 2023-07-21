<template>
  <ColumnsStackedBarsWidget
    v-if="widgetDetails.widgetData"
    :widget-details="widgetDetails"
  />
</template>

<script>
import ColumnsStackedBarsWidget from '@/components/widgets/ColumnsStackedBarsWidget'

export default {
  name: 'ComparisonTopLanguagesByLocationWidget',
  components: {ColumnsStackedBarsWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  provide: {
    barHeight: '32px',
  },
}
</script>
