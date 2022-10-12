<template>
  <div class="custom-action-row">
    <button class="select-button" @click="$emit('selectDate')">
      Select Date
    </button>
  </div>
</template>

<script>
import {defineComponent} from 'vue'

export default defineComponent({
  emits: ['selectDate', 'closePicker'],
  props: {
    selectText: {type: String, default: 'Select'},
    cancelText: {type: String, default: 'Cancel'},
    internalModelValue: {type: [Date, Array], default: null},
    range: {type: Boolean, default: true},
    previewFormat: {
      type: [String, Function],
      default: () => '',
    },
    monthPicker: {type: Boolean, default: false},
    timePicker: {type: Boolean, default: false},
  },
})
</script>

<style lang="scss">
.custom-action-row {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.current-selection {
  margin: 10px 0 0 0;
}

.select-button {
  display: block;
  background: transparent;
  border: 1px solid var(--dp-success-color);
  color: var(--dp-success-color);
  border-radius: 4px;
  padding: 5px;
  margin: 10px;
  cursor: pointer;
}
</style>
