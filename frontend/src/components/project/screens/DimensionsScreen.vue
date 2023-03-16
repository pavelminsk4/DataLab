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

    <div class="title">Source</div>

    <SelectWithCheckboxes
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
        :id="item"
        :has-icon="false"
        :model-value="isCheckedElement(item)"
        :class="['item', isCheckedElement(item) && `${item}-item`]"
        @change="onChange"
      >
        {{ capitalizeFirstLetter(item) }}
      </BaseCheckbox>
    </div>
  </div>
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'
import {capitalizeFirstLetter} from '@/lib/utilities'

import BaseCheckbox from '@/components/BaseCheckbox'
import SelectWithCheckboxes from '@/components/SelectWithCheckboxes'
import FilterChips from '@/components/FilterChips'

export default {
  name: 'DimensionsScreen',
  components: {
    BaseCheckbox,
    SelectWithCheckboxes,
    FilterChips,
  },
  props: {
    projectId: {
      type: [String, Number],
      required: false,
    },
    authorsDimensions: {
      type: Array,
      required: false,
    },
    countriesDimensions: {
      type: Array,
      required: false,
    },
    languagesDimensions: {
      type: Array,
      required: false,
    },
    sourcesDimensions: {
      type: Array,
      required: false,
    },
    sentimentsDimensions: {
      type: Array,
      required: false,
    },
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
      dimensionsList: get.DIMENSIONS_LIST,
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
  },
  created() {
    this.sentiments = ['neutral', 'negative', 'positive']

    this[action.GET_DIMENSIONS_OPTIONS](this.projectId)
  },
  methods: {
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
    onChange(args) {
      const {id, checked} = args
      if (checked) {
        this.selectedSentimentsProxy.push(id)
      } else {
        let element = this.selectedSentimentsProxy.indexOf(id)
        this.removeSelectedFilter(element, id)
      }

      this.updateSelectedDimensions()
    },
    removeSelectedFilter(index) {
      this.selectedSentimentsProxy.splice(index, 1)
    },
    isCheckedElement(item) {
      return this.selectedSentimentsProxy?.some((el) => el === item)
    },
    saveChanges() {
      try {
        this[action.UPDATE_PROJECT]({
          projectId: this.projectId,
          data: {
            sentiment_dimensions: this.selectedSentimentsProxy,
            author_dimensions: this.selectedAuthorsProxy,
            country_dimensions: this.selectedCountriesProxy,
            language_dimensions: this.selectedLanguagesProxy,
            source_dimensions: this.selectedSourcesProxy,
          },
        })

        this.$emit('update-search-results')
        this[action.GET_WORKSPACES]()
        this.$emit('close')
      } catch (e) {
        console.log(e)
      }
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
