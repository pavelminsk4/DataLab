<template>
  <label class="checkbox-container">
    <input v-model="isChecked" type="checkbox" :id="id" :value="id" />
    <span v-if="hasIcon" class="checkmark">
      <CheckIcon class="checkmark-icon" />
    </span>
    <slot></slot>
  </label>
</template>

<script>
import CheckIcon from '@/components/icons/CheckIcon'
export default {
  name: 'BaseCheckbox',
  components: {CheckIcon},
  props: {
    modelValue: {type: [Boolean, Array], default: false},
    selected: {type: Boolean, default: false},
    label: {type: String},
    id: {type: [Number, String], default: 'checkbox'},
    hasIcon: {type: Boolean, default: true},
  },
  emits: ['update:modelValue'],
  computed: {
    isChecked: {
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
.checkbox-container {
  position: relative;

  display: flex;

  height: 20px;
  width: 20px;

  font-size: 22px;

  cursor: pointer;

  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;

  &:hover input ~ .checkmark {
    border-color: var(--typography-title-color);
  }

  input {
    position: absolute;

    height: 0;
    width: 0;

    opacity: 0;
    cursor: pointer;
  }

  input:checked ~ .checkmark {
    border-color: var(--border-active-color);
    background-color: var(--background-secondary-color);
  }

  input ~ .checkmark > .checkmark-icon {
    display: none;
  }

  input:checked ~ .checkmark > .checkmark-icon {
    display: block;
    color: var(--primary-color);
  }

  input:checked ~ .checkmark:after {
    display: block;
    color: var(--primary-color);
  }
}

.checkmark {
  top: 0;
  left: 0;

  display: flex;
  align-items: center;
  justify-content: center;

  height: 100%;
  width: 100%;

  border: 1px solid var(--typography-secondary-color);
  border-radius: 4px;
  background-color: var(--background-secondary-color);
}
</style>
