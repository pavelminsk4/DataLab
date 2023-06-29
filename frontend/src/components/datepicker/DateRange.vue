<template>
  <div class="calendar-wrapper">
    <Datepicker
      v-model="selectedDateProxy"
      :month-year-component="monthYearCustom"
      :enableTimePicker="false"
      :action-row-component="actionRowCustom"
      range
      inline
      @internalModelChange="modelChange"
      @open="openCalendar"
      @closed="openCalendar"
    >
      <template #right-sidebar>
        <div class="fixed-period-wrapper">
          <div
            v-for="(item, index) in presetRanges"
            :key="'default-' + index"
            @click="addPeriod(item.range)"
            :class="[
              'fixed-period',
              isSelectedDefaultRange(item.range) &&
                isSelectedDateOnCalendar &&
                'active-range',
            ]"
          >
            {{ item.label }}
          </div>
        </div>
      </template>
    </Datepicker>
    <div class="custom-date">
      <div class="hint">FORMAT: dd/mm/yyyy hh:mm am OR pm</div>

      <BaseInput
        v-model="firstDate"
        label="Start date"
        :hasError="hasError"
        :errorMessage="errorMessage"
        class="custom-input-field"
      />
      <BaseInput
        v-model="lastDate"
        label="Ending date"
        :hasError="hasError"
        :errorMessage="errorMessage"
        class="custom-input-field"
      />
    </div>
  </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'

import ActionRowCustom from '@/components/datepicker/ActionRowCustom'
import MonthYearCustom from '@/components/datepicker/MonthYearCustom'

import Datepicker from '@vuepic/vue-datepicker'
import {
  startOfToday,
  endOfToday,
  startOfYesterday,
  endOfYesterday,
} from 'date-fns'

import '@vuepic/vue-datepicker/dist/main.css'
import BaseInput from '@/components/common/BaseInput'

const START_DATE = {type: 'startDate', index: 0}
const ENDING_DATE = {type: 'endingDate', index: 1}

export default {
  name: 'DateRange',
  components: {
    Datepicker,
    BaseInput,
  },
  data() {
    return {
      hoursStartDate: '',
      minutesStartDate: '',
      hoursEndDate: '',
      minutesEndDate: '',
      selectedDate: null,
      isSelectedDateOnCalendar: true,
      startDate: null,
      endingDate: null,
      errorMessage: '',
      hasError: false,
    }
  },
  computed: {
    ...mapState(['additionalFilters']),
    presetRanges() {
      return [
        {
          label: 'Last Week',
          range: this.lastWeekDate,
        },
        {
          label: 'Yesterday',
          range: [startOfYesterday(), endOfYesterday()],
        },
        {
          label: 'Today',
          range: [startOfToday(), endOfToday()],
        },
        {
          label: 'Last 3 month',
          range: [this.getLastFewMonthsDate(3), new Date()],
        },
        {
          label: 'Last month',
          range: [this.getLastFewMonthsDate(1), new Date()],
        },
      ]
    },
    firstDate: {
      get() {
        return (
          this.formatDateForInput(this.startDate) ||
          this.formatDateForInput(this.selectedDateProxy[0])
        )
      },
      set(val) {
        this.setDateFromInput(val, START_DATE)
      },
    },
    lastDate: {
      get() {
        return (
          this.formatDateForInput(this.endingDate) ||
          this.formatDateForInput(this.selectedDateProxy[1])
        )
      },
      set(val) {
        this.setDateFromInput(val, ENDING_DATE)
      },
    },
    selectedDateProxy: {
      get() {
        return this.additionalFilters?.date_range || this.lastWeekDate
      },
      set(val) {
        this[action.UPDATE_ADDITIONAL_FILTERS]({date_range: val})
      },
    },
    lastWeekDate() {
      return [this.getLastWeekDate(), endOfToday()]
    },
    monthYearCustom() {
      return MonthYearCustom
    },
    actionRowCustom() {
      return ActionRowCustom
    },
  },
  methods: {
    ...mapActions([action.UPDATE_ADDITIONAL_FILTERS]),
    formatDateForInput(date) {
      return date
        ?.toLocaleString('en-AU', {
          year: 'numeric',
          month: 'numeric',
          day: 'numeric',
          hour: '2-digit',
          minute: 'numeric',
        })
        .replace(',', '')
    },
    setDateFromInput(value, dateType) {
      var formatDateRegex =
        /([0-9]{2})\/([0-9]{2})\/([0-9]{4}) ([0-9]{1,2}):([0-9]{2})\s*[aApP][mM]/
      if (!formatDateRegex.test(value)) {
        return false
      } else {
        let dateArray = value.toUpperCase().split(/[\s/:]/g)
        let collectDate = new Date(
          dateArray[2],
          parseInt(dateArray[1]) - 1,
          dateArray[0],
          ...this.convertTime12to24(
            value.toUpperCase().substring(value.length - 8)
          )
        )
        this[dateType.type] = collectDate
        this.selectedDateProxy[dateType.index] = collectDate
        this.validateDateRange(this.selectedDateProxy)
        this[action.UPDATE_ADDITIONAL_FILTERS]({
          date_range: this.selectedDateProxy,
        })
      }
    },
    modelChange(date) {
      this.startDate = date[0]
      this.endingDate = date[1]
      this.isSelectedDateOnCalendar = this.isSelectedDefaultRange(date)
    },
    validateDateRange(datesArray) {
      if (datesArray[0] < datesArray[1]) {
        this.hasError = false
      } else {
        this.errorMessage = 'Enter the correct time range!'
        this.hasError = true
      }
    },
    convertTime12to24(time12h) {
      const [time, modifier] = time12h.split(' ')
      let [hours, minutes] = time.split(':')
      if (hours === '12') {
        hours = '00'
      }
      if (modifier === 'PM') {
        hours = parseInt(hours, 10) + 12
      }
      return [hours, minutes]
    },
    addPeriod(range) {
      this.selectedDateProxy = range
    },
    openCalendar() {
      this.isOpenCalendar = !this.isOpenCalendar
    },
    getLastWeekDate() {
      const now = new Date()

      return new Date(now.getFullYear(), now.getMonth(), now.getDate() - 6)
    },
    getLastFewMonthsDate(count) {
      return new Date(
        new Date().getFullYear(),
        new Date().getMonth() - count,
        new Date().getDate()
      )
    },
    isSelectedDefaultRange(val) {
      for (let i = 0; i < val.length; i++) {
        return (
          `${this.selectedDateProxy[i].getYear()} - ${this.selectedDateProxy[
            i
          ].getMonth()} - - ${this.selectedDateProxy[i].getDate()}` ===
          `${val[i].getYear()} - ${val[i].getMonth()} - - ${val[i].getDate()}`
        )
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.calendar-wrapper {
  position: relative;
  z-index: 2;
  .custom-date {
    position: absolute;
    top: 100px;
    right: 31px;

    display: flex;
    flex-direction: column;

    width: 235px;
    margin-top: 20px;

    .hint {
      font-size: 10px;
    }

    .custom-input-field {
      margin-bottom: 20px;
      border-radius: 10px;

      white-space: nowrap;
    }
  }
}

.fixed-period-wrapper {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;

  max-width: 235px;
  margin-bottom: 20px;

  .fixed-period {
    display: flex;
    white-space: nowrap;

    max-width: fit-content;
    padding: 4px 10px;

    border-radius: 8px;
    background-color: var(--chips-background-primary-color);

    cursor: pointer;

    font-style: normal;
    font-weight: 400;
    font-size: 12px;
    line-height: 20px;
    color: var(--typography-secondary-color);

    &:hover {
      color: var(--button-primary-color);
      background-color: rgba(5, 95, 252, 0.1);
    }
  }

  .active-range {
    color: var(--button-primary-color);
    background-color: rgba(5, 95, 252, 0.1);
  }
}

.right-side-title {
  margin-bottom: 8px;

  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 110%;
  color: var(--typography-primary-color);
}
</style>

<style lang="scss">
.calendar-wrapper {
  .dp {
    &__menu {
      height: 400px;
      padding: 39px 40px 39px 31px;

      background: var(--background-secondary-color);
      border: 1px solid var(--input-border-color);
      border-radius: 10px;

      &:focus {
        border: 1px solid var(--input-border-color);
        box-shadow: -4px 4px 20px rgba(16, 16, 16, 0.4);
      }
    }

    &__calendar_wrap {
      .dp__calendar {
        &_header {
          color: var(--typography-title-color);

          font-style: normal;
          font-weight: 600;
          font-size: 12px;
          line-height: 166%;
        }

        &_header_separator {
          height: 0;
        }

        &_row {
          .dp__calendar_item {
            .dp__range_start,
            .dp__range_end {
              border: none;
              background-color: var(--button-primary-color);
            }

            .dp__range_start {
              border-top-left-radius: 6px;
              border-bottom-left-radius: 6px;
            }

            .dp__range_end {
              border-top-right-radius: 6px;
              border-bottom-right-radius: 6px;
            }

            .dp__cell_inner {
              font-style: normal;
              font-weight: 400;
              font-size: 12px;
              line-height: 143%;
              color: var(--typography-primary-color);
            }

            .dp__cell_offset {
              font-style: normal;
              font-weight: 400;
              font-size: 12px;
              line-height: 143%;
              color: var(--typography-secondary-color);
            }

            .dp__range_between {
              border: none;
              background-color: rgba(5, 95, 252, 0.2);
            }
          }
        }
      }
    }

    &__sidebar_right {
      width: 235px;
      margin-left: 35px;
      padding: 0;

      border: none;
    }

    &__month_year_select {
      color: var(--typography-primary-color);
    }

    &__overlay {
      background: var(--background-secondary-color);
    }

    &__overlay_cell {
      color: var(--typography-primary-color);
      background: var(--primary-bg-color);
    }

    &__time_display {
      color: var(--typography-primary-color);
    }

    &__button_bottom {
      color: var(--typography-primary-color);
      background-color: var(--button-primary-color);
    }
  }
}
</style>
