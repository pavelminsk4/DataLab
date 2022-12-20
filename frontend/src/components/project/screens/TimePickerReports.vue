<template>
  <div class="timepicker-reports-wrapper">
    <div class="wrapper-button">
      <div
        v-for="button in timePicker"
        :key="button.name"
        :class="[timePickerName === button.name && 'active-button']"
        @click="openAccessories"
      >
        {{ button.name }}
      </div>
    </div>

    <section class="time-picker-settings-wrapper">
      <div class="title">Repeat time</div>
      <div v-if="timePickerName === 'Hourly'" class="frequency-sending">
        Every
        <BaseInput v-model="hours" class="hours-counter">
          <div class="arrows-wrapper">
            <ArrowDownIcon
              @click="increase('hours')"
              class="arrow-input arrow-increase"
            />
            <ArrowDownIcon
              @click="decrease('hours')"
              :class="['arrow-input', hours === 1 && 'disabled']"
            />
          </div>
        </BaseInput>
        hour
      </div>

      <div class="title">The ending</div>
      <div class="radio-wrapper">
        <BaseRadio
          v-for="(item, index) in endingDate"
          :key="item + index"
          :checked="item"
          :value="selectedValue"
          class="radio-btn"
          @change="changeValue(item)"
        >
          <template #default>
            <div class="not-check"><CheckRadioIcon class="check-icon" /></div>
            {{ item }}
          </template>
        </BaseRadio>

        <Datepicker
          v-if="selectedValue === 'Date'"
          v-model="hoursDate"
          :close-on-auto-apply="true"
          :format="formatDate"
          :is-24="false"
          @update:model-value="handleDate"
          placeholder="Select date"
          auto-apply
          class="date-picker"
        >
          <template #input-icon>
            <CalendarIcon class="input-slot-image" />
          </template>
        </Datepicker>
      </div>

      <div class="title">Template</div>
      <BaseSelect
        v-model="template"
        placeholder="Select Template"
        name="template"
        :list="titleTemplates"
        :is-reject-selection="false"
        @select-option="selectItem"
        class="select"
      />
    </section>
  </div>
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import BaseRadio from '@/components/BaseRadio'
import BaseInput from '@/components/BaseInput'
import ArrowDownIcon from '@/components/icons/ArrowDownIcon'
import CheckRadioIcon from '@/components/icons/CheckRadioIcon'
import BaseSelect from '@/components/BaseSelect'

import Datepicker from '@vuepic/vue-datepicker'
import '@vuepic/vue-datepicker/dist/main.css'
import CalendarIcon from '@/components/icons/CalendarIcon'

export default {
  name: 'TimePickerReports',
  components: {
    CalendarIcon,
    BaseSelect,
    BaseRadio,
    CheckRadioIcon,
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
      hours: 1,
      selectedValue: '',
      hoursDate: [],
      template: '',
      endingDate: ['Never', 'Date'],
      timePickerName: 'Hourly',
      timePicker: [
        {name: 'Hourly'},
        {name: 'Daily'},
        {name: 'Weekly'},
        {name: 'Monthly'},
      ],
      isShowCalendar: false,
    }
  },
  created() {
    this[action.GET_TEMPLATES]()
  },
  computed: {
    ...mapGetters({
      templates: get.TEMPLATES,
    }),
    titleTemplates() {
      return this.templates.map((el) => el.title)
    },
    calendarDate() {
      return this.formatDate(new Date())
    },
  },
  methods: {
    ...mapActions([action.GET_TEMPLATES]),
    openAccessories(e) {
      this.timePickerName =
        this.timePickerName === e.target.innerText ? null : e.target.innerText
    },
    increase(val) {
      this[val] = this[val] + 1
      this.$emit('repeat-time', this[val])
    },
    decrease(val) {
      this[val] = this[val] - 1
      this.$emit('repeat-time', this[val])
    },
    changeValue(newValue) {
      this.selectedValue = newValue
      this.$emit('ending-date', this.selectedValue)
    },
    openCalendar() {
      this.isShowCalendar = !this.isShowCalendar
    },
    handleDate(modelData) {
      this.$emit('update-ending-date', modelData)
    },
    selectItem(name, val) {
      let currentElement = this.templates.filter((el) => el.title === val)
      this.$emit('select-template', currentElement[0].id)
    },
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
    align-items: flex-end;

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

.select {
  margin-top: 16px;
}

.check-icon {
  display: none;
}

.radio-btn {
  display: flex;

  margin: 0 25px 8px 0;

  color: var(--primary-text-color);

  cursor: pointer;
}

.not-check {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 20px;
  height: 20px;
  margin-right: 7px;

  border: 1px solid var(--secondary-text-color);
  border-radius: 50px;

  cursor: pointer;
}

.radio-wrapper {
  display: flex;
  align-items: center;
  flex-wrap: wrap;

  margin: 10px 0 25px;
}

.radio-wrapper > .selected {
  background: none;
}

.radio-wrapper > .selected .not-check {
  border: none;
  background: var(--primary-button-color);
}

.radio-wrapper > .selected .check-icon {
  display: flex;
}

.input-slot-image {
  margin-left: 15px;

  color: var(--primary-text-color);
}
</style>

<style>
.dp__input_wrap {
  width: 240px;
  height: 40px;
}

.dp__input_readonly {
  background: #34353b;
  border: 1px solid #404046;
  border-radius: 10px;

  color: var(--primary-text-color);
}

.dp__arrow_top {
  border: none;
  background: #404046;
}
</style>
