<template>
  <div class="wrapper">
    <div
      v-for="tab in tabs"
      :key="tab"
      :class="['tab', isActiveTab(tab) && 'active']"
      @click="switchTab(tab)"
    >
      <CustomText tag="span" :text="tab" :class="[isSentiment && tab]" />
    </div>
  </div>
</template>

<script>
import CustomText from '@components/CustomText'

export default {
  name: 'WidgetsSwitcher',
  components: {CustomText},
  props: {
    tabs: {type: Array, required: true},
    modelValue: {type: String, required: true},
    isSentiment: {type: Boolean, default: false},
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

  width: 100%;
  height: 45px;

  border-top: 1px solid var(--border-color);
  background-color: var(--background-secondary-color);

  margin-top: -5px;
  border-radius: 0 0 8px 8px;
  padding: 10px 10px;

  .tab {
    display: -webkit-box;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
    overflow: hidden;

    width: 100%;

    text-align: center;
    text-transform: capitalize;

    &:not(:last-child) {
      border-right: 1px solid var(--border-color);
    }
    transition: 0.5s;
  }
  .positive:before,
  .negative:before,
  .neutral:before {
    content: '';
    display: inline-block;
    width: 20px;
    height: 10px;
    margin-right: 5px;
  }

  .positive:before {
    background: var(--positive-primary-color);
  }

  .negative:before {
    background: var(--negative-primary-color);
  }

  .neutral:before {
    background: var(--neutral-primary-color);
  }

  .active {
    color: var(--primary-color);
    text-decoration: underline 2px;
  }
}
</style>
