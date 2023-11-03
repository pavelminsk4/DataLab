<template>
  <div class="project-calendar">
    <div>Date</div>
    <VueDatePicker
      v-model="selectedDateProxy"
      placeholder="Select date"
      text-input
      :range="isRange"
      :disabled-dates="disabledDates"
    />
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import VueDatePicker from '@vuepic/vue-datepicker'

export default {
  name: 'ProjectCalendar',
  components: {
    VueDatePicker,
  },
  props: {
    isDesableAfterToday: {type: Boolean, default: true},
    isRange: {type: Boolean, default: false},
    isCurrentProject: {type: Boolean, default: false},
  },
  data() {
    return {
      date: null,
    }
  },
  computed: {
    ...mapGetters({additionalFilters: get.ADDITIONAL_FILTERS}),
    initialDate() {
      return this.additionalFilters?.date_range[0]
    },
    selectedDateProxy: {
      get() {
        return this.isRange ? [this.initialDate, new Date()] : this.date
      },
      set(newValue) {
        this.date = newValue
        this[action.UPDATE_ADDITIONAL_FILTERS]({
          date_range: this.isRange ? newValue : [newValue, new Date()],
        })
      },
    },
  },
  methods: {
    ...mapActions([action.UPDATE_ADDITIONAL_FILTERS]),
    disabledDates(date) {
      var startDate = new Date(this.initialDate).setDate(
        this.initialDate.getDate() - 1
      )

      return this.isRange && this.isDesableAfterToday
        ? date < new Date(startDate)
        : date > new Date()
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
