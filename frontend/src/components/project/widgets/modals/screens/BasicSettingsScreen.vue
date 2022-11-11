<template>
  <div class="options-wrapper">
    <div class="title">Widget Title</div>
    <BaseInput v-model="title" class="input-title" />

    <div class="title">Widget Description</div>
    <textarea
      class="description-field"
      placeholder="Some words about Widgets"
      v-model="description"
    />

    <div class="title">Date Aggregation Period</div>
    <BaseSelect
      v-model="aggregationPeriod"
      :list="aggregationPeriods"
      :is-reject-selection="false"
      @select-option="selectItem"
      name="aggregation-period"
      class="option"
    />

    <BaseButton @click="saveOptions">Save</BaseButton>
  </div>
</template>

<script>
import BaseInput from '@/components/BaseInput'
import BaseSelect from '@/components/BaseSelect'
import BaseButton from '@/components/buttons/BaseButton'

export default {
  name: 'BasicSettingsScreen',
  components: {BaseButton, BaseSelect, BaseInput},
  props: {
    aggregationPeriods: {
      type: [Object, Array],
      required: false,
    },
  },
  data() {
    return {
      aggregationPeriod: '',
      title: '',
      description: '',
    }
  },
  methods: {
    selectItem(name, val) {
      try {
        this.aggregationPeriod = val
        this.$emit('get-widget-params', val)
      } catch (e) {
        console.log(e)
      }
    },
    saveOptions() {
      this.$emit(
        'save-changes',
        this.title,
        this.description,
        this.aggregationPeriod
      )
    },
  },
}
</script>

<style lang="scss" scoped>
.options-wrapper {
  display: flex;
  flex-direction: column;
  flex: 1;

  margin-right: 30px;

  .input-title {
    width: 100%;
  }

  .title-general {
    padding-bottom: 10px;
    margin-bottom: 15px;

    border-bottom: 1px solid var(--primary-button-color);

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

  .option {
    margin-bottom: 25px;
  }

  .description-field {
    width: 100%;
    height: 132px;
    padding: 12px 16px;

    border: 1px solid var(--input-border-color);
    box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
    border-radius: 10px;
    background: var(--secondary-bg-color);

    color: var(--primary-text-color);

    resize: none;
  }

  .description-field::placeholder {
    color: var(--secondary-text-color);
  }

  .description-field::-webkit-scrollbar {
    width: 10px;
  }

  .description-field::-webkit-scrollbar-track {
    border-radius: 10px;

    -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  }

  .description-field::-webkit-scrollbar-thumb {
    width: 8px;

    border-radius: 10px;

    background-color: var(--box-shadow-color);
    outline: none;
  }
}
</style>
