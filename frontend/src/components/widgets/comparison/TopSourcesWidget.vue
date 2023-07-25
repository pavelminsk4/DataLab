<template>
  <ComparisonTopWidget :widget-details="widgetDetails" :fields="fields" />
</template>

<script>
import ComparisonTopWidget from '@/components/widgets/comparison/ComparisonTopWidget'

export default {
  name: 'ComparisonTopLanguagesWidget',
  components: {ComparisonTopWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  created() {
    this.fields = {
      label: 'feedlink__source1',
      value: 'brand_count',
      undefinedLabel: 'No source',
    }
  },
}
</script>
