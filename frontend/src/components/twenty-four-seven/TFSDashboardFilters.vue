<template>
  <StatusesChips @show-status-cards="showStatusCards" />

  <div class="sorting">
    <BaseDropdown
      v-for="(item, index) in filterOptions"
      :key="item.name + index"
      :title="item.title"
      :name="item.name"
      :selected-value="item.selectedValue"
    >
      <div
        v-for="(listOption, index) in item.sortingList"
        :key="listOption.label + index"
        @click="$emit(item.actionName, listOption)"
      >
        {{ listOption.label }}
      </div>
    </BaseDropdown>
  </div>
</template>

<script>
import BaseDropdown from '@/components/BaseDropdown'
import StatusesChips from '@/components/twenty-four-seven/StatusesChips'

export default {
  name: 'TFSDashboardFilters',
  components: {
    BaseDropdown,
    StatusesChips,
  },
  props: {
    selectedIntervalValue: {type: String, reqired: true},
    selectedSortValue: {type: String, reqired: true},
  },
  emits: ['show-status-cards', 'sort-selection', 'refresh-results'],
  computed: {
    filterOptions() {
      return [
        {
          title: 'Sort by',
          name: 'sort-posts',
          actionName: 'sort-selection',
          selectedValue: this.selectedSortValue,
          sortingList: [
            {label: 'Latest', value: 'asc_date'},
            {label: 'Earliest', value: 'desc_date'},
            {label: 'PR ASC', value: 'asc_reach'},
            {label: 'PR DESC', value: 'desc_reach'},
          ],
        },
        {
          title: 'Refresh',
          name: 'refresh',
          actionName: 'refresh-results',
          selectedValue: this.selectedIntervalValue,
          sortingList: [
            {label: 'Refresh every 5 sec', value: 5000},
            {label: 'Refresh every 15 sec', value: 15000},
            {label: 'Refresh every 30 sec', value: 30000},
            {label: 'No automatic refresh', value: 0},
          ],
        },
      ]
    },
  },
  methods: {
    showStatusCards(status) {
      this.$emit('show-status-cards', status)
    },
  },
}
</script>

<style lang="scss">
.sorting {
  display: flex;
  gap: 24px;
}
</style>
