<template>
  <label class="radio" :class="{selected: Object.is(checked, value)}">
    <input
      class="input-radio"
      type="radio"
      :value="label"
      :name="name"
      v-model="radioButtonValue"
    />
    <slot name="default" />
    <slot name="description" />
  </label>
</template>

<script>
export default {
  props: {
    checked: {type: [String, Number, Object], default: ''},
    label: {type: String, default: undefined},
    value: {type: [String, Number, Object], required: true},
    name: {type: String, required: false},
  },
  model: {
    prop: 'checked',
    event: 'change',
  },
  computed: {
    radioButtonValue: {
      get() {
        return this.value
      },

      set() {
        this.$emit('change', this.label)
      },
    },
  },
}
</script>

<style scoped>
.radio {
  display: block;

  padding: 12px 20px 25px 20px;

  border-radius: 15px;
  border: 1px solid var(--input-border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
  background: var(--secondary-bg-color);

  color: var(--primary-text-color);

  cursor: pointer;
}

.input-radio {
  width: 0;
}

.selected {
  background: var(--primary-button-color);
}
</style>
