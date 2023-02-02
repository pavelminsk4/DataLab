<template>
  <div class="filters-wrapper">
    <div class="alexa-ranking">
      <span class="second-title">Country</span>

      <BaseSelect class="select" v-model="country" :list="countryArray" />

      <span class="second-title">No of Followers</span>

      <BaseSelect class="select" v-model="follow" :list="followers" />
    </div>

    <div class="alexa-ranking">
      <span class="second-title">Language</span>

      <BaseSelect class="select" v-model="country" :list="countryArray" />
    </div>
  </div>

  <span class="second-title">Types of Tweets</span>

  <div class="checkbox-wrapper">
    <BaseCheckbox v-for="(item, index) in tweets" :key="index" :value="item">
      Test
    </BaseCheckbox>
  </div>

  <span class="second-title">Sentiment</span>

  <div class="radio-wrapper">
    <BaseRadio
      v-for="(item, index) in sentiments"
      :key="index"
      :checked="item"
      class="radio-btn"
    >
      <template #default>
        <div class="btn-checked"><CheckRadioIcon class="checked-icon" /></div>
        {{ item.value }}
      </template>
    </BaseRadio>
  </div>
</template>

<script>
import BaseRadio from '@/components/BaseRadio'
import CheckRadioIcon from '@/components/icons/CheckIcon'
import BaseSelect from '@/components/BaseSelect'
import BaseCheckbox from '@/components/BaseCheckbox'

export default {
  name: 'SocialType',
  components: {
    BaseCheckbox,
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
      country: null,
      follow: null,
      countryArray: [1, 2],
      tweets: [1, 2],
      followers: [1, 2],
    }
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
  color: var(--primary-text-color);
}

.alexa-ranking {
  flex: 1;

  &:first-child {
    margin-right: 16px;
  }
}

.radio-btn {
  display: flex;

  margin-right: 25px;

  color: var(--primary-text-color);

  cursor: pointer;
}

.btn-checked {
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

.checked-icon {
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

.radio-wrapper > .selected .btn-checked {
  border: none;
  background: var(--button-primary-color);
}

.radio-wrapper > .selected .checked-icon {
  display: flex;
}
</style>
