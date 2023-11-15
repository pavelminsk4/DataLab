<template>
  <div class="common-calendar">
    <CustomText tag="span" text="Date" class="title" />

    <div class="date-wrapper">
      <div
        class="trigger-wrapper"
        :style="`width: ${width}px`"
        @click="openCalendar"
      >
        <CalendarIcon />
        <div class="calendar-date">{{ calendarDate }}</div>
        <ArrowDownIcon :class="[isShowCalendarContents && 'open-calendar']" />
      </div>
      <div :class="['calendar', `calendar-position-${position}`]">
        <DateRange v-if="isShowCalendarContents" />
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapState, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import {defaultDate} from '@lib/utilities'

import CustomText from '@components/CustomText'
import CalendarIcon from '@components/icons/CalendarIcon'
import DateRange from '@components/datepicker/DateRange'
import ArrowDownIcon from '@components/icons/ArrowDownIcon'

export default {
  name: 'CommonCalendar',
  components: {
    DateRange,
    CustomText,
    CalendarIcon,
    ArrowDownIcon,
  },
  props: {
    width: {type: String, default: '100%'},
    position: {type: String, default: 'bottom'},
  },
  computed: {
    ...mapState(['isShowCalendarContents']),
    ...mapGetters({
      additionalFilters: get.ADDITIONAL_FILTERS,
    }),
    calendarDate() {
      if (this.additionalFilters?.date_range?.length) {
        const currentDate = this.additionalFilters?.date_range.map((el) =>
          this.defaultDate(el, this.platformLanguage)
        )

        return `${currentDate[0]} - ${currentDate[1]}`
      } else {
        return `${this.defaultDate(
          this.getLastWeeksDate(),
          this.platformLanguage
        )} - ${this.defaultDate(new Date(), this.platformLanguage)}`
      }
    },
  },
  methods: {
    ...mapActions([action.REFRESH_DISPLAY_CALENDAR]),
    defaultDate,
    openCalendar() {
      this[action.REFRESH_DISPLAY_CALENDAR](!this.isShowCalendarContents)
    },
    getLastWeeksDate() {
      const now = new Date()
      return new Date(now.getFullYear(), now.getMonth(), now.getDate() - 6)
    },
  },
}
</script>

<style lang="scss" scoped>
.common-calendar {
  position: relative;

  margin-bottom: 40px;
}

.title {
  margin-bottom: 4px;

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--typography-title-color);
}

.date-wrapper {
  position: absolute;

  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  gap: 20px;

  width: 100%;
  margin-bottom: 25px;

  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--typography-secondary-color);

  .trigger-wrapper {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 12px;

    border: 1px solid var(--input-border-color);
    background: var(--chips-background-primary-color);
    border-radius: 8px;

    cursor: pointer;

    .calendar-date {
      flex-grow: 1;
    }

    .open-calendar {
      transform: rotate(180deg);
    }
  }
}

.calendar {
  position: absolute;
}

.calendar-position-bottom {
  top: 100%;
  bottom: auto;
}

.calendar-position-top {
  top: auto;
  bottom: 100%;
}
</style>
