<template>
  <div :class="['input-wrapper', isSettings && 'settings-input']">
    <SearchIcon v-if="isSearch" class="icon" />
    <input
      v-bind="$attrs"
      :value="modelValue"
      :class="['input', isSearch && 'input-search']"
      :placeholder="placeholder"
      @input="handleInput"
    />

    <slot></slot>
  </div>
</template>

<script>
import SearchIcon from '@components/icons/SearchIcon'

export default {
  name: 'BaseInput',
  props: {
    modelValue: {
      type: String,
      required: true,
    },
    isSearch: {
      type: Boolean,
      default: false,
    },
    isSettings: {
      type: Boolean,
      default: false,
    },
    placeholder: {
      type: String,
      default: 'Enter text',
    },
  },
  components: {
    SearchIcon,
  },
  methods: {
    handleInput(e) {
      this.$emit('update:modelValue', e.target.value)
    },
  },
}
</script>

<style lang="scss" scoped>
.input-wrapper {
  position: relative;

  display: flex;
  align-items: center;

  height: 40px;
  width: 262px;

  border: 1px solid var(--input-border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
  border-radius: 10px;

  background-color: var(--secondary-bg-color);
}

.input {
  width: 100%;
  padding-left: 16px;

  border: none;
  border-radius: 10px;

  outline: none;
  color: var(--primary-text-color);
  background-color: var(--secondary-bg-color);
}

.input::placeholder {
  color: var(--secondary-text-color);
}

.input-search {
  padding-left: 32px;
}

.settings-input {
  width: 100%;

  background: #34353b;
  border: 1px solid #404046;
  border-radius: 10px;

  input {
    background: #34353b;
  }
}

.icon {
  position: absolute;
  left: 10px;

  width: 16px;
  height: 16px;
}
</style>
