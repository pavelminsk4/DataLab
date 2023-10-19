<template>
  <Datepicker
    v-model="selectedDateProxy"
    placeholder="Start Typing ..."
    text-input
    :range="isRange"
    :disabled-dates="disabledAfterToday"
  />
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'

import Datepicker from '@vuepic/vue-datepicker'

export default {
  name: 'DateRange',
  components: {
    Datepicker,
  },
  props: {
    isRange: {type: Boolean, default: false},
  },
  data() {
    return {
      date: new Date(),
    }
  },
  computed: {
    ...mapState(['additionalFilters']),
    selectedDateProxy: {
      get() {
        return this.date
      },
      set(val) {
        this.date = val
        this[action.UPDATE_ADDITIONAL_FILTERS]({date_range: [val, val]})
      },
    },
  },
  methods: {
    ...mapActions([action.UPDATE_ADDITIONAL_FILTERS]),
    disabledAfterToday(date) {
      const today = new Date()
      today.setHours(0, 0, 0, 0)

      if (this.isRange) {
        return date < this.additionalFilters.date_range[0]
      } else {
        return date > today
      }
    },
  },
}
</script>
