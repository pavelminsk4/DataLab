<template>
  <div v-if="allCountries" class="filters-wrapper">
    <div class="filters-settings-items">
      <div class="items-container">
        <span class="second-title">Country</span>

        <BaseSelect
          v-model="country"
          :name="'country'"
          :placeholder="'Select country'"
          :list="allCountries"
          @select-option="selectCountry"
          class="select"
        />
      </div>

      <div class="items-container">
        <span class="second-title">Author</span>

        <BaseSelect
          :name="'author'"
          :placeholder="'Select author'"
          class="select"
        />
      </div>
    </div>

    <div class="filters-settings-items">
      <div class="items-container">
        <span class="second-title">Language</span>

        <BaseSelect
          v-model="language"
          :name="'language'"
          :placeholder="'Select language'"
          :list="allLanguages"
          @select-option="selectLanguage"
          class="select"
        />
      </div>

      <div class="items-container">
        <span class="second-title">Source</span>

        <BaseSelect
          v-model="source"
          :name="'source'"
          :placeholder="'Select Source'"
          :list="allSources"
          @select-option="selectSource"
          class="select"
        />
      </div>
    </div>
  </div>
  <span class="second-title">Sentiment</span>

  <div class="radio-wrapper">
    <BaseRadio
      v-for="(item, index) in sentiments"
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
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseRadio from '@/components/BaseRadio'
import BaseSelect from '@/components/BaseSelect'

import CheckRadioIcon from '@/components/icons/CheckIcon'

export default {
  name: 'OnlineType',
  components: {
    BaseRadio,
    BaseSelect,
    CheckRadioIcon,
  },
  data() {
    return {
      sentiments: ['Negative', 'Neutral', 'Positive'],
      selectedValue: '',
      country: '',
      language: '',
      source: '',
    }
  },
  created() {
    if (!this.countries.length) {
      this[action.GET_COUNTRIES]()
    }

    if (!this.languages.length) {
      this[action.GET_LANGUAGES]()
    }

    if (!this.sources.length) {
      this[action.GET_SOURCES]()
    }
  },
  computed: {
    ...mapGetters({
      countries: get.COUNTRIES,
      languages: get.LANGUAGES,
      sources: get.SOURCES,
    }),
    allCountries() {
      return this.countries.map((el) => el.name)
    },
    allLanguages() {
      return this.languages.map((el) => el.language)
    },
    allSources() {
      return this.sources.map((el) => el.source1)
    },
  },
  methods: {
    ...mapActions([
      action.GET_COUNTRIES,
      action.GET_LANGUAGES,
      action.GET_SOURCES,
      action.UPDATE_ADDITIONAL_FILTERS,
    ]),
    changeValue(newValue) {
      this.selectedValue = newValue
      this[action.UPDATE_ADDITIONAL_FILTERS]({
        sentiment: this.selectedValue.toLocaleLowerCase(),
      })
    },
    selectCountry(val) {
      try {
        if (val === 'Reject selection') {
          this.country = []
        } else {
          this.country = val
        }
        this[action.UPDATE_ADDITIONAL_FILTERS]({country: this.country})
      } catch (e) {
        console.log(e)
      }
    },
    selectLanguage(val) {
      try {
        if (val === 'Reject selection') {
          this.language = []
        } else {
          this.language = val
        }
        this[action.UPDATE_ADDITIONAL_FILTERS]({language: this.language})
      } catch (e) {
        console.log(e)
      }
    },
    selectSource(val) {
      try {
        if (val === 'Reject selection') {
          this.source = []
        } else {
          this.source = val
        }
        this[action.UPDATE_ADDITIONAL_FILTERS]({source: this.source})
      } catch (e) {
        console.log(e)
      }
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
