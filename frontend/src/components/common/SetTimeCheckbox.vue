<template>
  <div :class="['set-time-checkbox', isChecked && 'active']">
    <div class="set-time">
      <BaseCheckbox2 v-model="isChecked" class="checkbox" />
      <h5 class="title">{{ title }}</h5>
    </div>
    <div class="set-time">
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
    modelValue: {type: [Boolean, Array], default: false},
    title: {type: String, required: true},
  },
  computed: {
    isChecked: {
      get() {
        return this.modelValue
      },
      set(val) {
        this.$emit('update:modelValue', val)
      },
    },
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

.active {
  border-color: var(--border-active-color);
  background-color: var(--primary-active-color);
}

.set-time {
  display: flex;
  align-items: center;

  &:not(:last-child) {
    margin-bottom: 8px;
  }
}

.checkbox {
  --checkbox-width: 24px;

  margin-right: 12px;
}
</style>
