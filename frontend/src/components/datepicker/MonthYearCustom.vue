<template>
  <div class="month-year-wrapper">
    <div class="custom-month-year-component">
      <select class="select-input" :value="year" @change="updateYear">
        <option v-for="y in years" :key="y.value" :value="y.value">
          {{ y.text }}
        </option>
      </select>
      <BaseCalendarSelect :options="yearsArray" @select-option="selectItem" />
      <select class="select-input" :value="month" @change="updateMonth">
        <option v-for="m in months" :key="m.value" :value="m.value">
          {{ m.text }}
        </option>
      </select>
    </div>
    <div class="icons">
      <span class="custom-icon" @click="onPrev">q</span>
      <span class="custom-icon" @click="onNext">w</span>
    </div>
  </div>
</template>

<script>
import {defineComponent, computed} from 'vue'
import BaseCalendarSelect from '@/components/datepicker/BaseCalendarSelect'

export default defineComponent({
  components: {BaseCalendarSelect},
  emits: ['update-month-year'],
  // Available props
  props: {
    months: {type: Array, default: () => []},
    years: {type: Array, default: () => []},
    filters: {type: Object, default: null},
    monthPicker: {type: Boolean, default: false},
    month: {type: Number, default: 0},
    year: {type: Number, default: 0},
    customProps: {type: Object, default: null},
  },
  setup(props, {emit}) {
    const updateMonthYear = (month, year) => {
      emit('update-month-year', {instance: 0, month, year})
    }

    const onNext = () => {
      let month = props.month
      let year = props.year
      if (props.month === 11) {
        month = 0
        year = props.year + 1
      } else {
        month += 1
      }
      updateMonthYear(month, year)
    }

    const onPrev = () => {
      let month = props.month
      let year = props.year
      if (props.month === 0) {
        month = 11
        year = props.year - 1
      } else {
        month -= 1
      }
      updateMonthYear(month, year)
    }

    const yearsArray = computed(() => {
      return props.years.map((el) => el.text)
    })

    const updateYear = (event) => {
      updateMonthYear(props.month, +event.target.value)
    }

    const updateMonth = (event) => {
      updateMonthYear(+event.target.value, props.year)
    }

    const selectItem = (option) => {
      updateMonthYear(props.month, option)
    }

    return {
      onNext,
      onPrev,
      updateYear,
      updateMonth,
      yearsArray,
      selectItem,
    }
  },
})
</script>

<style lang="scss">
.month-year-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
}
.custom-month-year-component {
  display: flex;
  align-items: center;
  justify-content: flex-start;
}

.select-input {
  margin: 5px 3px;
  padding: 5px;
  width: auto;
  border-radius: 4px;
  border-color: var(--dp-border-color);
  outline: none;
}

.icons {
  display: flex;
}

.custom-icon {
  padding: 5px;
  display: flex;
  height: 25px;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  width: 25px;
  color: var(--dp-icon-color);
  text-align: center;
  border-radius: 50%;

  svg {
    height: 20px;
    width: 20px;
  }

  &:hover {
    background: var(--dp-hover-color);
  }
}
</style>
