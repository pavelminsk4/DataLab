<template>
  <BaseFlashMessage v-bind="$attrs" class="error-flash-message">
    <slot></slot>
  </BaseFlashMessage>
</template>

<script>
import BaseFlashMessage from '@components/flash-messages/BaseFlashMessage'

export default {
  name: 'SuccessFlashMessage',
  components: {BaseFlashMessage},
}
</script>

<style lang="scss" scoped>
.error-flash-message {
  border-color: var(--positive-primary-color);
  background-color: var(--positive-secondary-color);
}
</style>
