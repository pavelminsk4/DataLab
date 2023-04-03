<template>
  <div class="set-time-checkbox">
    <h5 class="title">{{ title }}</h5>
    <div class="set-time">
      <BaseCheckbox2 class="checkbox" />
      <slot></slot>
    </div>
  </div>
</template>

<script>
import BaseCheckbox2 from '@/components/BaseCheckbox2'

export default {
  name: 'SetTimeCheckbox',
  components: {BaseCheckbox2},
  props: {
    title: {type: String, required: true},
  },
}
</script>

<style lang="scss" scoped>
.set-time-checkbox {
  display: flex;
  flex-direction: column;

  padding: 12px 12px 8px;

  border: var(--border-primary);
  border-radius: 10px;

  .title {
    font-weight: 600;
  }
}

.set-time {
  display: flex;

  span {
    margin-right: 5px;
  }
}

.checkbox {
  margin-right: 12px;
}
</style>
