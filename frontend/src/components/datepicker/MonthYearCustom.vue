<template>
  <div class="month-year-wrapper">
    <div class="custom-month-year-component">
      <BaseCalendarSelect
        :options="yearsArray"
        :default="year"
        :name="'month-year'"
        @select-option="updateYear"
        class="select-year"
      />
      <BaseCalendarSelect
        :options="monthArray"
        :default="currentMonth"
        :name="'month-year'"
        @select-option="updateMonth"
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

export default defineComponent({
  components: {CalendarControlIcon, BaseCalendarSelect},
  emits: ['update-month-year'],
  props: {
    months: {type: Array, default: () => []},
    years: {type: Array, default: () => []},
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
        year = props.year + 1
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

    const currentMonth = computed(() => {
      return props.months.filter((el) => el.value === props.month)[0].text
    })

    const yearsArray = computed(() => {
      return props.years.map((el) => el.text)
    })

    const monthArray = computed(() => {
      return props.months.map((el) => el.text)
    })

    const updateMonth = (option) => {
      console.log(option)
      const selectedMonth = computed(() => {
        return props.months.filter((el) => el.text === option)
      })

      updateMonthYear(selectedMonth.value[0].value, props.year)
    }

    const updateYear = (option) => {
      updateMonthYear(props.month, option)
    }

    return {
      onNext,
      onPrev,
      updateYear,
      updateMonth,
      yearsArray,
      monthArray,
      currentMonth,
    }
  },
})
</script>

<style lang="scss" scoped>
.month-year-wrapper {
  display: flex;
  justify-content: space-between;

  background-color: var(--secondary-bg-color);

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
        color: var(--primary-button-color);
      }

      &:last-child {
        margin-left: 18px;

        transform: rotate(180deg);
      }
    }
  }
}
</style>
