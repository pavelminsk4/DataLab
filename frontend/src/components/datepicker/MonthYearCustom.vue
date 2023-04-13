<template>
  <div class="month-year-wrapper">
    <div class="custom-month-year-component">
      <BaseCalendarSelect
        :options="yearsArray"
        :value="year"
        :name="'month-year'"
        @select-option="updateYear"
        class="select-year"
      />
      <BaseCalendarSelect
        :options="months"
        :value="currentMonth(month)"
        :name="'month-year'"
        @select-option="updateMonth"
        :selectWidth="95"
      />
    </div>
    <div class="icons">
      <CalendarControlIcon class="custom-icon" @click="onPrev" />
      <CalendarControlIcon class="custom-icon" @click="onNext" />
    </div>
  </div>
</template>

<script>
import {defineComponent, computed} from 'vue'

import BaseCalendarSelect from '@/components/datepicker/BaseCalendarSelect'
import CalendarControlIcon from '@/components/icons/CalendarControlIcon'

import {years, months} from '@/lib/constants'

export default defineComponent({
  components: {CalendarControlIcon, BaseCalendarSelect},
  emits: ['update-month-year'],
  props: {
    filters: {type: Object, default: null},
    monthPicker: {type: Boolean, default: false},
    month: {type: Number, default: 0},
    year: {type: Number, default: 0},
    customProps: {type: Object, default: null},
  },
  setup(props, {emit}) {
    const updateMonthYear = (month, year) => {
      emit('update-month-year', {instance: 0, month, year})
    }

    const onNext = () => {
      let month = props.month
      let year = props.year
      if (props.month === 11) {
        month = 0
        year = +props.year + 1
      } else {
        month += 1
      }
      updateMonthYear(month, year)
    }

    const onPrev = () => {
      let month = props.month
      let year = props.year
      if (props.month === 0) {
        month = 11
        year = props.year - 1
      } else {
        month -= 1
      }
      updateMonthYear(month, year)
    }

    const currentMonth = (numOfMonth) => {
      return months[numOfMonth]
    }

    const yearsArray = computed(() => {
      return years.map((el) => el.text)
    })

    const updateMonth = (option) => {
      const selectedMonth = computed(() => {
        return [{text: option, value: months.indexOf(option)}]
      })

      updateMonthYear(selectedMonth.value[0].value, props.year)
    }

    const updateYear = (option) => {
      updateMonthYear(props.month, +option)
    }

    return {
      onNext,
      onPrev,
      updateYear,
      updateMonth,
      yearsArray,
      months,
      currentMonth,
    }
  },
})
</script>

<style lang="scss" scoped>
.month-year-wrapper {
  display: flex;
  justify-content: space-between;

  background-color: var(--background-secondary-color);

  .custom-month-year-component {
    display: flex;

    .select-year {
      margin-right: 15px;
    }
  }

  .icons {
    margin: 5px;

    .custom-icon {
      cursor: pointer;

      &:hover {
        color: var(--button-primary-color);
      }

      &:last-child {
        margin-left: 18px;

        transform: rotate(180deg);
      }
    }
  }
}
</style>
