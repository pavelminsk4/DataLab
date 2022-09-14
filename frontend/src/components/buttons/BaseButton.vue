<template>
  <button
    :class="[
      'base-button',
      isNotBackground && 'not-background',
      isDisabled && 'disabled',
    ]"
  >
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: 'BaseButton',
  props: {
    isNotBackground: {
      type: Boolean,
      default: false,
    },
    isDisabled: {
      type: Boolean,
      default: false,
    },
  },
}
</script>

<style>
.base-button {
  cursor: pointer;
  outline: none;

  height: 40px;

  border: none;
  border-radius: 8px;

  color: var(--primary-text-color);
  background: var(--primary-button-color);
}

.not-background {
  background: var(--secondary-button-color);
}

.disabled {
  opacity: 0.5;
  cursor: not-allowed;

  color: var(--primary-text-color);
  background: var(--disabled-color);
}
</style>
