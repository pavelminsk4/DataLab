<template>
  <Datepicker
    v-model="selectedDateProxy"
    :month-year-component="monthYearCustom"
    :enableTimePicker="false"
    :action-row-component="actionRowCustom"
    @update:modelValue="handleDate"
    @internalModelChange="modelChange"
    @open="openCalendar"
    @closed="openCalendar"
    range
    inline
    class="datepicker-wrapper"
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
              selectedDate &&
              'active-range',
          ]"
        >
          {{ item.label }}
        </div>
      </div>

      <div class="right-side-title">Start date</div>
      <div class="time-picker">
        <div class="current-date">{{ formatDate(selectedDateProxy[0]) }}</div>
        <TimePickerCustom
          :name-hours="'hoursStartDate'"
          :name-minutes="'minutesStartDate'"
          @update:hours="updateTimePicker"
          @update:minutes="updateTimePicker"
        />
      </div>

      <div class="right-side-title">Ending date</div>

      <div class="time-picker">
        <div class="current-date">{{ formatDate(selectedDateProxy[1]) }}</div>
        <TimePickerCustom
          :name-hours="'hoursEndDate'"
          :name-minutes="'minutesEndDate'"
          @update:hours="updateTimePicker"
          @update:minutes="updateTimePicker"
        />
      </div>
    </template>
  </Datepicker>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'

import TimePickerCustom from '@/components/datepicker/TimePickerCustom'
import ActionRowCustom from '@/components/datepicker/ActionRowCustom'
import MonthYearCustom from '@/components/datepicker/MonthYearCustom'

import Datepicker from '@vuepic/vue-datepicker'
import {
  endOfMonth,
  startOfMonth,
  subMonths,
  startOfYesterday,
  endOfYesterday,
} from 'date-fns'

import '@vuepic/vue-datepicker/dist/main.css'

export default {
  name: 'BaseCalendar',
  components: {
    TimePickerCustom,
    Datepicker,
  },
  props: {
    currentProject: {
      type: [Object, Array],
      required: false,
    },
  },
  data() {
    return {
      hoursStartDate: '',
      minutesStartDate: '',
      hoursEndDate: '',
      minutesEndDate: '',
      selectedDate: true,
    }
  },
  computed: {
    ...mapState(['additionalFilters', 'keywords']),
    presetRanges() {
      return [
        {
          label: 'Last Week',
          range: this.lastWeeksDate,
        },
        {
          label: 'Yesterday',
          range: [startOfYesterday(new Date()), endOfYesterday(new Date())],
        },
        {label: 'Today', range: [new Date(), new Date()]},
        {
          label: 'Last 3 month',
          range: [this.getLastThreeMonthsDate(), new Date()],
        },
        {
          label: 'Last month',
          range: [
            startOfMonth(subMonths(new Date(), 1)),
            endOfMonth(subMonths(new Date(), 1)),
          ],
        },
      ]
    },
    selectedDateProxy: {
      get() {
        return this.additionalFilters?.date_range || this.lastWeeksDate
      },
      set(val) {
        this.selectedDate = val
        this[action.UPDATE_ADDITIONAL_FILTERS]({date_range: val})
      },
    },
    lastWeeksDate() {
      return [this.getLastWeeksDate(), new Date()]
    },
    timePickerCustom() {
      return TimePickerCustom
    },
    monthYearCustom() {
      return MonthYearCustom
    },
    actionRowCustom() {
      return ActionRowCustom
    },
  },
  methods: {
    ...mapActions([action.UPDATE_ADDITIONAL_FILTERS, action.POST_SEARCH]),
    handleDate(modelData) {
      try {
        this.selectedDate = [
          new Date(
            modelData[0].getFullYear(),
            modelData[0].getMonth(),
            modelData[0].getDate(),
            this.hoursStartDate || modelData[0].getHours(),
            this.minutesStartDate || modelData[0].getMinutes(),
            0,
            0
          ),
          new Date(
            modelData[1].getFullYear(),
            modelData[1].getMonth(),
            modelData[1].getDate(),
            this.hoursEndDate || modelData[1].getHours(),
            this.minutesEndDate || modelData[1].getMinutes(),
            0,
            0
          ),
        ]
        this[action.UPDATE_ADDITIONAL_FILTERS]({date_range: this.selectedDate})
        this[action.POST_SEARCH]({
          keywords: this.keywords?.keywords || [],
          additions: this.keywords?.additional_keywords || [],
          exceptions: this.keywords?.ignore_keywords || [],
          country: this.additionalFilters?.country || [],
          language: this.additionalFilters?.language || [],
          sentiment: this.additionalFilters?.sentiment || [],
          date_range: this.additionalFilters?.date_range || [],
          source: this.additionalFilters?.source || [],
          author: this.additionalFilters?.author || [],
        })
      } catch (e) {
        console.log(e)
      }
    },
    formatDate(date) {
      return date.toLocaleString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
      })
    },
    modelChange(date) {
      this.selectedDate = this.isSelectedDefaultRange(date)
    },
    addPeriod(range) {
      this.selectedDateProxy = range
    },
    openCalendar() {
      this.isOpenCalendar = !this.isOpenCalendar
    },
    updateTimePicker(value, name) {
      this[name] = value
    },
    getLastWeeksDate() {
      const now = new Date()

      return new Date(now.getFullYear(), now.getMonth(), now.getDate() - 7)
    },
    getLastThreeMonthsDate() {
      return new Date(
        new Date().getFullYear(),
        new Date().getMonth() - 3,
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
.datepicker-wrapper {
  position: absolute;
  top: 248px;
  right: 69px;
  z-index: 2;
}

.open-calendar {
  transform: rotate(180deg);
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
    background-color: var(--progress-line);

    cursor: pointer;

    font-style: normal;
    font-weight: 400;
    font-size: 12px;
    line-height: 20px;
    color: var(--secondary-text-color);

    &:hover {
      color: var(--primary-button-color);
      background-color: rgba(5, 95, 252, 0.1);
    }
  }

  .active-range {
    color: var(--primary-button-color);
    background-color: rgba(5, 95, 252, 0.1);
  }
}

.right-side-title {
  margin-bottom: 8px;

  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 110%;
  color: var(--primary-text-color);
}

.time-picker {
  display: flex;
  align-items: center;

  margin-bottom: 25px;

  .current-date {
    margin-right: 8px;
    padding: 10px 16px;

    background: var(--progress-line);
    border: 1px solid var(--modal-border-color);
    border-radius: 10px;

    white-space: nowrap;

    font-weight: 400;
    font-size: 14px;
    line-height: 20px;
    color: var(--primary-text-color);
  }
}
</style>

<style lang="scss">
.dp__menu {
  padding: 39px 40px 39px 31px;

  background: var(--secondary-bg-color);
  border: 1px solid var(--input-border-color);
  box-shadow: -4px 4px 20px rgba(16, 16, 16, 0.4);
  border-radius: 10px;

  &:focus {
    border: 1px solid var(--input-border-color);
    box-shadow: -4px 4px 20px rgba(16, 16, 16, 0.4);
  }
}

.dp__calendar_wrap {
  .dp__calendar_header {
    color: rgba(255, 255, 255, 0.5);

    font-style: normal;
    font-weight: 600;
    font-size: 12px;
    line-height: 166%;
  }

  .dp__calendar_header_separator {
    height: 0;
  }

  .dp__calendar {
    .dp__calendar_row {
      .dp__calendar_item {
        .dp__range_start,
        .dp__range_end {
          border: none;
          background-color: var(--primary-button-color);
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
          color: var(--primary-text-color);
        }

        .dp__cell_offset {
          font-style: normal;
          font-weight: 400;
          font-size: 12px;
          line-height: 143%;
          color: rgba(255, 255, 255, 0.3);
        }

        .dp__range_between {
          border: none;
          background-color: rgba(5, 95, 252, 0.2);
        }
      }
    }
  }
}

.dp__sidebar_right {
  margin-left: 35px;
  padding: 0;

  border: none;
}
</style>
