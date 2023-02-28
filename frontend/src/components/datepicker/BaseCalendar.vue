<template>
  <Datepicker
    v-model="selectedDateProxy"
    :month-year-component="monthYearCustom"
    :enableTimePicker="false"
    :action-row-component="actionRowCustom"
    range
    inline
    class="datepicker-wrapper"
    @update:modelValue="handleDate"
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
        <div class="current-date">
          {{ formatDate(selectedDateProxy[1]) }}
        </div>
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
  startOfToday,
  endOfToday,
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
        return this.additionalFilters?.date_range || this.lastWeekDate
      },
      set(val) {
        this.selectedDate = val
        this[action.UPDATE_ADDITIONAL_FILTERS]({date_range: val})
      },
    },
    lastWeekDate() {
      return [this.getLastWeekDate(), endOfToday()]
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
          posts_per_page: 20,
          page_number: 1,
          sort_posts: [],
          country_dimensions: [],
          language_dimensions: [],
          source_dimensions: [],
          author_dimensions: [],
          sentiment_dimensions: [],
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
    getLastWeekDate() {
      const now = new Date()

      return new Date(now.getFullYear(), now.getMonth(), now.getDate() - 6)
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
  top: 100%;
  left: 0;
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

.time-picker {
  display: flex;
  align-items: center;

  margin-bottom: 25px;

  .current-date {
    margin-right: 8px;
    padding: 10px 16px;

    background: var(--chips-background-primary-color);
    border: var(--border-primary);
    border-radius: 10px;

    white-space: nowrap;

    font-weight: 400;
    font-size: 14px;
    line-height: 20px;
    color: var(--typography-primary-color);
  }
}
</style>

<style lang="scss">
.dp__menu {
  padding: 39px 40px 39px 31px;

  background: var(--background-secondary-color);
  border: 1px solid var(--input-border-color);
  border-radius: 10px;

  &:focus {
    border: 1px solid var(--input-border-color);
    box-shadow: -4px 4px 20px rgba(16, 16, 16, 0.4);
  }
}

.dp__calendar_wrap {
  .dp__calendar_header {
    color: var(--typography-title-color);

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

.dp__sidebar_right {
  margin-left: 35px;
  padding: 0;

  border: none;
}

.dp__month_year_select {
  color: var(--typography-primary-color);
}

.dp__overlay {
  background: var(--background-secondary-color);
}

.dp__overlay_cell {
  color: var(--typography-primary-color);
  background: var(--primary-bg-color);
}

.dp__time_display {
  color: var(--typography-primary-color);
}

.dp__button_bottom {
  color: var(--typography-primary-color);
  background-color: var(--button-primary-color);
}
</style>
