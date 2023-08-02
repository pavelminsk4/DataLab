<template>
  <GenderColumnsStackedBarsWidget
    v-if="widgetDetails.widgetData"
    :widget-details="widgetDetails"
  />
</template>

<script>
import GenderColumnsStackedBarsWidget from '@/components/widgets/GenderColumnsStackedBarsWidget'

export default {
  name: 'TopGenderByLocation',
  components: {GenderColumnsStackedBarsWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  provide: {
    barHeight: '32px',
  },
}
</script>
