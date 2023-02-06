<template>
  <BaseModal
    v-if="authorsList"
    modal-frame-style="width: 40vw; max-height: 80vh;"
    title="Widgets Dimensions"
  >
    <div class="title">Author</div>

    <SelectWithCheckboxes
      v-model="author"
      name="author"
      placeholder="Enter the author"
      :list="authorsList"
      :is-search="true"
      :selected-checkboxes="currentProject.author_dimensions"
      @get-selected-items="getAuthorsList"
      class="select"
    />

    <div class="title">Country</div>

    <SelectWithCheckboxes
      v-model="country"
      name="country"
      placeholder="Enter the country"
      :list="countriesList"
      :is-search="true"
      :selected-checkboxes="currentProject.country_dimensions"
      @get-selected-items="getCountriesList"
      class="select"
    />

    <div class="title">Language</div>

    <SelectWithCheckboxes
      v-model="language"
      name="language"
      placeholder="Enter the language"
      :list="languagesList"
      :is-search="true"
      :selected-checkboxes="currentProject.language_dimensions"
      @get-selected-items="getLanguagesList"
      class="select"
    />

    <div class="title">Source</div>

    <SelectWithCheckboxes
      v-model="source"
      name="source"
      placeholder="Enter the source"
      :list="sourcesList"
      :is-search="true"
      :selected-checkboxes="currentProject.source_dimensions"
      @get-selected-items="getSourcesList"
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

    <BaseButton class="button" @click="saveChanges">Save</BaseButton>
  </BaseModal>
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'
import {capitalizeFirstLetter} from '@/lib/utilities'

import BaseModal from '@/components/modals/BaseModal'
import BaseButton from '@/components/buttons/BaseButton'
import BaseCheckbox from '@/components/BaseCheckbox'
import SelectWithCheckboxes from '@/components/SelectWithCheckboxes'

export default {
  name: 'AllDimensionsModal',
  components: {
    SelectWithCheckboxes,
    BaseCheckbox,
    BaseButton,
    BaseModal,
  },
  props: {
    projectId: {
      type: [String, Number],
      required: false,
    },
    currentProject: {
      type: [Array, Object],
      required: false,
    },
  },
  data() {
    return {
      author: '',
      country: '',
      language: '',
      source: '',
      authors: [],
      countries: [],
      languages: [],
      sources: [],
      sentiments: ['neutral', 'negative', 'positive'],
      selectedSentiments: [],
    }
  },
  created() {
    this[action.GET_DIMENSION_AUTHORS](this.projectId)
    this[action.GET_DIMENSION_COUNTRIES](this.projectId)
    this[action.GET_DIMENSION_LANGUAGES](this.projectId)
    this[action.GET_DIMENSION_SOURCES](this.projectId)
  },
  computed: {
    ...mapGetters({
      dimensionAuthors: get.DIMENSION_AUTHORS,
      dimensionCounties: get.DIMENSION_COUNTRIES,
      dimensionLanguages: get.DIMENSION_LANGUAGES,
      dimensionSources: get.DIMENSION_SOURCES,
    }),
    authorsList() {
      return this.dimensionAuthors?.map((el) => el.entry_author)
    },
    countriesList() {
      return this.dimensionCounties?.map((el) => el.feedlink__country)
    },
    languagesList() {
      return this.dimensionLanguages?.map((el) => el.feed_language__language)
    },
    sourcesList() {
      return this.dimensionSources?.map((el) => el.feedlink__source1)
    },
    selectedSentimentsProxy: {
      get() {
        return (
          this.currentProject.sentiment_dimensions || this.selectedSentiments
        )
      },
      set(val) {
        this.selectedSentiments = val
      },
    },
  },
  methods: {
    ...mapActions([
      action.UPDATE_PROJECT,
      action.GET_DIMENSION_AUTHORS,
      action.GET_DIMENSION_COUNTRIES,
      action.GET_DIMENSION_LANGUAGES,
      action.GET_DIMENSION_SOURCES,
    ]),
    capitalizeFirstLetter,
    onChange(args) {
      const {id, checked} = args
      if (checked) {
        this.selectedSentimentsProxy.push(id)
      } else {
        let element = this.selectedSentimentsProxy.indexOf(id)
        this.removeSelectedFilter(element, id)
      }
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
            author_dimensions: this.authors,
            country_dimensions: this.countries,
            language_dimensions: this.languages,
            source_dimensions: this.sources,
          },
        })
      } catch (e) {
        console.log(e)
      }
    },
    getAuthorsList(items) {
      this.authors = items
    },
    getCountriesList(items) {
      this.countries = items
    },
    getLanguagesList(items) {
      this.languages = items
    },
    getSourcesList(items) {
      this.sources = items
    },
  },
}
</script>

<style lang="scss" scoped>
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

.button {
  width: 59px;
  margin-top: 32px;
  margin-left: auto;
}
</style>
