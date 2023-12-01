<template>
  <div class="dimensions-wrapper">
    <FilterChips
      v-if="chipsItems.length"
      :items="chipsItems"
      class="chips"
      @clear-all="clearAll"
      @remove-item="removeChipsItem"
    />
    <CustomText text="Author" class="title" />

    <SelectWithCheckboxes
      v-model="author"
      name="Authors"
      placeholder="Enter the author"
      :list="dimensionsList.authors"
      :is-search="true"
      :selected-checkboxes="selectedAuthorsProxy"
      class="select"
      @get-selected-items="getValuesList"
    />

    <CustomText text="Country" class="title" />

    <SelectWithCheckboxes
      v-model="country"
      name="Countries"
      placeholder="Enter the country"
      :list="dimensionsList.countries"
      :is-search="true"
      :selected-checkboxes="selectedCountriesProxy"
      class="select"
      @get-selected-items="getValuesList"
    />

    <CustomText text="Language" class="title" />

    <SelectWithCheckboxes
      v-model="language"
      name="Languages"
      placeholder="Enter the language"
      :list="dimensionsList.languages"
      :is-search="true"
      :selected-checkboxes="selectedLanguagesProxy"
      class="select"
      @get-selected-items="getValuesList"
    />

    <CustomText v-if="moduleName === 'Online'" text="Source" class="title" />

    <SelectWithCheckboxes
      v-if="moduleName === 'Online'"
      v-model="source"
      name="Sources"
      placeholder="Enter the source"
      :list="dimensionsList.sources"
      :is-search="true"
      :selected-checkboxes="selectedSourcesProxy"
      class="select"
      @get-selected-items="getValuesList"
    />

    <CustomText text="Sentiment" class="title" />

    <div class="sentiments">
      <BaseCheckbox
        v-for="(item, index) in sentiments"
        :key="item + index"
        v-model="selectedSentimentsProxy"
        :id="item"
        :has-icon="false"
        :class="['item', isCheckedElement(item) && `${item}-item`]"
      >
        <CustomText tag="span" :text="capitalizeFirstLetter(item)" />
      </BaseCheckbox>
    </div>
  </div>
</template>

<script>
import {action, get} from '@store/constants'
import {action as actionSocial, action as actionOnline} from '@store/constants'
import {mapActions, mapGetters, createNamespacedHelpers} from 'vuex'
import {capitalizeFirstLetter} from '@lib/utilities'

import CustomText from '@components/CustomText'
import BaseCheckbox from '@components/BaseCheckbox'
import SelectWithCheckboxes from '@components/SelectWithCheckboxes'
import FilterChips from '@components/FilterChips'

const {mapActions: mapOnlineActions} = createNamespacedHelpers('online')
const {mapActions: mapSocialActions} = createNamespacedHelpers('social')

export default {
  name: 'FiltersScreen',
  components: {
    BaseCheckbox,
    SelectWithCheckboxes,
    FilterChips,
    CustomText,
  },
  props: {
    moduleName: {type: String, required: true},
    projectId: {type: [String, Number], required: false},
    authorsFilters: {type: Array, required: false},
    countriesFilters: {type: Array, required: false},
    languagesFilters: {type: Array, required: false},
    sourcesFilters: {type: Array, required: false},
    sentimentsFilters: {type: Array, required: false},
  },
  data() {
    return {
      author: '',
      country: '',
      language: '',
      source: '',
      authors: null,
      countries: null,
      languages: null,
      sources: null,
      selectedSentiments: null,
    }
  },
  computed: {
    ...mapGetters({
      dimensionAuthors: get.FILTERS_AUTHORS,
      dimensionCounties: get.FILTERS_COUNTRIES,
      dimensionLanguages: get.FILTERS_LANGUAGES,
      dimensionSources: get.FILTERS_SOURCES,
      selectedFilters: get.SELECTED_FILTERS,
      dimensionsListOnline: get.DIMENSIONS_LIST,
      dimensionsListSocial: get.SOCIAL_FILTERS_LIST,
    }),
    selectedAuthorsProxy: {
      get() {
        return this.authors || this.authorsFilters || []
      },
      set(val) {
        this.authors = val
        this.updateSelectedFilters()
      },
    },
    selectedCountriesProxy: {
      get() {
        return this.countries || this.countriesFilters || []
      },
      set(val) {
        this.countries = val
        this.updateSelectedFilters()
      },
    },
    selectedLanguagesProxy: {
      get() {
        return this.languages || this.languagesFilters || []
      },
      set(val) {
        this.languages = val
        this.updateSelectedFilters()
      },
    },
    selectedSourcesProxy: {
      get() {
        return this.sources || this.sourcesFilters || []
      },
      set(val) {
        this.sources = val
        this.updateSelectedFilters()
      },
    },
    selectedSentimentsProxy: {
      get() {
        return this.selectedSentiments || this.sentimentsFilters || []
      },
      set(val) {
        this.selectedSentiments = val
        this.updateSelectedFilters()
      },
    },
    chipsItems() {
      return [
        ...this.selectedAuthorsProxy,
        ...this.selectedCountriesProxy,
        ...this.selectedLanguagesProxy,
        ...this.selectedSourcesProxy,
        ...this.selectedSentimentsProxy,
      ]
    },
    dimensionsList() {
      if (this.moduleName === 'Online') return this.dimensionsListOnline

      if (this.moduleName === 'Social') return this.dimensionsListSocial

      return []
    },
  },
  created() {
    this.sentiments = ['neutral', 'negative', 'positive']

    if (this.moduleName === 'Online') {
      this[actionOnline.GET_FILTERS_OPTIONS](this.projectId)
    }

    if (this.moduleName === 'Social') {
      this[actionSocial.GET_SOCIAL_FILTERS_OPTIONS](this.projectId)
    }
  },
  methods: {
    ...mapSocialActions([actionSocial.GET_SOCIAL_FILTERS_OPTIONS]),
    ...mapOnlineActions([actionOnline.GET_FILTERS_OPTIONS]),
    ...mapActions([
      action.UPDATE_PROJECT,
      action.GET_WORKSPACES,
      action.GET_SELECTED_FILTERS,
    ]),
    capitalizeFirstLetter,
    updateSelectedFilters() {
      this[action.GET_SELECTED_FILTERS]({
        authors: this.selectedAuthorsProxy,
        countries: this.selectedCountriesProxy,
        languages: this.selectedLanguagesProxy,
        sources: this.selectedSourcesProxy,
        sentiments: this.selectedSentimentsProxy,
      })
    },
    isCheckedElement(item) {
      return this.selectedSentimentsProxy?.some((el) => el === item)
    },
    getValuesList(items, name) {
      this[`selected${name}Proxy`] = items
    },
    removeChipsItem(item) {
      this.selectedAuthorsProxy.find((el, index) => {
        return el === item ? this.selectedAuthorsProxy.splice(index, 1) : null
      })
      this.selectedSourcesProxy.find((el, index) => {
        return el === item ? this.selectedSourcesProxy.splice(index, 1) : null
      })
      this.selectedSentimentsProxy.find((el, index) => {
        return el === item
          ? this.selectedSentimentsProxy.splice(index, 1)
          : null
      })
      this.selectedCountriesProxy.find((el, index) => {
        return el === item ? this.selectedCountriesProxy.splice(index, 1) : null
      })
      this.selectedLanguagesProxy.find((el, index) => {
        return el === item ? this.selectedLanguagesProxy.splice(index, 1) : null
      })

      this.updateSelectedFilters()
    },
    async clearAll() {
      this.selectedLanguagesProxy = []
      this.selectedCountriesProxy = []
      this.selectedSourcesProxy = []
      this.selectedSentimentsProxy = []
      this.selectedAuthorsProxy = []

      await this.updateSelectedFilters()
    },
  },
}
</script>

<style lang="scss" scoped>
.dimensions-wrapper {
  display: flex;
  flex-direction: column;
}

.chips {
  margin-bottom: 36px;
}

.title {
  margin-bottom: 4px;

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--typography-title-color);
}

.select {
  margin-bottom: 20px;
}

.sentiments {
  display: flex;
  gap: 8px;

  .item {
    padding: 6px 12px;

    border: 1px solid var(--border-color);
    border-radius: 12px;

    cursor: pointer;

    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 20px;
    color: var(--typography-title-color);
  }

  .neutral-item {
    border: 1px solid var(--neutral-primary-color);

    color: var(--neutral-primary-color);
  }

  .negative-item {
    border: 1px solid var(--negative-primary-color);

    color: var(--negative-primary-color);
  }

  .positive-item {
    border: 1px solid var(--positive-primary-color);

    color: var(--positive-primary-color);
  }
}
</style>
