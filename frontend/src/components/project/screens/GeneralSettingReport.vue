<template>
  <div>
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
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseRadio from '@/components/BaseRadio'
import BaseSelect from '@/components/BaseSelect'
import CalendarIcon from '@/components/icons/CalendarIcon'
import CheckRadioIcon from '@/components/icons/CheckRadioIcon'

import Datepicker from '@vuepic/vue-datepicker'
import '@vuepic/vue-datepicker/dist/main.css'

export default {
  name: 'GeneralSettingReport',
  components: {BaseRadio, CheckRadioIcon, BaseSelect, CalendarIcon, Datepicker},
  data() {
    return {
      selectedValue: '',
      template: '',
      hoursDate: [],
      endingDate: ['Never', 'Date'],
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
    changeValue(newValue) {
      this.selectedValue = newValue
      this.$emit('ending-date', this.selectedValue)
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
    handleDate(modelData) {
      this.$emit('update-ending-date', modelData)
    },
    selectItem(name, val) {
      let currentElement = this.templates.filter((el) => el.title === val)
      this.$emit('select-template', currentElement[0].id)
    },
  },
}
</script>

<style lang="scss" scoped>
.title {
  font-style: normal;
  font-weight: 500;
  font-size: 14px;
  line-height: 110%;
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

.radio-btn {
  display: flex;

  margin: 0 25px 8px 0;

  color: var(--primary-text-color);

  cursor: pointer;
}

.check-icon {
  display: none;
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

.input-slot-image {
  margin-left: 15px;

  color: var(--primary-text-color);
}

.select {
  margin-top: 16px;
}
</style>

<style>
.radio-wrapper .dp__input_wrap {
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
