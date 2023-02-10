<template>
  <div v-if="templates.length">
    <div class="title">The ending</div>
    <div class="radio-wrapper">
      <BaseRadio
        v-for="(item, index) in endingDate"
        :key="item + index"
        v-model="selectedValueProxy"
        :id="currentTimePicker + index"
        :value="item"
        :label="item"
        class="radio-btn"
      />

      <Datepicker
        v-if="selectedValueProxy === 'Date'"
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
      :current-value="currentTemplate?.title"
      :hasError="!!reportTemplateError"
      :errorMessage="reportTemplateError"
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

import Datepicker from '@vuepic/vue-datepicker'
import '@vuepic/vue-datepicker/dist/main.css'

export default {
  name: 'GeneralSettingReport',
  components: {BaseRadio, BaseSelect, CalendarIcon, Datepicker},
  props: {
    currentEndingTimeValue: {
      type: String,
      required: false,
    },
    currentTemplateId: {
      type: [String, Number],
      required: false,
    },
    currentTimePicker: {
      type: String,
      required: true,
    },
    reportTemplateError: {
      type: String,
      default: null,
    },
  },
  data() {
    return {
      selectedValue: 'Never',
      template: '',
      hoursDate: '',
      endingDate: ['Never', 'Date'],
    }
  },
  computed: {
    ...mapGetters({
      templates: get.TEMPLATES,
    }),
    titleTemplates() {
      return this.templates.map((el) => el.title)
    },
    currentTemplate() {
      return this.templates.find((el) => el.id === this.currentTemplateId)
    },
    calendarDate() {
      return this.formatDate(new Date())
    },
    selectedValueProxy: {
      get() {
        return this.currentEndingTimeValue ? 'Date' : this.selectedValue
      },
      set(val) {
        this.selectedValue = val
        this.$emit('update-ending-date', this.selectedValue)
      },
    },
  },
  created() {
    if (this.currentEndingTimeValue) {
      this.hoursDate = this.currentEndingTimeValue
    }
  },
  methods: {
    ...mapActions([action.GET_TEMPLATES]),
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

.radio-btn {
  margin: 0 25px 8px 0;
}

.input-slot-image {
  margin-left: 15px;

  color: var(--typography-primary-color);
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

  color: var(--typography-primary-color);
}

.dp__arrow_top {
  border: none;
  background: #404046;
}
</style>
