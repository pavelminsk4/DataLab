<template>
  <div v-if="allCountries" class="filters-wrapper">
    <div class="filters-settings-items">
      <div class="items-container">
        <span class="second-title">Country {{ country }}</span>

        <v-select
          class="select"
          label="'Select'"
          v-model="country"
          :options="allCountries"
        />
      </div>

      <div class="items-container">
        <span class="second-title">City</span>

        <BaseInput class="input" />
      </div>
    </div>

    <div class="filters-settings-items">
      <div class="items-container">
        <span class="second-title">Language</span>

        <BaseSelect class="select" v-model="country" :list="countries" />
      </div>

      <div class="items-container">
        <span class="second-title">Source</span>

        <BaseInput class="input" />
      </div>
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
      <template #default>
        <div class="not-check"><CheckRadioIcon class="check-icon" /></div>
        {{ item.value }}
      </template>
    </BaseRadio>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseInput from '@/components/BaseInput'
import BaseRadio from '@/components/BaseRadio'
import BaseSelect from '@/components/BaseSelect'

import CheckRadioIcon from '@/components/icons/CheckIcon'

import vSelect from 'vue-select'
import 'vue-select/dist/vue-select.css'

export default {
  name: 'OnlineType',
  components: {
    BaseInput,
    BaseRadio,
    BaseSelect,
    CheckRadioIcon,
    vSelect,
  },
  data() {
    return {
      sentiments: [
        {value: 'Negative'},
        {value: 'Neutral'},
        {value: 'Positive'},
      ],
      selectedValue: '',
      country: '',
      countryArray: [1, 2],
    }
  },
  created() {
    this[action.GET_COUNTRIES]()
  },
  computed: {
    ...mapGetters({countries: get.COUNTRIES}),
    allCountries() {
      return this.countries.map((el) => el.name)
    },
  },
  methods: {
    ...mapActions([action.GET_COUNTRIES]),
    changeValue(newValue) {
      this.selectedValue = newValue
    },
    selectCountry(country, el) {
      console.log(this.country)
      this.country = el
    },
  },
}
</script>

<style lang="scss" scoped>
.filters-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.second-title {
  margin-bottom: 12px;

  font-size: 14px;
  color: var(--primary-text-color);
}

.filters-settings-items {
  display: flex;
  flex: 1;
}

.items-container {
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

@media screen and (max-width: 1050px) {
  .filters-settings-items {
    flex-direction: column;

    .items-container {
      margin: 0;
    }
  }
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
