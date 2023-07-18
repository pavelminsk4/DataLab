<template>
  <div :style="`border-top: 3px solid ${statusColor};`" class="column-header">
    <span>{{ status }}</span>
    <div class="results">{{ numberOfResults }}</div>

    <div class="pagination-wrapper">
      <ArrowheadIcon
        class="left-arrow arrow"
        direction="left"
        @click="$emit('decrease-arrow')"
      />
      <BaseSelect
        modelValue="value"
        v-bind="$attrs"
        :selectName="status"
        :options="numberOfPages"
        class="select"
        @update:modelValue="updatePage"
      />
      <ArrowheadIcon
        class="right-arrow arrow"
        direction="right"
        @click="$emit('increase-arrow')"
      />
    </div>
  </div>
</template>

<script>
import BaseSelect from '@/components/BaseSelect2'
import ArrowheadIcon from '@/components/icons/ArrowheadIcon'

export default {
  name: 'TFSColumnHeader',
  components: {BaseSelect, ArrowheadIcon},
  props: {
    value: {type: [Number, String], required: true},
    status: {type: String, required: true},
    statusColor: {type: String, required: true},
    numberOfResults: {type: Number, required: false},
    numberOfPages: {type: Array, required: true},
  },
  data() {
    return {
      newPageNumber: null,
    }
  },
  methods: {
    updatePage(newPage) {
      this.$emit('update-page', newPage, this.status)
    },
  },
}
</script>

<style lang="scss" scoped>
.column-header {
  display: flex;
  align-items: center;
  gap: 4px;

  width: 92%;
  padding: 12px 20px;
  margin-bottom: 24px;

  border-radius: 8px;
  background-color: var(--background-secondary-color);

  font-style: normal;
  font-weight: 500;
  font-size: 16px;
  line-height: 20px;
  color: var(--typography-title-color);

  .results {
    padding: 2px 10px;

    border-radius: 14px;
    background-color: var(--icon-primary-color);

    text-align: center;
    font-size: 14px;
    color: var(--button-text-color);
  }

  .pagination-wrapper {
    display: flex;
    align-items: center;

    margin-left: auto;

    .arrow {
      width: 16px;
      height: 8px;

      cursor: pointer;
    }

    .left-arrow {
      margin-right: 5px;

      transform: rotate(90deg);
    }

    .right-arrow {
      margin-left: 5px;

      transform: rotate(-90deg);
    }

    .select {
      width: 68px;
    }
  }
}
</style>

<style lang="scss">
.pagination-wrapper {
  .select__button {
    margin-bottom: 0;
  }
}
</style>
