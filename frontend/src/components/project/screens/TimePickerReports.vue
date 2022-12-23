<template>
  <div class="timepicker-reports-wrapper">
    <div class="wrapper-button">
      <div
        v-for="button in timePicker"
        :key="button.name"
        :class="[timePickerName === button.name && 'active-button']"
        @click="toggleTimePickerSettings"
      >
        {{ button.name }}
      </div>
    </div>

    <section class="time-picker-settings-wrapper">
      <div class="title">Repeat time</div>
      <div v-show="timePickerName === 'Hourly'" class="frequency-sending">
        <div class="repeat-time-wrapper">
          Every
          <BaseInput v-model="hour" placeholder="0" class="hours-counter">
            <div class="arrows-wrapper">
              <ArrowDownIcon
                @click="increase('hour')"
                class="arrow-input arrow-increase"
              />
              <ArrowDownIcon
                @click="decrease('hour')"
                :class="['arrow-input', hour === 1 && 'disabled']"
              />
            </div>
          </BaseInput>
          hour
        </div>
        <GeneralSettingReport
          current-time-picker="Hourly"
          :current-ending-time-value="regularReport.h_ending_date"
          :current-template-id="regularReport.h_template"
          @ending-date="setEndingDate"
          @update-ending-date="updateEndingDate"
          @select-template="selectTemplate"
        />
      </div>

      <div v-show="timePickerName === 'Daily'" class="frequency-sending">
        <Datepicker
          v-model="timePickerValueDaily"
          :is-24="false"
          @update:model-value="handleTimePickerDaily"
          time-picker
          auto-apply
          placeholder="Time"
          menu-class-name="time-picker-menu"
          class="time-picker"
        >
          <template #input-icon>
            <ClockIcon class="input-slot-image" />
          </template>
        </Datepicker>

        <GeneralSettingReport
          current-time-picker="Daily"
          :current-ending-time-value="regularReport.d_ending_date"
          :current-template-id="regularReport.d_template"
          @ending-date="setEndingDate"
          @update-ending-date="updateEndingDate"
          @select-template="selectTemplate"
        />
      </div>

      <div v-show="timePickerName === 'Weekly'" class="frequency-sending">
        <div class="weekly-wrapper">
          <div class="week-days">
            <div
              v-for="(item, index) in weekDays"
              :key="item.name + index"
              @click="chooseDay(item.value)"
              :class="['day', activeDayProxy === item.value && 'active-day']"
            >
              {{ item.name }}
            </div>
          </div>

          <Datepicker
            v-model="timePickerValueWeekly"
            :is-24="false"
            @update:model-value="handleTimePickerWeekly"
            time-picker
            auto-apply
            placeholder="Time"
            menu-class-name="time-picker-menu"
            class="time-picker"
          >
            <template #input-icon>
              <ClockIcon class="input-slot-image" />
            </template>
          </Datepicker>
        </div>

        <GeneralSettingReport
          current-time-picker="Weekly"
          :current-ending-time-value="regularReport.w_ending_date"
          :current-template-id="regularReport.w_template"
          @ending-date="setEndingDate"
          @update-ending-date="updateEndingDate"
          @select-template="selectTemplate"
        />
      </div>

      <div v-show="timePickerName === 'Monthly'" class="frequency-sending">
        <div class="monthly-wrapper">
          <div class="repeat-time-wrapper">
            Every
            <BaseInput
              v-model="dayOfMonth"
              placeholder="0"
              class="hours-counter"
            >
              <div class="arrows-wrapper">
                <ArrowDownIcon
                  @click="increase('dayOfMonth')"
                  class="arrow-input arrow-increase"
                />
                <ArrowDownIcon
                  @click="decrease('dayOfMonth')"
                  :class="['arrow-input', dayOfMonth === 1 && 'disabled']"
                />
              </div>
            </BaseInput>
            day
          </div>

          <Datepicker
            v-model="timePickerValueMonthly"
            :is-24="false"
            @update:model-value="handleTimePickerMonthly"
            time-picker
            auto-apply
            placeholder="Time"
            menu-class-name="time-picker-menu"
            class="time-picker monthly-picker"
          >
            <template #input-icon>
              <ClockIcon class="input-slot-image" />
            </template>
          </Datepicker>
        </div>

        <GeneralSettingReport
          current-time-picker="Monthly"
          :current-ending-time-value="regularReport.m_ending_date"
          :current-template-id="regularReport.m_template"
          @ending-date="setEndingDate"
          @update-ending-date="updateEndingDate"
          @select-template="selectTemplate"
        />
      </div>
    </section>
  </div>
</template>

<script>
import BaseInput from '@/components/BaseInput'
import ClockIcon from '@/components/icons/ClockIcon'
import ArrowDownIcon from '@/components/icons/ArrowDownIcon'
import GeneralSettingReport from '@/components/project/screens/GeneralSettingReport'

import Datepicker from '@vuepic/vue-datepicker'
import '@vuepic/vue-datepicker/dist/main.css'

export default {
  name: 'TimePickerReports',
  components: {
    GeneralSettingReport,
    ClockIcon,
    ArrowDownIcon,
    BaseInput,
    Datepicker,
  },
  props: {
    regularReport: {
      type: [Array, Object],
      default: () => [],
    },
  },
  data() {
    return {
      hour: 1,
      dayOfMonth: 1,
      timePickerValueDaily: {},
      timePickerValueWeekly: {},
      timePickerValueMonthly: {},
      timePickerName: 'Hourly',
      timePicker: [
        {name: 'Hourly'},
        {name: 'Daily'},
        {name: 'Weekly'},
        {name: 'Monthly'},
      ],
      weekDays: [
        {name: 'Sun', value: 7},
        {name: 'Mon', value: 1},
        {name: 'Tue', value: 2},
        {name: 'Wed', value: 3},
        {name: 'Thu', value: 4},
        {name: 'Fri', value: 5},
        {name: 'Sat', value: 6},
      ],
      activeDay: null,
    }
  },
  created() {
    if (this.regularReport.length) {
      this.hour = this.regularReport.h_hour
      this.activeDay = +this.regularReport.w_day_of_week
      this.dayOfMonth = this.regularReport.m_day_of_month
      this.timePickerValueDaily = {
        hours: this.regularReport.d_hour,
        minutes: this.regularReport.d_minute,
        seconds: 0,
      }
      this.timePickerValueWeekly = {
        hours: this.regularReport.w_hour,
        minutes: this.regularReport.w_minute,
        seconds: 0,
      }
      this.timePickerValueMonthly = {
        hours: this.regularReport.m_hour,
        minutes: this.regularReport.m_minute,
        seconds: 0,
      }
    }
  },
  computed: {
    activeDayProxy: {
      get() {
        return +this.regularReport.w_day_of_week || this.activeDay
      },
      set(val) {
        this.activeDay = val
      },
    },
  },
  methods: {
    toggleTimePickerSettings(e) {
      this.timePickerName = e.target.innerText
    },
    increase(val) {
      this[val] = +this[val] + 1
      this.$emit('repeat-time', this[val], val)
    },
    decrease(val) {
      this[val] = +this[val] - 1
      this.$emit('repeat-time', this[val], val)
    },
    handleTimePickerDaily(modelTime) {
      this.$emit('update-time-daily', modelTime)
    },
    handleTimePickerMonthly(modelTime) {
      this.$emit('update-time-monthly', modelTime)
    },
    handleTimePickerWeekly(modelTime) {
      this.$emit('update-time-weekly', modelTime)
    },
    chooseDay(val) {
      this.activeDay = val
      this.$emit('choose-weekly-day', val)
    },
    setEndingDate(val) {
      switch (this.timePickerName) {
        case 'Hourly':
          return this.$emit('ending-date-hourly', val, 'endingTimeHourly')
        case 'Daily':
          return this.$emit('ending-date-hourly', val, 'endingTimeDaily')
        case 'Weekly':
          return this.$emit('ending-date-hourly', val, 'endingTimeWeekly')
        case 'Monthly':
          return this.$emit('ending-date-hourly', val, 'endingTimeMonthly')
      }
    },
    updateEndingDate(val) {
      switch (this.timePickerName) {
        case 'Hourly':
          return this.$emit(
            'update-ending-date-hourly',
            val,
            'endingTimeHourly'
          )
        case 'Daily':
          return this.$emit('update-ending-date-hourly', val, 'endingTimeDaily')
        case 'Weekly':
          return this.$emit(
            'update-ending-date-hourly',
            val,
            'endingTimeWeekly'
          )
        case 'Monthly':
          return this.$emit(
            'update-ending-date-hourly',
            val,
            'endingTimeMonthly'
          )
      }
    },
    selectTemplate(val) {
      switch (this.timePickerName) {
        case 'Hourly':
          return this.$emit('select-hourly-template', val, 'hourlyTemplate')
        case 'Daily':
          return this.$emit('select-hourly-template', val, 'dailyTemplate')
        case 'Weekly':
          return this.$emit('select-hourly-template', val, 'weeklyTemplate')
        case 'Monthly':
          return this.$emit('select-hourly-template', val, 'monthlyTemplate')
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.timepicker-reports-wrapper {
  width: 100%;
}

.wrapper-button {
  display: flex;
  gap: 38px;

  padding-bottom: -10px;

  border-bottom: 1px solid var(--input-border-color);

  cursor: pointer;

  font-style: normal;
  font-weight: 500;
  font-size: 14px;
  line-height: 22px;
  color: rgba(255, 255, 255, 0.8);

  .active-button {
    padding-bottom: 10px;

    border-bottom: 2px solid var(--primary-button-color);

    color: var(--primary-text-color);
  }
}

.repeat-time-wrapper {
  display: flex;
  align-items: flex-end;

  margin: 15px 0 40px;

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
}

.time-picker-settings-wrapper {
  position: relative;

  padding: 35px;
  margin-top: 25px;

  border-radius: 15px;
  background: var(--secondary-bg-color);
  border: 1px solid var(--input-border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);

  color: var(--primary-text-color);

  .frequency-sending {
    display: flex;
    flex-direction: column;

    margin: 15px 0 40px;

    .hours-counter {
      width: 80px;
      margin: 0 12px;

      .arrows-wrapper {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 3px;

        margin-right: 18px;

        cursor: pointer;

        .arrow-input {
          color: var(--primary-text-color);

          &:hover {
            color: var(--primary-button-color);
          }
        }

        .disabled {
          display: none;
        }

        .arrow-increase {
          margin-left: 0.5px;
          transform: rotate(180deg);

          &:hover {
            color: var(--primary-button-color);
          }
        }
      }
    }
  }
}

.title {
  font-style: normal;
  font-weight: 500;
  font-size: 14px;
  line-height: 110%;
}

.input-slot-image {
  margin: 0 10px 0 16px;
}

.time-picker {
  width: 135px;

  margin-bottom: 40px;

  background: var(--progress-line);
  border-radius: 10px;
}

.monthly-picker {
  margin-top: 18px;
}

.weekly-wrapper {
  display: flex;

  .week-days {
    display: flex;
    gap: 5px;

    margin-right: 32px;

    .day {
      display: flex;
      align-items: center;
      justify-content: center;

      width: 40px;
      height: 40px;

      background: var(--progress-line);
      border: 1px solid var(--modal-border-color);
      border-radius: 10px;

      cursor: pointer;

      font-style: normal;
      font-weight: 400;
      font-size: 14px;
      line-height: 110%;
      color: rgba(255, 255, 255, 0.8);
    }

    .active-day {
      background: var(--primary-button-color);
    }
  }
}

.monthly-wrapper {
  display: flex;
  align-items: center;
  gap: 25px;
}
</style>

<style>
.time-picker-menu {
  padding: 0;
}

.dp__date_hover:hover {
  color: var(--hover-button-color) !important;
}

.dp__arrow_bottom {
  background-color: var(--secondary-bg-color);
  border: none;
}
</style>
