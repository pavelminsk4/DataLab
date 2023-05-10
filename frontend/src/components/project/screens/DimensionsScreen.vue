<template>
  <div class="dimensions-wrapper">
    <FilterChips
      v-if="chipsItems.length"
      :items="chipsItems"
      class="chips"
      @clear-all="clearAll"
      @remove-item="removeChipsItem"
    />
    <div class="title">Author</div>

    <SelectWithCheckboxes
      v-model="author"
      name="Authors"
      placeholder="Enter the author"
      :list="dimensionsList.authors"
      :is-search="true"
      :selected-checkboxes="selectedAuthorsProxy"
      @get-selected-items="getValuesList"
      class="select"
    />

    <div class="title">Country</div>

    <SelectWithCheckboxes
      v-model="country"
      name="Countries"
      placeholder="Enter the country"
      :list="dimensionsList.countries"
      :is-search="true"
      :selected-checkboxes="selectedCountriesProxy"
      @get-selected-items="getValuesList"
      class="select"
    />

    <div class="title">Language</div>

    <SelectWithCheckboxes
      v-model="language"
      name="Languages"
      placeholder="Enter the language"
      :list="dimensionsList.languages"
      :is-search="true"
      :selected-checkboxes="selectedLanguagesProxy"
      @get-selected-items="getValuesList"
      class="select"
    />

    <div v-if="moduleName === 'Online'" class="title">Source</div>

    <SelectWithCheckboxes
      v-if="moduleName === 'Online'"
      v-model="source"
      name="Sources"
      placeholder="Enter the source"
      :list="dimensionsList.sources"
      :is-search="true"
      :selected-checkboxes="selectedSourcesProxy"
      @get-selected-items="getValuesList"
      class="select"
    />

    <div class="title">Sentiment</div>

    <div class="sentiments">
      <BaseCheckbox
        v-for="(item, index) in sentiments"
        :key="item + index"
        v-model="selectedSentimentsProxy"
        :id="item"
        :has-icon="false"
        :class="['item', isCheckedElement(item) && `${item}-item`]"
      >
        {{ capitalizeFirstLetter(item) }}
      </BaseCheckbox>
    </div>
  </div>
</template>

<script>
import {action, get} from '@store/constants'
import {action as actionSocial} from '@store/constants'
import {mapActions, mapGetters, createNamespacedHelpers} from 'vuex'
import {capitalizeFirstLetter} from '@/lib/utilities'

import BaseCheckbox from '@/components/BaseCheckbox2'
import SelectWithCheckboxes from '@/components/SelectWithCheckboxes'
import FilterChips from '@/components/FilterChips'

const {mapActions: mapSocialActions} = createNamespacedHelpers('social')

export default {
  name: 'DimensionsScreen',
  components: {
    BaseCheckbox,
    SelectWithCheckboxes,
    FilterChips,
  },
  props: {
    moduleName: {type: String, required: true},
    projectId: {type: [String, Number], required: false},
    authorsDimensions: {type: Array, required: false},
    countriesDimensions: {type: Array, required: false},
    languagesDimensions: {type: Array, required: false},
    sourcesDimensions: {type: Array, required: false},
    sentimentsDimensions: {type: Array, required: false},
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
      dimensionAuthors: get.DIMENSION_AUTHORS,
      dimensionCounties: get.DIMENSION_COUNTRIES,
      dimensionLanguages: get.DIMENSION_LANGUAGES,
      dimensionSources: get.DIMENSION_SOURCES,
      selectedDimensions: get.SELECTED_DIMENSIONS,
      dimensionsListOnline: get.DIMENSIONS_LIST,
      dimensionsListSocial: get.SOCIAL_DIMENSIONS_LIST,
    }),
    selectedAuthorsProxy: {
      get() {
        return this.authors || this.authorsDimensions || []
      },
      set(val) {
        this.authors = val
        this.updateSelectedDimensions()
      },
    },
    selectedCountriesProxy: {
      get() {
        return this.countries || this.countriesDimensions || []
      },
      set(val) {
        this.countries = val
        this.updateSelectedDimensions()
      },
    },
    selectedLanguagesProxy: {
      get() {
        return this.languages || this.languagesDimensions || []
      },
      set(val) {
        this.languages = val
        this.updateSelectedDimensions()
      },
    },
    selectedSourcesProxy: {
      get() {
        return this.sources || this.sourcesDimensions || []
      },
      set(val) {
        this.sources = val
        this.updateSelectedDimensions()
      },
    },
    selectedSentimentsProxy: {
      get() {
        return this.selectedSentiments || this.sentimentsDimensions || []
      },
      set(val) {
        this.selectedSentiments = val
        this.updateSelectedDimensions()
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
      this[action.GET_DIMENSIONS_OPTIONS](this.projectId)
    }

    if (this.moduleName === 'Social') {
      this[actionSocial.GET_SOCIAL_DIMENSIONS_OPTIONS](this.projectId)
    }
  },
  methods: {
    ...mapSocialActions([actionSocial.GET_SOCIAL_DIMENSIONS_OPTIONS]),
    ...mapActions([
      action.UPDATE_PROJECT,
      action.GET_WORKSPACES,
      action.GET_DIMENSIONS_OPTIONS,
      action.GET_SELECTED_DIMENSIONS,
    ]),
    capitalizeFirstLetter,
    updateSelectedDimensions() {
      this[action.GET_SELECTED_DIMENSIONS]({
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

      this.updateSelectedDimensions()
    },
    async clearAll() {
      this.selectedLanguagesProxy = []
      this.selectedCountriesProxy = []
      this.selectedSourcesProxy = []
      this.selectedSentimentsProxy = []
      this.selectedAuthorsProxy = []

      await this.updateSelectedDimensions()
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
