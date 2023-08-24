<template>
  <div class="custom-action-row">
    <BaseButton
      :is-disabled="internalModelValue.length <= 1"
      class="button"
      @click="applyChanges"
    >
      <CustomText tag="span" text="Apply" />
    </BaseButton>
  </div>
</template>

<script>
import {mapActions} from 'vuex'
import {defineComponent} from 'vue'
import {action} from '@store/constants'

import CustomText from '@/components/CustomText'
import BaseButton from '@/components/common/BaseButton'

export default defineComponent({
  components: {BaseButton, CustomText},
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
  methods: {
    ...mapActions([action.REFRESH_DISPLAY_CALENDAR]),
    applyChanges() {
      this.$emit('selectDate')
      this[action.REFRESH_DISPLAY_CALENDAR](false)
    },
  },
})
</script>

<style lang="scss" scoped>
.custom-action-row {
  position: absolute;
  right: 30px;
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
