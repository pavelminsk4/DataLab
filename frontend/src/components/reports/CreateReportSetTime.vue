<template>
  <section class="set-time-wrapper">
    <h4>Sending Time</h4>
    <div>
      <SetTimeCheckbox title="By Hour">
        <span>Every</span>
        <BaseSelect
          v-model="selectHour"
          name="hours"
          :list="hours"
          :isRejectSelection="false"
        />
      </SetTimeCheckbox>

      <SetTimeCheckbox title="By Day">
        <span>Time</span>
      </SetTimeCheckbox>

      <SetTimeCheckbox title="By Week">
        <span>Weekday</span>
        <BaseSelect
          v-model="selectWeekday"
          name="weekday"
          :list="weekDays"
          :isRejectSelection="false"
        />
      </SetTimeCheckbox>

      <SetTimeCheckbox title="By Month">
        <span>Every</span>
      </SetTimeCheckbox>
    </div>

    <BaseButton :is-disabled="true" class="next-button" @click="nextStep">
      <span>Next</span>
      <ArrowLeftIcon class="button-arrow-icon" />
    </BaseButton>
  </section>
</template>

<script>
import ArrowLeftIcon from '@/components/icons/ArrowLeftIcon'
import BaseButton from '@/components/common/BaseButton'
import SetTimeCheckbox from '@/components/common/SetTimeCheckbox'
import BaseSelect from '@/components/BaseSelect'

export default {
  name: 'CreateReportSetTime',
  components: {
    ArrowLeftIcon,
    BaseButton,
    SetTimeCheckbox,
    BaseSelect,
  },
  data() {
    return {
      hour: {
        h_hour: '',
      },
      week: {
        w_day_of_week: '',
      },
    }
  },
  computed: {
    selectHour: {
      get() {
        const additionalWord = this.hour.h_hour === 1 ? ' hour' : ' hours'
        return this.hour.h_hour + additionalWord
      },
      set(val) {
        console.log(val.replace(/^\d+$/))
        this.hour.h_hour = val.replace(/^\d+$/)
      },
    },
    selectWeekday: {
      get() {
        return this.weekDays[this.week.w_day_of_week] || ''
      },
      set(val) {
        this.week.w_day_of_week = this.weekDays.indexOf(val)
      },
    },
  },
  created() {
    this.hours = new Array(23).fill(0)
    this.hours = this.hours.map((item, index) => {
      console.log('sdf')
      const additionalWord = index + 1 === 1 ? 'hour' : 'hours'
      return index + 1 + additionalWord
    })
    console.log(this.hours)
    this.weekDays = [
      'Sunday',
      'Monday',
      'Tuesday',
      'Wednesday',
      'Thursday',
      'Friday',
      'Saturday',
    ]
  },
  methods: {
    nextStep() {},
  },
}
</script>

<style lang="scss" scoped>
.form-wrapper {
  display: flex;
  flex-direction: column;

  width: 56%;
  margin-top: 40px;
}

.next-button {
  align-self: flex-end;

  margin-top: 32px;

  .button-arrow-icon {
    margin-left: 10px;
    transform: rotate(180deg);
  }
}
</style>
