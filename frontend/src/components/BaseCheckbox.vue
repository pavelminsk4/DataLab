<template>
  <label class="container container-header">
    <input
      type="checkbox"
      :id="id"
      v-model="checked"
      @change="click"
      :checked="selected"
    />
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
    modelValue: {type: Boolean, default: false},
    selected: {type: Boolean, default: false},
    label: {type: String},
    id: {type: [Number, String]},
    hasIcon: {type: Boolean, default: true},
  },
  emits: ['change'],
  data() {
    return {
      checked: this.modelValue,
    }
  },
  methods: {
    click() {
      this.$emit('change', {id: this.id, checked: this.checked})
    },
  },
}
</script>

<style scoped>
.container {
  position: relative;

  display: flex;

  font-size: 22px;

  cursor: pointer;

  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.container input {
  position: absolute;

  flex-shrink: 0;

  height: 0;
  width: 0;

  opacity: 0;
  cursor: pointer;
}

.checkmark {
  top: 0;
  left: 0;

  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;

  height: 20px;
  width: 20px;

  border: 1px solid var(--typography-secondary-color);
  border-radius: 4px;
  background-color: var(--background-secondary-color);
}

.container:hover input ~ .checkmark {
  border-color: var(--typography-title-color);
}

.container input:checked ~ .checkmark {
  border-color: var(--border-active-color);
  background-color: var(--background-secondary-color);
}

.container input ~ .checkmark > .checkmark-icon {
  display: none;
}

.container input:checked ~ .checkmark > .checkmark-icon {
  display: block;
  color: var(--primary-color);
}

.container input:checked ~ .checkmark:after {
  display: block;
  color: var(--primary-color);
}
</style>
