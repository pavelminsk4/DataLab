<template>
  <label class="base-radio-container">
    <input
      type="radio"
      :id="id"
      :value="value"
      :checked="modelValue === value"
      @input="$emit('update:modelValue', $event.target.value)"
      :name="id"
    />
    <slot></slot>
    {{ label }}
    <span class="checkmark"></span>
  </label>
</template>

<script>
export default {
  name: 'BaseRadio',
  props: ['modelValue', 'label', 'value', 'id'],
}
</script>

<style lang="scss" scoped>
.base-radio-container {
  position: relative;

  display: block;
  margin: auto;

  padding-left: 30px;

  cursor: pointer;

  input {
    opacity: 0;
    cursor: pointer;

    &:checked ~ .checkmark {
      border: 1px solid var(--border-active-color);
    }

    &:checked ~ .checkmark:after {
      display: block;
    }
  }

  .checkmark {
    position: absolute;
    top: 0;
    left: 0;

    height: 20px;
    width: 20px;

    background-color: transparent;
    border-radius: 50%;
    border: 1px solid var(--typography-secondary-color);

    &:after {
      content: '';
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);

      display: none;

      width: 8px;
      height: 8px;

      border-radius: 50%;
      background: var(--primary-color);
    }
  }

  &:hover input ~ .checkmark {
    border: 1px solid var(--border-active-color);
    background-color: var(--background-secondary-color);
  }
}
</style>
