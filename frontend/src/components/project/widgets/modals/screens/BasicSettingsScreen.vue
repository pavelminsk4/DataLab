<template>
  <div class="options-wrapper">
    <BaseInput
      v-model="title"
      label="Widget Title"
      :hasError="!!errors.titleError"
      :errorMessage="errors.titleError"
      class="input-title title"
      @update="errors.titleError = null"
    />

    <BaseTextarea
      v-model="description"
      label="Widget Description"
      placeholder="Some words about Widgets"
    />

    <div v-if="hasAggregationPeriod">
      <CustomText text="Date Aggregation Period" class="title" />
      <BaseSelect
        v-model="aggregationPeriod"
        :list="aggregationPeriods"
        :is-reject-selection="false"
        :current-value="capitalizeFirstLater(period)"
        @select-option="selectItem"
        name="aggregation-period"
      />
    </div>
  </div>
</template>

<script>
import {isAllFieldsEmpty} from '@lib/utilities'

import CustomText from '@components/CustomText'
import BaseInput from '@components/common/BaseInput'
import BaseSelect from '@components/BaseSelect'
import BaseTextarea from '@components/common/BaseTextarea'

export default {
  name: 'BasicSettingsScreen',
  components: {BaseTextarea, BaseSelect, BaseInput, CustomText},
  props: {
    widgetTitle: {type: String, required: false},
    widgetDescription: {type: String, required: false},
    period: {type: String, required: false},
    hasAggregationPeriod: {type: Boolean, default: true},
  },
  data() {
    return {
      newTitle: null,
      newDescription: '',
      aggregationPeriod: this.period,
      aggregationPeriods: ['Hour', 'Day', 'Month', 'Year'],
      errors: {
        titleError: null,
      },
    }
  },
  computed: {
    title: {
      get() {
        if (this.newTitle === '') return this.newTitle
        return this.newTitle || this.widgetTitle
      },
      set(value) {
        this.newTitle = value
        this.errors.titleError = this.newTitle ? null : 'required'

        if (!isAllFieldsEmpty(this.errors)) return
        this.$emit('update-general-data', this.newTitle, 'newWidgetTitle')
      },
    },

    description: {
      get() {
        return this.widgetDescription
      },
      set(value) {
        this.newDescription = value
        this.$emit(
          'update-general-data',
          this.newDescription,
          'newWidgetDescription'
        )
      },
    },
  },
  methods: {
    selectItem(name, value) {
      try {
        this.$emit('update-general-data', value, 'newAggregationPeriod')
        this.$emit('change-aggregation-period', value)
      } catch (e) {
        console.error(e)
      }
    },
    capitalizeFirstLater(string) {
      return string.charAt(0).toUpperCase() + string.slice(1)
    },
  },
}
</script>

<style lang="scss" scoped>
.options-wrapper {
  display: flex;
  flex-direction: column;
  flex: 1;

  .input-title {
    width: 100%;
    margin-bottom: 20px;
  }

  .title-general {
    padding-bottom: 10px;
    margin-bottom: 15px;

    border-bottom: 1px solid var(--button-primary-color);

    font-weight: 400;
    font-size: 14px;
    line-height: 22px;
  }

  .title {
    margin: 25px 0 12px;

    font-style: normal;
    font-weight: 500;
    font-size: 14px;
    line-height: 110%;
  }

  &::placeholder {
    color: var(--typography-secondary-color);
  }
}
</style>
