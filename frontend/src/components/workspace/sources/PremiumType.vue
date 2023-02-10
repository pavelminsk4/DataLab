<template>
  <div class="filters-wrapper">
    <div class="alexa-ranking">
      <span class="second-title">Country</span>

      <BaseSelect class="select" v-model="country" :list="countryArray" />
    </div>

    <div class="alexa-ranking">
      <span class="second-title">Language</span>

      <BaseSelect class="select" v-model="country" :list="countryArray" />
    </div>
  </div>
</template>

<script>
import BaseSelect from '@/components/BaseSelect'

export default {
  name: 'PremiumType',
  components: {
    BaseSelect,
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
      follow: null,
      countryArray: [1, 2],
      tweets: [1, 2],
      followers: [1, 2],
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
.checkbox-wrapper {
  display: flex;

  margin-top: 13px;
}

.filters-wrapper {
  display: flex;
  justify-content: space-between;
}

.second-title {
  margin-bottom: 12px;

  font-size: 14px;
  color: var(--typography-primary-color-text-color);
}

.alexa-ranking {
  width: 250px;
}

.radio-btn {
  display: flex;

  margin-right: 25px;

  color: var(--typography-primary-color);

  cursor: pointer;
}

.not-check {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 20px;
  height: 20px;
  margin-right: 7px;

  border: 1px solid var(--typography-secondary-color);
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
  background: var(--button-primary-color);
}

.radio-wrapper > .selected .check-icon {
  display: flex;
}
</style>
