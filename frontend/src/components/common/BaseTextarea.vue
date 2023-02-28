<template>
  <textarea
    v-model="value"
    :placeholder="placeholder"
    class="textarea scroll"
  />
</template>

<script>
export default {
  name: 'BaseTextarea',
  props: {
    modelValue: {
      type: String,
      default: '',
    },
    placeholder: {
      type: String,
      default: '',
    },
  },
  computed: {
    value: {
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
.textarea {
  width: 100%;
  height: 80px;
  padding: 10px 12px;

  background-color: var(--background-secondary-color);
  border: var(--border-primary);
  border-radius: var(--border-radius);

  resize: none;

  color: var(--typography-primary-color);
}

.textarea::placeholder {
  color: var(--typography-secondary-color);
}
</style>
