<template>
  <div class="chips-container">
    <div v-for="(item, index) in items" :key="item + index" class="chip">
      {{ item }}
      <CrossIcon class="icon" @click="removeItem(item)" />
    </div>
    <CustomText text="Clear All" class="active-button" @click="clearAll" />
  </div>
</template>

<script>
import CustomText from '@/components/CustomText'
import CrossIcon from '@/components/icons/CrossIcon'

export default {
  name: 'FilterChips',
  components: {CrossIcon, CustomText},
  props: {
    items: {
      type: Array,
      default: () => [],
    },
  },
  methods: {
    removeItem(item) {
      this.$emit('remove-item', item)
    },
    clearAll() {
      this.$emit('clear-all')
    },
  },
}
</script>

<style lang="scss" scoped>
.chips-container {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;

  .chip {
    display: flex;
    align-items: center;
    gap: 4px;

    padding: 6px 12px;

    background: var(--button-secondary-hover-color);
    border: var(--border-primary);
    border-radius: 12px;

    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 20px;
    color: var(--typography-title-color);

    .icon {
      cursor: pointer;

      width: 16px;
      height: 16px;
    }
  }

  .active-button {
    margin-left: 8px;

    cursor: pointer;

    font-style: normal;
    font-weight: 500;
    font-size: 14px;
    line-height: 20px;
    color: var(--primary-color);
  }
}
</style>
