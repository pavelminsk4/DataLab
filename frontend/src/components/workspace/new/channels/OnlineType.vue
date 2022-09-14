<template>
  <div class="filters-wrapper">
    <div class="alexa-ranking">
      <span class="second-title">Country</span>

      <BaseSelect class="select" v-model="country" :list="countryArray" />

      <span class="second-title">Language</span>

      <BaseSelect class="select" v-model="country" :list="countryArray" />
    </div>

    <div class="alexa-ranking">
      <span class="second-title">City</span>

      <BaseInput class="input" />

      <span class="second-title">Source</span>

      <BaseInput class="input" />
    </div>
  </div>
  <span class="second-title">Sentiment</span>

  <div class="radio-wrapper">
    <BaseRadio
      v-for="(item, index) in sentiments"
      :key="index"
      :checked="item"
      :value="selectedValue"
      class="radio-btn"
      @change="changeValue(item)"
    >
      <template v-slot:default>
        <div class="not-check"><CheckRadioIcon class="check-icon" /></div>
        {{ item.value }}
      </template>
    </BaseRadio>
  </div>
</template>

<script>
import BaseRadio from '@/components/BaseRadio'
import CheckRadioIcon from '@/components/icons/CheckIcon'
import BaseSelect from '@/components/BaseSelect'
import BaseInput from '@/components/BaseInput'

export default {
  name: 'OnlineType',
  components: {
    BaseInput,
    BaseSelect,
    CheckRadioIcon,
    BaseRadio,
  },
  data() {
    return {
      alexaRanking: [{value: '10%'}, {value: '20%'}, {value: '30%'}],
      sentiments: [
        {value: 'Negative'},
        {value: 'Neutral'},
        {value: 'Positive'},
      ],
      selectedValue: '',
      country: null,
      countryArray: [1, 2],
    }
  },
  methods: {
    changeValue(newValue) {
      this.selectedValue = newValue
    },
  },
}
</script>

<style lang="scss" scoped>
.filters-wrapper {
  display: flex;
  justify-content: space-between;
}

.second-title {
  margin-bottom: 12px;

  font-size: 14px;
  color: var(--primary-text-color);
}

.alexa-ranking {
  width: 250px;
}

.radio-btn {
  display: flex;

  margin-right: 25px;

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
  justify-content: space-between;

  margin: 10px 0 25px;
}

.select,
.input {
  margin: 12px 0 25px;
}

.check-icon {
  display: none;
}
</style>

<style>
.additional-key > .input-tag {
  margin-bottom: 10px;
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
</style>
