<template>
  <label v-if="label" :for="label">
    <CustomText :text="label" class="label" />
    <div :class="['input-wrapper', hasError && 'error']">
      <SearchIcon v-if="isSearch" class="search-icon" />
      <input
        v-bind="$attrs"
        :type="inputType"
        :id="label"
        :dir="customDir || currentDir"
        :value="modelValue"
        :class="['input', isSearch && 'input-search']"
        :placeholder="currentPlaceholder"
        :autocomplete="autocomplete"
        @input="debounceInput"
      />

      <div v-if="hasError" class="error-container">
        <CustomText :text="errorMessage" />
        <ErrorIcon class="error-icon" />
      </div>

      <slot></slot>
    </div>
  </label>
</template>

<script>
import debounce from 'lodash/debounce'
import translate from '@lib/mixins/translate.js'

import CustomText from '@components/CustomText'
import SearchIcon from '@components/icons/SearchIcon'
import ErrorIcon from '@components/icons/ErrorIcon'

export default {
  name: 'BaseInput',
  mixins: [translate],
  props: {
    modelValue: {type: [String, Number], required: true},
    inputType: {type: String, default: 'text'},
    isSearch: {type: Boolean, default: false},
    placeholder: {type: String, default: 'Enter text'},
    hasError: {type: Boolean, default: false},
    errorMessage: {type: String, default: 'Error'},
    autocomplete: {type: String, default: ''},
    label: {type: String, default: ''},
    dir: {type: String, default: 'ltr'},
    customDir: {type: String, default: ''},
  },
  components: {
    ErrorIcon,
    SearchIcon,
    CustomText,
  },
  methods: {
    debounceInput: debounce(function (e) {
      this.$emit('update:modelValue', e.target.value)
    }, 100),
  },
}
</script>

<style lang="scss" scoped>
.label {
  margin-bottom: 4px;

  color: var(--typography-title-color);
}

.input-wrapper {
  position: relative;

  display: flex;
  align-items: center;

  height: 40px;
  padding: 10px 12px;

  border: var(--border-primary);
  border-radius: var(--border-radius);
  background-color: var(--background-secondary-color);
}

.input {
  width: 100%;

  border: none;
  border-radius: var(--border-radius);
  background-color: var(--background-secondary-color);
  outline: none;

  color: var(--typography-primary-color);
}

.input[type='number'] {
  -moz-appearance: textfield;

  &::-webkit-inner-spin-button,
  &::-webkit-outer-spin-button {
    -webkit-appearance: none;
    margin: 0;
  }
}

.input::placeholder {
  color: var(--typography-secondary-color);
}

.input-search {
  padding-left: 28px;
}

.search-icon {
  position: absolute;
  left: 12px;

  width: 20px;
  height: 20px;
}

.error {
  border: 1px solid var(--negative-status);
  border-radius: 10px;
}

.error-container {
  position: absolute;
  top: calc(100% + 5px);
  right: 0;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 10px;

  width: 262px;

  white-space: nowrap;
  pointer-events: none;

  color: var(--negative-status);

  .error-icon {
    flex-shrink: 0;
  }

  font-size: 12px;
}
</style>
