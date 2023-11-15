<template>
  <Datepicker
    v-model="modelValueProxy"
    :close-on-auto-apply="true"
    :format="formatDate"
    :is-24="false"
    :clearable="null"
    placeholder="Select date"
    auto-apply
    menu-class-name="date-picker-menu"
    class="date-picker-wrapper"
  >
    <template #input-icon>
      <CalendarIcon class="input-slot-image" />
    </template>
  </Datepicker>
</template>

<script>
import moment from 'moment'
import Datepicker from '@vuepic/vue-datepicker'

import CalendarIcon from '@components/icons/CalendarIcon'

export default {
  name: 'DatePicker',
  components: {Datepicker, CalendarIcon},
  props: {
    modelValue: {type: [Object, String], required: false},
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
  methods: {
    formatDate(date) {
      return moment(date).format('lll')
    },
  },
}
</script>

<style lang="scss" scoped>
.input-slot-image {
  margin-left: 15px;

  color: var(--typography-primary-color);
}
</style>

<style lang="scss">
.date-picker-wrapper {
  .dp__input {
    border-radius: 10px;
  }

  .dp__input_focus {
    border: 1px solid var(--border-active-color);
  }
}

.date-picker-menu {
  border-radius: 10px !important;

  .dp__today {
    border: 1px solid var(--primary-color);
  }

  .dp__active_date,
  .dp__pm_am_button {
    background: var(--primary-color);
  }

  .dp__button {
    border-radius: 10px;
  }
}
</style>
