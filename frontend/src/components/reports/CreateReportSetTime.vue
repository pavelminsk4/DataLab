<template>
  <section class="set-time-wrapper">
    <h4 class="label">Sending Time</h4>
    <div>
      <SetTimeCheckbox
        v-model="hour.hourly_enabled"
        title="By Hour"
        class="set-time-box"
      >
        <span>Every</span>
        <BaseSelect
          v-model="selectHour"
          :currentValue="selectHour"
          name="hours"
          :list="hours"
          :isRejectSelection="false"
        />
      </SetTimeCheckbox>

      <SetTimeCheckbox
        v-model="day.daily_enabled"
        title="By Day"
        class="set-time-box"
      >
        <span>Time</span>
        <Datepicker
          v-model="timePickerDay"
          :is-24="false"
          time-picker
          auto-apply
          placeholder="Time"
          menu-class-name="time-picker-menu"
          class="time-picker"
        >
          <template #input-icon>
            <svg></svg>
          </template>
        </Datepicker>
      </SetTimeCheckbox>

      <SetTimeCheckbox
        v-model="week.weekly_enabled"
        title="By Week"
        class="set-time-box"
      >
        <span>Weekday</span>
        <BaseSelect
          v-model="selectWeekday"
          :currentValue="selectWeekday"
          name="weekday"
          :list="weekDays"
          :isRejectSelection="false"
          class="set-time__select"
        />

        <span>Time</span>
        <Datepicker
          v-model="timePickerWeek"
          :is-24="false"
          time-picker
          auto-apply
          placeholder="Time"
          menu-class-name="time-picker-menu"
          class="time-picker"
        >
          <template #input-icon>
            <svg></svg>
          </template>
        </Datepicker>
      </SetTimeCheckbox>

      <SetTimeCheckbox
        v-model="month.monthly_enabled"
        title="By Month"
        class="set-time-box"
      >
        <span>Day of month</span>
        <BaseSelect
          v-model="month.m_day_of_month"
          :currentValue="month.m_day_of_month"
          name="month"
          :list="dayOfMonth"
          :isRejectSelection="false"
          class="set-time__select"
        />

        <span>Time</span>
        <Datepicker
          v-model="timePickerMonth"
          :is-24="false"
          time-picker
          auto-apply
          placeholder="Time"
          menu-class-name="time-picker-menu"
          class="time-picker"
        >
          <template #input-icon>
            <svg></svg>
          </template>
        </Datepicker>
      </SetTimeCheckbox>
    </div>

    <h4 class="label">The Ending</h4>
    <p>Stop sending reports</p>

    <BaseRadio
      v-model="stopSendingReports"
      :checked="ending.NEVER"
      id="stop-sending-never"
      :value="ending.NEVER"
      :label="ending.NEVER"
      class="stop-sending__radio-btn"
    />
    <BaseRadio
      v-model="stopSendingReports"
      :checked="ending.DATE"
      id="stop-sending-date"
      :value="ending.DATE"
      :label="ending.DATE"
      class="stop-sending__radio-btn"
    />

    <div :class="['stop-sending', isDisableStopSendingDate && 'disable']">
      <p class="stop-sending_label">Date</p>
      <Datepicker
        v-model="stopSendingReportDate"
        :close-on-auto-apply="true"
        :format="formatDate"
        :is-24="false"
        placeholder="Select date"
        auto-apply
      >
        <template #input-icon>
          <CalendarIcon class="input-slot-image" />
        </template>
      </Datepicker>
    </div>

    <footer class="create-reports__footer">
      <ButtonWithArrow
        :is-disabled="isDisableNextBtn"
        class="create-reports_next-step-button"
        @click="nextStep"
      >
        <span>Next</span>
      </ButtonWithArrow>
    </footer>
  </section>
</template>

<script>
import {action} from '@store/constants'
import createReportMixin from '@/lib/mixins/create-report.js'
import {weekDays} from '@/lib/constants'

import CalendarIcon from '@/components/icons/CalendarIcon'

import Datepicker from '@vuepic/vue-datepicker'
import SetTimeCheckbox from '@/components/common/SetTimeCheckbox'
import BaseSelect from '@/components/BaseSelect'
import BaseRadio from '@/components/BaseRadio'

const ending = {
  NEVER: 'Never',
  DATE: 'Date',
}

export default {
  name: 'CreateReportSetTime',
  mixins: [createReportMixin],
  components: {
    SetTimeCheckbox,
    BaseSelect,
    Datepicker,
    BaseRadio,
    CalendarIcon,
  },
  data() {
    return {
      hour: {
        hourly_enabled: false,
        h_hour: '1',
      },
      day: {
        daily_enabled: false,
        d_hour: '0',
        d_minute: '0',
      },
      week: {
        weekly_enabled: false,
        w_day_of_week: 7,
        w_hour: '0',
        w_minute: '0',
      },
      month: {
        monthly_enabled: false,
        m_day_of_month: '1',
        m_hour: '0',
        m_minute: '0',
      },
      stopSendingReports: ending.NEVER,
      stopSendingReportDate: '',
    }
  },
  computed: {
    isDisableNextBtn() {
      return !(
        this.hour.hourly_enabled ||
        this.day.daily_enabled ||
        this.week.weekly_enabled ||
        this.month.monthly_enabled
      )
    },
    isDisableStopSendingDate() {
      return this.stopSendingReports === ending.NEVER
    },
    selectHour: {
      get() {
        const additionalWord = this.hour.h_hour === '1' ? ' hour' : ' hours'
        return this.hour.h_hour + additionalWord
      },
      set(val) {
        this.hour.h_hour = val.replace(/[^0-9]/g, '')
      },
    },
    selectWeekday: {
      get() {
        if (this.week.w_day_of_week === 7) return this.weekDays[0]
        return this.weekDays[this.week.w_day_of_week]
      },
      set(val) {
        const currentIndex = this.weekDays.indexOf(val)
        this.week.w_day_of_week = currentIndex || 7
      },
    },
    timePickerDay: {
      get() {
        return {
          hours: this.day.d_hour || 0,
          minutes: this.day.d_minute || 0,
        }
      },
      set(val) {
        this.day.d_hour = val.hours
        this.day.d_minute = val.minutes
      },
    },
    timePickerWeek: {
      get() {
        return {
          hours: this.week.w_hour || 0,
          minutes: this.week.w_minute || 0,
        }
      },
      set(val) {
        this.week.w_hour = val.hours
        this.week.w_minute = val.minutes
      },
    },
    timePickerMonth: {
      get() {
        return {
          hours: this.month.m_hour || 0,
          minutes: this.month.m_minute || 0,
        }
      },
      set(val) {
        this.month.m_hour = val.hours
        this.month.m_minute = val.minutes
      },
    },
  },
  created() {
    this.ending = ending

    this.hours = new Array(23).fill(0).map((item, index) => {
      const additionalWord = index + 1 === 1 ? ' hour' : ' hours'
      return index + 1 + additionalWord
    })

    this.weekDays = weekDays

    this.dayOfMonth = new Array(31).fill(0).map((item, index) => index + 1)
  },
  methods: {
    formatDate(date) {
      return new Date(date).toLocaleString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
        hour12: true,
        hour: 'numeric',
        minute: 'numeric',
      })
    },
    nextStep() {
      let data = {}

      const endingDate = this.stopSendingReportDate
        ? this.stopSendingReportDate
        : null

      if (this.hour.hourly_enabled) {
        data = {...data, ...this.hour, h_ending_date: endingDate}
      }
      if (this.day.daily_enabled) {
        data = {...data, ...this.day, d_ending_date: endingDate}
      }
      if (this.week.weekly_enabled) {
        data = {...data, ...this.week, w_ending_date: endingDate}
      }
      if (this.month.monthly_enabled) {
        data = {...data, ...this.month, m_ending_date: endingDate}
      }

      const nextStep = 3
      const nextStepName = this.getNextStepName(nextStep)

      this[action.UPDATE_NEW_REPORT]({
        step: nextStep,
        ...data,
      })
      this.$router.push({name: nextStepName})
    },
  },
}
</script>

<style lang="scss" scoped>
.set-time-wrapper {
  display: flex;
  flex-direction: column;

  width: 65%;

  span {
    margin-right: 5px;
  }
}

.set-time-box:not(:last-child) {
  margin-bottom: 12px;
}

.set-time__select {
  margin-right: 12px;
}

.label {
  margin-bottom: 20px;

  &:not(:first-child) {
    margin-top: 32px;
  }
}

.time-picker {
  width: 108px;

  border-radius: var(--border-radius);
}

.stop-sending {
  &__radio-btn {
    width: 100%;
    margin-top: 12px;
  }

  &_label {
    margin: 20px 0 4px;
  }

  &__time-picker {
    width: 100%;
  }
}

.input-slot-image {
  margin-left: 15px;

  color: var(--typography-primary-color);
}
</style>
