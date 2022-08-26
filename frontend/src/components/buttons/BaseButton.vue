<template>
  <button v-bind="$attrs" :disabled="disabled" class="base-button">
      <slot></slot>
  </button>
</template>

<script>
export default {
  name: 'BaseButton',
  props: {
    disabled: { type: Boolean, default: false }
  }
}
</script>

<style>
 .base-button {
   outline: none;
   cursor: pointer;

   height: 40px;

   border: none;
   border-radius: 8px;

   color: var(--primary-text-color);
   background: var(--primary-button-color);
 }
</style>
