<template>
  <div class="textarea-wrapper">
    <div class="label-wrapper">
      <label v-if="label" :for="label" class="label">{{ label }}</label>
      <div v-if="hasError" class="error-message">
        {{ errorMessage }} <ErrorIcon class="icon" />
      </div>
    </div>

    <textarea
      v-model="value"
      :placeholder="placeholder"
      :id="label"
      :dir="dir"
      :class="['scroll', hasError && 'error']"
    />
  </div>
</template>

<script>
import ErrorIcon from '@components/icons/ErrorIcon'

export default {
  name: 'BaseTextarea',
  components: {ErrorIcon},
  props: {
    modelValue: {type: String, default: ''},
    placeholder: {type: String, default: ''},
    dir: {type: String, default: 'ltr'},
    label: {type: String, default: ''},
    hasError: {type: Boolean, default: false},
    errorMessage: {type: String, default: ''},
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

  .label-wrapper {
    display: flex;
    justify-content: space-between;

    .error-message {
      display: flex;
      align-items: center;
      gap: 5px;

      font-size: 12px;
      color: var(--error-primary-color);

      .icon {
        color: var(--error-primary-color);
      }
    }
  }

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

  .error {
    border-color: var(--error-primary-color);
  }

  .label {
    margin-bottom: 4px;

    color: var(--typography-title-color);
  }
}
</style>
