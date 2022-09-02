<template>
  <div class="mode-wrapper">
    <div class="mode-title mode-active">Simple mode</div>
    <div class="mode-title">Expert mode</div>
  </div>

  <div class="second-title">Define the main keywords (OR)</div>
  <BaseTag :is-main-field="true" />

  <div class="additional-key-words">
    <div class="additional-key-block">
      <div class="second-title">
        Add Additional keywords <br />
        (And)
      </div>
      <BaseTag class="additional-key" />
    </div>

    <div>
      <div class="second-title">
        Exclude Irrelevant keywords <br />
        (And Not)
      </div>
      <BaseTag
        class="additional-key"
        :placeholder="'Enter Keywords and Phrases seperated by comas'"
      />
    </div>
  </div>

  <div class="filters-title">Refine youre search with additional filters</div>

  <div class="filters-wrapper">
    <div class="alexa-ranking">
      <span class="second-title">Global Alexa Ranking</span>

      <div class="radio-wrapper">
        <BaseRadio
          v-for="(item, index) in alexaRanking"
          :key="index"
          :checked="item"
          :value="selectedValue"
          class="radio-btn"
          @change="changeValue(item)"
        >
          <template v-slot:default>
            <div class="not-check"><CheckRadioIcon /></div>
            {{ item.value }}
          </template>
        </BaseRadio>
      </div>

      <span class="second-title">Country</span>

      <BaseSelect class="select" v-model="country" :list="countryArray" />

      <span class="second-title">Language</span>

      <BaseSelect class="select" v-model="country" :list="countryArray" />
    </div>

    <div class="alexa-ranking">
      <span class="second-title">Countries Group</span>

      <div class="radio-wrapper">
        <BaseRadio
          v-for="(item, index) in alexaRanking"
          :key="index"
          :checked="item"
          :value="selectedValue"
          class="radio-btn"
          @change="changeValue(item)"
        >
          <template v-slot:default>
            <div class="not-check"><CheckRadioIcon /></div>
            {{ item.value }}
          </template>
        </BaseRadio>
      </div>

      <span class="second-title">Country</span>

      <BaseInput class="input" />

      <span class="second-title">Source</span>

      <BaseInput class="input" />
    </div>
  </div>
</template>

<script>
import BaseTag from '@components/BaseTag'
import BaseRadio from '@components/BaseRadio'
import CheckRadioIcon from '@components/icons/CheckRadioIcon'
import BaseSelect from '@components/BaseSelect'
import BaseInput from '@/components/BaseInput'

export default {
  name: 'OnlineType',
  components: {
    BaseInput,
    BaseSelect,
    CheckRadioIcon,
    BaseRadio,
    BaseTag,
  },
  data() {
    return {
      alexaRanking: [{value: '10%'}, {value: '20%'}, {value: '30%'}],
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
.mode-wrapper {
  display: flex;

  margin-bottom: 20px;

  border-bottom: 1px solid var(--input-border-color);
}

.mode-title {
  padding-bottom: 10px;

  font-size: 14px;
  color: rgba(255, 255, 255, 0.8);

  &:first-child {
    margin-right: 55px;
  }
}

.mode-active {
  border-bottom: 2px solid var(--primary-button-color);

  font-weight: 500;
  color: var(--primary-text-color);
}

.second-title {
  margin-bottom: 12px;

  font-size: 14px;
  color: var(--primary-text-color);
}

.filters-wrapper {
  display: flex;
  justify-content: space-between;
}

.additional-key-words {
  display: flex;

  margin: 26px 0 40px;
}

.additional-key-block {
  margin-right: 13px;
}

.additional-key {
  align-items: flex-start;
  flex-wrap: wrap;

  width: 250px;
  height: 110px;

  padding-top: 10px;
}

.filters-title {
  margin-bottom: 25px;

  font-weight: 600;
  font-size: 16px;
  color: var(--primary-text-color);
}

.alexa-ranking {
  width: 250px;
}

.radio-btn {
  display: flex;

  margin-right: 25px;

  color: var(--primary-text-color);
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
</style>
