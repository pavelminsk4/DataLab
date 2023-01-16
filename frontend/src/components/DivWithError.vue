<template>
  <div :class="hasError && 'div-with-error'">
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
.div-with-error {
  position: relative;

  border: 1px solid var(--negative-status) !important;
}

.error-container {
  position: absolute;
  top: 10px;
  right: 10px;

  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;

  white-space: nowrap;

  color: var(--negative-status);

  font-size: 12px;
}
</style>
