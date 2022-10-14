<template>
  <label class="container container-header">
    <input type="checkbox" :id="id" v-model="checked" @change="click" />
    <span class="checkmark">
      <CheckIcon class="checkmark-icon" />
    </span>
    <div class="title">
      <slot></slot>
    </div>
  </label>
</template>

<script>
import CheckIcon from '@/components/icons/CheckIcon'
export default {
  name: 'BaseCheckbox',
  components: {CheckIcon},
  props: {
    modelValue: {type: Boolean, default: false},
    label: {type: String},
    id: {type: Number},
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
  margin-bottom: 10px;

  cursor: pointer;

  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.container input {
  position: absolute;

  height: 0;
  width: 0;

  opacity: 0;
  cursor: pointer;
}

.checkmark {
  top: 0;
  left: 0;

  display: flex;
  align-items: center;
  justify-content: center;

  height: 20px;
  width: 20px;

  border: 1px solid var(--secondary-text-color);
  border-radius: 4px;
  background-color: var(--input-border-color);
}

.title {
  margin-left: 10px;

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--primary-text-color);
}

.container:hover input ~ .checkmark {
  background-color: var(--secondary-bg-color);
}

.container input:checked ~ .checkmark {
  border: none;
  background-color: var(--primary-button-color);
}

.container input ~ .checkmark > .checkmark-icon {
  display: none;
}

.container input:checked ~ .checkmark > .checkmark-icon {
  display: block;
}

.container input:checked ~ .checkmark:after {
  display: block;
}
</style>
