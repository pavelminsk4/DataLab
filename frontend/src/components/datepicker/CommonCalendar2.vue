<template>
  <Datepicker
    v-model="selectedDateProxy"
    placeholder="Select date"
    text-input
    :range="isRange"
    :disabled-dates="disabledAfterToday"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

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
    ...mapGetters({additionalFilters: get.ADDITIONAL_FILTERS}),
    selectedDateProxy: {
      get() {
        return this.date
      },
      set(newValue) {
        this.date = newValue
        this[action.UPDATE_ADDITIONAL_FILTERS]({
          date_range: [newValue, new Date()],
        })
      },
    },
  },
  methods: {
    ...mapActions([action.UPDATE_ADDITIONAL_FILTERS]),
    disabledAfterToday(date) {
      return this.isRange
        ? date < this.additionalFilters.date_range[0]
        : date > new Date()
    },
  },
}
</script>
