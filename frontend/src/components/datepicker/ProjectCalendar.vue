<template>
  <div class="project-calendar">
    <div>{{ name }}</div>
    <VueDatePicker
      v-model="selectedDateProxy"
      placeholder="Select date"
      text-input
      :range="isRange"
      :disabled-dates="disabledDates"
      :enable-time-picker="isEnableTimePicker"
    />
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import moment from 'moment'
import {action, get} from '@store/constants'

import VueDatePicker from '@vuepic/vue-datepicker'

export default {
  name: 'ProjectCalendar',
  components: {
    VueDatePicker,
  },
  props: {
    name: {type: String, default: 'Date'},
    startDate: {type: String, required: false},
    isDisableAfterToday: {type: Boolean, default: true},
    isRange: {type: Boolean, default: false},
    isEnableTimePicker: {type: Boolean, default: true},
  },
  data() {
    return {
      date: null,
    }
  },
  computed: {
    ...mapGetters({additionalFilters: get.ADDITIONAL_FILTERS}),
    initialDate() {
      const date = new Date(this.startDate)

      if (this.isRange) {
        return this.additionalFilters.date_range
      }

      return this.isValidDate(date) ? date : new Date()
    },
    selectedDateProxy: {
      get() {
        return this.date || this.initialDate
      },
      set(newValue) {
        this.date = newValue

        const format = 'YYYY-MM-DD'
        this[action.UPDATE_ADDITIONAL_FILTERS]({
          date_range: this.isRange ? newValue : [newValue, new Date()],
          start_date: this.isRange
            ? moment(this.startDate).format(format)
            : moment(newValue).format(format),
        })
      },
    },
  },
  methods: {
    ...mapActions([action.UPDATE_ADDITIONAL_FILTERS]),
    disabledDates(date) {
      let initialActiveDate = new Date(this.startDate)?.setDate(
        new Date(this.startDate).getDate() - 1
      )

      return this.isRange && this.isDisableAfterToday
        ? date < new Date(initialActiveDate)
        : date > new Date()
    },
    isValidDate(date) {
      return date instanceof Date && !isNaN(date)
    },
  },
}
</script>

<style lang="scss" scoped>
.project-calendar {
  display: flex;
  flex-direction: column;

  gap: 4px;
}
</style>
