<template>
  <span class="search-results-count">{{ totalResults }}</span>
  <CustomText text="results" class="search-results-count" />
</template>

<script>
import CustomText from '@components/CustomText'

export default {
  name: 'TotalResults',
  components: {
    CustomText,
  },
  props: {
    totalResults: {type: Number, required: true},
  },
}
</script>

<style scoped>
.search-results-count {
  font-weight: 600;
  font-size: 14px;
  line-height: 20px;
  color: var(--typography-secondary-color);
}
</style>
