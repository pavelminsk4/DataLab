<template>
  <div class="search-result-wrapper">
    <div class="filters">Filters</div>
    <div v-if="searchData.length" class="search-result-cards">
      <div
        v-for="(item, index) in searchData"
        :key="'result' + index"
        class="search-result-card"
      >
        {{ item.entry_title }}
      </div>
    </div>
    <div v-else>No results.</div>
  </div>
</template>

<script>
import {mapState} from 'vuex'

export default {
  name: 'SearchResults',
  computed: {
    ...mapState(['searchData']),
  },
}
</script>

<style scoped>
.search-result-wrapper {
  display: flex;
  flex-direction: column;
  align-items: flex-start;

  width: 630px;
  margin-left: 108px;

  color: var(--primary-text-color);
}

.filters {
  margin-bottom: 25px;
}

.search-result-card {
  margin-bottom: 10px;
  padding: 12px 21px 17px 20px;

  background: var(--secondary-bg-color);
  border-radius: 10px;
  border: 1px solid var(--input-border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
}
</style>
