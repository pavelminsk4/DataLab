<template>
  <div class="wrapper">
    <div
      v-for="tab in tabs"
      :key="tab"
      :class="['tab', isActiveTab(tab) && 'active']"
      @click="switchTab(tab)"
    >
      {{ tab }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'WidgetsSwitcher',
  props: {
    tabs: {type: Array, required: true},
    modelValue: {type: String, required: true},
  },
  methods: {
    isActiveTab(tabName) {
      return tabName === this.modelValue
    },
    switchTab(tab) {
      this.$emit('update:modelValue', tab)
    },
  },
}
</script>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  justify-content: space-around;
  align-items: center;

  position: relative;

  height: 45px;

  border-top: 1px solid var(--border-color);
  background-color: var(--background-secondary-color);

  margin-top: -5px;
  border-radius: 0 0 8px 8px;

  .tab {
    display: -webkit-box;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
    overflow: hidden;

    width: 100%;

    text-align: center;

    &:not(:last-child) {
      border-right: 1px solid var(--border-color);
    }
  }

  .active {
    color: var(--primary-color);
    text-decoration: underline;
  }
}
</style>
