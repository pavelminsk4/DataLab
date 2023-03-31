<template>
  <div class="textarea-wrapper">
    <label v-if="label" :for="label" class="label">{{ label }}</label>

    <textarea
      v-model="value"
      :placeholder="placeholder"
      :id="label"
      class="scroll"
    />
  </div>
</template>

<script>
export default {
  name: 'BaseTextarea',
  props: {
    modelValue: {type: String, default: ''},
    placeholder: {type: String, default: ''},
    label: {type: String, default: ''},
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
.textarea-wrapper {
  display: flex;
  flex-direction: column;

  textarea {
    width: 100%;
    height: 80px;
    padding: 10px 12px;

    background-color: var(--background-secondary-color);
    border: var(--border-primary);
    border-radius: var(--border-radius);

    resize: none;
    outline: none;

    color: var(--typography-primary-color);
  }

  textarea::placeholder {
    color: var(--typography-secondary-color);
  }

  .label {
    margin-bottom: 4px;

    color: var(--typography-title-color);
  }
}
</style>
