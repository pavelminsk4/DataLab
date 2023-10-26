<template>
  <Datepicker
    v-model="modelValueProxy"
    :is-24="false"
    :clearable="null"
    :hide-input-icon="true"
    time-picker
    auto-apply
    placeholder="Time"
    menu-class-name="time-picker-menu"
    class="time-picker-wrapper"
  />
</template>

<script>
import Datepicker from '@vuepic/vue-datepicker'
import '@vuepic/vue-datepicker/dist/main.css'

export default {
  name: 'TimePicker',
  components: {Datepicker},
  props: {
    modelValue: {type: Object, default: () => {}},
  },
  computed: {
    modelValueProxy: {
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

<style lang="scss">
.time-picker-wrapper {
  width: 100px;
  height: 40px;

  .dp__input_wrap {
    .dp__input {
      border-radius: 10px;
      border: 1px solid var(--border-color);
    }
  }
}

.time-picker-menu {
  height: 150px;

  border-radius: 10px !important;

  .dp__instance_calendar {
    height: 150px;

    .dp__overlay {
      border-radius: 10px;
      border-bottom: 1px solid var(--border-color);

      .dp__pm_am_button {
        background: var(--primary-color);
      }
    }
  }
}
</style>
