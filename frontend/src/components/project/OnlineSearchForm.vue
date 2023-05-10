<template>
  <div class="filters-wrapper">
    <span class="second-title">Country</span>

    <BaseSearchField
      v-model="country"
      name="country"
      :placeholder="'Enter the country'"
      :list="countries"
      :is-search="true"
      :current-value="country"
      :is-reject-selection="false"
      @select-option="selectItem"
      @update:modelValue="getResult"
      class="select"
    />

    <span class="second-title">Author</span>

    <BaseSearchField
      v-model="author"
      name="author"
      :list="authors"
      :placeholder="'Enter the author'"
      :current-value="author"
      :is-search="true"
      :is-reject-selection="false"
      :is-clear-selected-value="clearValue"
      @select-option="selectItem"
      @update:modelValue="getResult"
      class="select"
    />

    <span class="second-title">Language</span>

    <BaseSearchField
      v-model="language"
      name="language"
      placeholder="Enter the language"
      :list="languages"
      :is-search="true"
      :current-value="language"
      :is-reject-selection="false"
      :is-clear-selected-value="clearValue"
      @select-option="selectItem"
      @update:modelValue="getResult"
      class="select"
    />

    <span class="second-title">Source</span>

    <BaseSearchField
      v-model="source"
      name="source"
      placeholder="Enter the source"
      :list="sources"
      :is-search="true"
      :current-value="source"
      :is-reject-selection="false"
      :is-clear-selected-value="clearValue"
      @select-option="selectItem"
      @update:modelValue="getResult"
      class="select"
    />
  </div>

  <CommonCalendar />

  <span class="second-title">Sentiment</span>

  <div class="radio-wrapper">
    <BaseRadio
      v-for="(item, index) in sentiments"
      :key="item + index"
      v-model="selectedValueProxy"
      :checked="item"
      :id="item + index"
      :value="item"
      :label="item"
      class="radio-btn"
    >
      <component
        :is="item + 'Icon'"
        :class="['radio-icon', selectedValueProxy === item && item + '-item']"
      />
    </BaseRadio>

    <BaseRadio
      v-model="selectedValueProxy"
      checked="All sentiments"
      id="allSentiments"
      value="All sentiments"
      label="All sentiments"
      class="radio-btn"
    />
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseRadio from '@/components/BaseRadio'
import BaseSearchField from '@/components/BaseSearchField'
import PositiveIcon from '@/components/icons/PositiveIcon'
import NegativeIcon from '@/components/icons/NegativeIcon'
import NeutralIcon from '@/components/icons/NeutralIcon'
import CommonCalendar from '@/components/datepicker/CommonCalendar'

export default {
  name: 'OnlineSearchForm',
  components: {
    BaseRadio,
    BaseSearchField,
    PositiveIcon,
    NegativeIcon,
    NeutralIcon,
    CommonCalendar,
  },
  props: {
    currentProject: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      sentiments: ['Negative', 'Neutral', 'Positive'],
      selectedValue: '',
      clearValue: false,
      country: '',
      language: '',
      source: '',
      author: '',
    }
  },
  computed: {
    ...mapGetters({
      countries: get.COUNTRIES,
      languages: get.LANGUAGES,
      sources: get.SOURCES,
      authors: get.AUTHORS,
      keywords: get.KEYWORDS,
    }),
    selectedValueProxy: {
      get() {
        return (
          this.selectedValue ||
          this.capitalizeFirstLetter(this.currentProject.sentiment_filter)
        )
      },
      set(sentiment) {
        this.selectedValue = sentiment
        if (sentiment === 'All sentiments') {
          this[action.UPDATE_ADDITIONAL_FILTERS]({sentiment: null})
        } else {
          this[action.UPDATE_ADDITIONAL_FILTERS]({
            sentiment: this.selectedValue?.toLocaleLowerCase(),
          })
        }
      },
    },
  },
  created() {
    this.country = this.currentProject?.country_filter || ''
    this.language = this.currentProject?.language_filter || ''
    this.source = this.currentProject?.source_filter || ''
    this.author = this.currentProject?.author_filter || ''

    this[action.UPDATE_ADDITIONAL_FILTERS]({
      country: this.currentProject.country_filter,
      language: this.currentProject.language_filter,
      source: this.currentProject.source_filter,
      author: this.currentProject.author_filter,
      sentiment: this.currentProject.sentiment_filter,
    })
  },
  watch: {
    async keywords() {
      if (!this.keywords.keywords?.length) {
        this.clearValue = true
        this.country = ''
        this.language = ''
        this.source = ''
        this.author = ''
        this.selectedValue = ''
      }
    },
  },
  methods: {
    ...mapActions([
      action.GET_SOURCES,
      action.GET_AUTHORS,
      action.GET_COUNTRIES,
      action.GET_LANGUAGES,
      action.UPDATE_ADDITIONAL_FILTERS,
    ]),
    selectItem(name, val) {
      try {
        this[name] = val
        if (val === 'Reject selection') {
          this[action.UPDATE_ADDITIONAL_FILTERS]({[name]: null})
        } else {
          this[action.UPDATE_ADDITIONAL_FILTERS]({[name]: val})
        }
      } catch (e) {
        console.log(e)
      }
    },

    capitalizeFirstLetter(string) {
      return string?.charAt(0)?.toUpperCase() + string?.slice(1)
    },

    getResult(searchValue, name) {
      try {
        this[name] = searchValue
        this[action.UPDATE_ADDITIONAL_FILTERS]({[name]: searchValue})

        switch (name) {
          case 'country':
            return this[action.GET_COUNTRIES](
              this.capitalizeFirstLetter(searchValue)
            )
          case 'language':
            return this[action.GET_LANGUAGES](
              this.capitalizeFirstLetter(searchValue)
            )
          case 'author':
            return this[action.GET_AUTHORS](searchValue)
          case 'source':
            return this[action.GET_SOURCES](searchValue)
        }
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

  margin-bottom: 20px;
}

.second-title {
  margin: 20px 0 4px;

  font-size: 14px;
  color: var(--typography-primary-color);
}

.radio-btn {
  display: flex;
  align-items: center;

  margin: 0 25px 8px 0;

  cursor: pointer;

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--typography-primary-color);
}

.radio-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  margin: 10px 0 25px;

  .radio-icon {
    margin-right: 4px;
  }
}

.neutral-item {
  color: var(--neutral-primary-color);
}

.negative-item {
  color: var(--negative-primary-color);
}

.positive-item {
  color: var(--positive-primary-color);
}

@media screen and (max-width: 1000px) {
  .filters {
    align-items: flex-end;
    flex-direction: column;
  }

  .search-result-card {
    margin: 0 0 10px 0;
  }
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
</style>
