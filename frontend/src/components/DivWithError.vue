<template>
  <div :class="['div', hasError && 'div-with-error']">
    <div v-if="hasError" class="error-container">
      {{ errorMessage }}
      <ErrorIcon class="error-icon" />
    </div>
    <slot></slot>
  </div>
</template>

<script>
import ErrorIcon from '@/components/icons/ErrorIcon'

export default {
  name: 'DivWithError',
  components: {ErrorIcon},
  props: {
    hasError: {
      type: Boolean,
      default: false,
    },
    errorMessage: {
      type: String,
      default: 'Error',
    },
  },
}
</script>

<style lang="scss" scoped>
.div {
  border: 1px solid transparent;
}
.div-with-error {
  --error-top: calc(100% + 5px);
  position: relative;

  border: 1px solid var(--negative-status) !important;
}

.error-container {
  position: absolute;
  top: var(--error-top);
  right: 10px;

  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;

  white-space: nowrap;

  color: var(--error-primary-color);

  font-size: 12px;
}

.error-icon {
  color: var(--error-primary-color);
}
</style>
