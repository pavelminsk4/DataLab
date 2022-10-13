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
        <div>{{ format(selectedDate) }}</div>
        <ArrowDownIcon :class="[isOpenCalendar && 'open-calendar']" />
      </div>
    </template>

    <template #right-sidebar>
      <span
        v-for="(item, index) in presetRanges"
        :key="index + 'year'"
        @click="test(item.range)"
        >{{ item.label }}
      </span>

      <div>Start date</div>
      <div>1</div>
      <TimePickerCustom
        :name-hours="'hoursStartDate'"
        :name-minutes="'minutesStartDate'"
        @update:hours="updateTimePicker"
        @update:minutes="updateTimePicker"
      />

      <div>Ending date</div>
      <div>2</div>
      <TimePickerCustom
        :name-hours="'hoursEndDate'"
        :name-minutes="'minutesEndDate'"
        @update:hours="updateTimePicker"
        @update:minutes="updateTimePicker"
      />
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
  endOfYear,
  startOfMonth,
  startOfYear,
  subMonths,
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
        {label: 'Today', range: [new Date(), new Date()]},
        {
          label: 'This month',
          range: [startOfMonth(new Date()), endOfMonth(new Date())],
        },
        {
          label: 'Last month',
          range: [
            startOfMonth(subMonths(new Date(), 1)),
            endOfMonth(subMonths(new Date(), 1)),
          ],
        },
        {
          label: 'This year',
          range: [startOfYear(new Date()), endOfYear(new Date())],
        },
        {
          label: 'This year (slot)',
          range: [startOfYear(new Date()), endOfYear(new Date())],
          slot: 'yearly',
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
      console.log(this.hoursStartDate, modelData[0].getHours())
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
    format(date) {
      const formattedDate = date.map((el) =>
        el.toLocaleString('en-US', {
          month: 'short',
          day: 'numeric',
          year: 'numeric',
        })
      )
      return `${formattedDate[0]} - ${formattedDate[1]}`
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
</style>

<style lang="scss">
.dp__menu {
  padding: 39px 40px 39px 31px;

  background: red;
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
  border: none;
}
</style>
