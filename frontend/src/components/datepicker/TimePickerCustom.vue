<template>
  <div class="custom-time-picker-component">
    <select
      class="select-input"
      :value="hours"
      @change="$emit('update:hours', +$event.target.value, nameHours)"
      @click="$emit('update:hours', +$event.target.value, nameHours)"
    >
      <option v-for="h in hoursArray" :key="h.value" :value="h.value">
        {{ h.text }}
      </option>
    </select>
    <select
      class="select-input"
      :value="minutes"
      @change="$emit('update:minutes', +$event.target.value, nameMinutes)"
      @click="$emit('update:minutes', +$event.target.value, nameMinutes)"
    >
      <option v-for="m in minutesArray" :key="m.value" :value="m.value">
        {{ m.text }}
      </option>
    </select>
  </div>
</template>

<script>
import {computed, defineComponent} from 'vue'

export default defineComponent({
  emits: ['update:hours', 'update:minutes'],
  props: {
    hoursIncrement: {type: [Number, String], default: 1},
    minutesIncrement: {type: [Number, String], default: 1},
    is24: {type: Boolean, default: true},
    hoursGridIncrement: {type: [String, Number], default: 1},
    minutesGridIncrement: {type: [String, Number], default: 5},
    range: {type: Boolean, default: false},
    filters: {type: Object, default: () => ({})},
    minTime: {type: Object, default: () => ({})},
    maxTime: {type: Object, default: () => ({})},
    timePicker: {type: Boolean, default: false},
    hours: {type: [Number, Array], default: 0},
    minutes: {type: [Number, Array], default: 0},
    customProps: {type: Object, default: null},
    nameHours: {type: String, required: true},
    nameMinutes: {type: String, required: true},
  },
  setup() {
    // Generate array of hours
    const hoursArray = computed(() => {
      const arr = []
      for (let i = 0; i < 24; i++) {
        arr.push({text: i < 10 ? `0${i}` : i, value: i})
      }
      return arr
    })

    // Generate array of minutes
    const minutesArray = computed(() => {
      const arr = []
      for (let i = 0; i < 60; i++) {
        arr.push({text: i < 10 ? `0${i}` : i, value: i})
      }
      return arr
    })

    return {
      hoursArray,
      minutesArray,
    }
  },
})
</script>

<style lang="scss">
.custom-time-picker-component {
  display: flex;
  align-items: center;
  justify-content: center;
}

.select-input {
  margin: 5px 3px;
  padding: 5px;
  width: 100px;
  border-radius: 4px;
  border-color: var(--dp-border-color);
  outline: none;
}
</style>
