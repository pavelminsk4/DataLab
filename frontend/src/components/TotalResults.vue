<template>
  <div class="search-results-count">{{ totalResults }} results</div>
</template>

<script>
export default {
  name: 'TotalResults',
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
