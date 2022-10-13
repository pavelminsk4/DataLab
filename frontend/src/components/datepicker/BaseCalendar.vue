<template>
  <Datepicker
    v-model="selectedDate"
    :month-year-component="monthYearCustom"
    :enableTimePicker="false"
    :action-row-component="actionRowCustom"
    @update:modelValue="handleDate"
    @open="openCalendar"
    @closed="openCalendar"
    range
    inline
    class="datepicker-wrapper"
  >
    <template #trigger>
      <div class="trigger-wrapper">
        <CalendarIcon class="dp-icon" />
        <div>
          {{ formatDate(selectedDate[0]) - formatDate(selectedDate[1]) }}
        </div>
        <ArrowDownIcon :class="[isOpenCalendar && 'open-calendar']" />
      </div>
    </template>

    <template #right-sidebar>
      <div class="fixed-period-wrapper">
        <div
          v-for="(item, index) in presetRanges"
          :key="index + 'year'"
          @click="test(item.range)"
          class="fixed-period"
        >
          {{ item.label }}
        </div>
      </div>

      <div class="right-side-title">Start date</div>
      <div class="time-picker">
        <div class="current-date">{{ formatDate(selectedDate[0]) }}</div>
        <TimePickerCustom
          :name-hours="'hoursStartDate'"
          :name-minutes="'minutesStartDate'"
          @update:hours="updateTimePicker"
          @update:minutes="updateTimePicker"
        />
      </div>

      <div class="right-side-title">Ending date</div>

      <div class="time-picker">
        <div class="current-date">{{ formatDate(selectedDate[1]) }}</div>
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
import {mapActions} from 'vuex'
import {action} from '@store/constants'

import '@vuepic/vue-datepicker/dist/main.css'

import Datepicker from '@vuepic/vue-datepicker'
import CalendarIcon from '@/components/icons/CalendarIcon'
import ArrowDownIcon from '@/components/icons/ArrowDownIcon'
import MonthYearCustom from '@/components/datepicker/MonthYearCustom'
import {
  endOfMonth,
  startOfMonth,
  subMonths,
  startOfYesterday,
  endOfYesterday,
} from 'date-fns'
import TimePickerCustom from '@/components/datepicker/TimePickerCustom'
import ActionRowCustom from '@/components/datepicker/ActionRowCustom'

export default {
  name: 'BaseCalendar',
  components: {
    TimePickerCustom,
    ArrowDownIcon,
    CalendarIcon,
    Datepicker,
  },
  data() {
    return {
      selectedDate: [new Date(), new Date()],
      isOpenCalendar: false,
      presetRanges: [
        {
          label: 'Last Week',
          range: [this.getLastWeeksDate(), new Date()],
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
      ],
      hoursStartDate: '',
      minutesStartDate: '',
      hoursEndDate: '',
      minutesEndDate: '',
    }
  },
  computed: {
    monthYearCustom() {
      return MonthYearCustom
    },
    timePickerCustom() {
      return TimePickerCustom
    },
    actionRowCustom() {
      return ActionRowCustom
    },
  },
  methods: {
    ...mapActions([action.UPDATE_ADDITIONAL_FILTERS]),
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
    test(range) {
      this.selectedDate = range
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
  },
}
</script>

<style lang="scss" scoped>
.datepicker-wrapper {
  position: absolute;
  top: 232px;
  right: 69px;
}

.trigger-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;

  width: 100%;
  padding: 10px 16px 10px 25px;

  background: var(--secondary-bg-color);
  border: 1px solid var(--input-border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
  border-radius: 8px;

  color: var(--primary-text-color);

  cursor: pointer;
}

.open-calendar {
  transform: rotate(180deg);
}

.fixed-period-wrapper {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;

  max-width: 285px;
  margin-bottom: 20px;

  .fixed-period {
    display: flex;
    white-space: nowrap;

    max-width: fit-content;
    padding: 4px 10px;

    border-radius: 8px;
    background-color: var(--progress-line);

    cursor: pointer;
    color: var(--secondary-text-color);

    &:hover {
      color: var(--primary-button-color);
      background-color: rgba(5, 95, 252, 0.1);
    }
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
  }

  .dp__calendar_header_separator {
    height: 0;
  }

  .dp__calendar {
    .dp__calendar_row {
      .dp__calendar_item {
        .dp__range_start,
        .dp__range_end {
          border-radius: 6px;
          color: var(--primary-button-color);
        }

        .dp__cell_inner {
          color: var(--primary-text-color);
        }

        .dp__cell_offset {
          color: rgba(255, 255, 255, 0.3);
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
