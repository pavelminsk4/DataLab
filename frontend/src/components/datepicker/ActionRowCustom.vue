<template>
  <div class="custom-action-row">
    <BaseButton class="button" @click="$emit('selectDate')">Apply</BaseButton>
  </div>
</template>

<script>
import {defineComponent} from 'vue'
import BaseButton from '@/components/buttons/BaseButton'

export default defineComponent({
  components: {BaseButton},
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

<style lang="scss" scoped>
.custom-action-row {
  position: absolute;
  right: 40px;
  bottom: 35px;

  display: flex;
  align-items: center;
  justify-content: center;

  margin-top: 25px;

  .button {
    width: 235px;
  }
}
</style>
