<template>
  <div>
    <span class="title">Date</span>
    <div class="date-wrapper">
      <div class="trigger-wrapper" @click="openCalendar">
        <CalendarIcon />
        <div class="calendar-date">{{ calendarDate }}</div>
        <ArrowDownIcon :class="[isShowCalendarContents && 'open-calendar']" />
      </div>
      <BaseCalendar
        v-if="isShowCalendarContents"
        :class="[`calendar-position-${position}`]"
      />
    </div>
  </div>
</template>

<script>
import {mapActions, mapState, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import CalendarIcon from '@/components/icons/CalendarIcon'
import BaseCalendar from '@/components/datepicker/BaseCalendar'
import ArrowDownIcon from '@/components/icons/ArrowDownIcon'

export default {
  name: 'CommonCalendar',
  components: {
    BaseCalendar,
    CalendarIcon,
    ArrowDownIcon,
  },
  props: {
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
          this.formatDate(el)
        )

        return `${currentDate[0]} - ${currentDate[1]}`
      } else {
        return `${this.formatDate(this.getLastWeeksDate())} - ${this.formatDate(
          new Date()
        )}`
      }
    },
  },
  methods: {
    ...mapActions([action.REFRESH_DISPLAY_CALENDAR]),
    openCalendar() {
      this[action.REFRESH_DISPLAY_CALENDAR](!this.isShowCalendarContents)
    },
    formatDate(date) {
      return date.toLocaleString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
      })
    },
    getLastWeeksDate() {
      const now = new Date()
      return new Date(now.getFullYear(), now.getMonth(), now.getDate() - 7)
    },
  },
}
</script>

<style lang="scss" scoped>
.title {
  margin-bottom: 4px;

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--typography-title-color);
}

.date-wrapper {
  position: relative;

  display: flex;
  align-items: center;
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

    width: 100%;
    padding: 10px 12px;

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

.calendar-position-bottom {
  top: 100%;
  bottom: auto;
}

.calendar-position-top {
  top: auto;
  bottom: 100%;
}
</style>
