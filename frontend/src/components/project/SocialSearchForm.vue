<template>
  <div class="filters-wrapper">
    <template v-for="{name, listName} in searchFields" :key="name">
      <CustomText tag="span" :text="name" class="second-title" />

      <BaseSearchField
        v-model="search[name]"
        :name="name"
        :placeholder="`Enter the ${name}`"
        :list="searchLists[listName]"
        :is-search="true"
        :current-value="search[name]"
        :is-reject-selection="false"
        :is-clear-selected-value="clearValue"
        :is-loading="isLoadingFilters[name]"
        class="select"
        @update:modelValue="getResult"
        @select-option="selectItem"
      />
    </template>
  </div>

  <ProjectCalendar
    :is-range="isCurrentProjectCreated"
    :start-date="currentProject.start_search_date"
    class="date-picker"
  />

  <CustomText tag="span" text="Sentiment" class="second-title" />

  <div class="sentiments-wrapper">
    <BaseCheckbox
      v-for="(item, index) in sentiments"
      :key="item + index"
      v-model="selectedValueProxy"
      :value="item"
      :has-icon="false"
      :id="item"
      :class="['checkbox', isSelectedItem(item) && 'active']"
    >
      <component
        :is="item + 'Icon'"
        :class="['sentiment-icon', isSelectedItem(item) && item + '-item']"
      />
      <CustomText :text="item" />
    </BaseCheckbox>
  </div>
</template>

<script>
import {mapActions, mapGetters, createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'
import {isAllFieldsEmpty} from '@lib/utilities'

import CustomText from '@components/CustomText'
import BaseCheckbox from '@components/BaseCheckbox2'
import BaseRadio from '@components/BaseRadio'
import BaseSearchField from '@components/BaseSearchField'
import PositiveIcon from '@components/icons/PositiveIcon'
import NegativeIcon from '@components/icons/NegativeIcon'
import NeutralIcon from '@components/icons/NeutralIcon'
import ProjectCalendar from '@components/datepicker/ProjectCalendar'

const {mapActions: mapSocialActions, mapGetters: mapSocialGetters} =
  createNamespacedHelpers('social')

const SEARCH_FIELDS = [
  {
    name: 'country',
    listName: 'countries',
  },
  {
    name: 'author',
    listName: 'authors',
  },
  {
    name: 'language',
    listName: 'languages',
  },
]

export default {
  name: 'SocialSearchForm',
  inheritAttrs: false,
  components: {
    BaseRadio,
    BaseSearchField,
    PositiveIcon,
    NegativeIcon,
    NeutralIcon,
    BaseCheckbox,
    CustomText,
    ProjectCalendar,
  },
  props: {
    currentProject: {type: Object, required: true},
  },
  data() {
    return {
      sentiments: ['negative', 'neutral', 'positive'],
      selectedValue: null,
      clearValue: false,
      search: {
        country: '',
        language: '',
        source: '',
        author: '',
      },
      isLoadingFilters: {
        country: false,
        language: false,
        source: false,
        author: false,
      },
    }
  },
  computed: {
    ...mapSocialGetters({
      searchLists: get.SEARCH_LISTS,
    }),
    ...mapGetters({
      keywords: get.KEYWORDS,
    }),
    isCurrentProjectCreated() {
      return !isAllFieldsEmpty(this.currentProject)
    },
    selectedValueProxy: {
      get() {
        return this.selectedValue || this.currentProject?.sentiment_filter || []
      },
      set(value) {
        this.selectedValue = value
        this[action.UPDATE_ADDITIONAL_FILTERS]({
          sentiment: this.selectedValue,
        })
      },
    },
  },
  created() {
    this.searchFields = SEARCH_FIELDS
    this.search.country = this.currentProject?.country_filter || ''
    this.search.language = this.currentProject?.language_filter || ''
    this.search.source = this.currentProject?.source_filter || ''
    this.search.author = this.currentProject?.author_filter || ''

    this[action.UPDATE_ADDITIONAL_FILTERS]({
      country: this.currentProject?.country_filter,
      language: this.currentProject?.language_filter,
      source: this.currentProject?.source_filter,
      author: this.currentProject?.author_filter,
      sentiment: this.currentProject?.sentiment_filter,
    })
  },
  watch: {
    async keywords() {
      if (!this.keywords.keywords?.length) {
        this.clearValue = true
        this.search.country = ''
        this.search.language = ''
        this.search.source = ''
        this.search.author = ''
      }
    },
  },
  methods: {
    ...mapActions([
      action.GET_AUTHORS,
      action.GET_COUNTRIES,
      action.GET_LANGUAGES,
      action.UPDATE_ADDITIONAL_FILTERS,
    ]),
    ...mapSocialActions([
      action.GET_AUTHORS,
      action.GET_COUNTRIES,
      action.GET_LANGUAGES,
    ]),

    isSelectedItem(item) {
      return this.selectedValueProxy.some((el) => item === el)
    },

    selectItem(name, val) {
      try {
        this.search[name] = val
        if (val === '') {
          this[action.UPDATE_ADDITIONAL_FILTERS]({[name]: null})
        } else {
          this[action.UPDATE_ADDITIONAL_FILTERS]({[name]: [val]})
        }
      } catch (e) {
        console.error(e)
      }
    },

    async getFilterList(searchValue, name) {
      this.isLoadingFilters[name] = true
      try {
        switch (name) {
          case 'country':
            return await this[action.GET_COUNTRIES](searchValue)
          case 'language':
            return await this[action.GET_LANGUAGES](searchValue)
          case 'author':
            return await this[action.GET_AUTHORS](searchValue)
        }
      } finally {
        this.isLoadingFilters[name] = false
      }
    },
    getResult(searchValue, name) {
      try {
        this[name] = searchValue
        this[action.UPDATE_ADDITIONAL_FILTERS]({[name]: searchValue})

        this.getFilterList(searchValue, name)
      } catch (e) {
        console.error(e)
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

  width: 408px;

  margin-bottom: 20px;
}

.date-picker {
  width: 408px;
  margin-bottom: 60px;
}

.second-title {
  margin: 20px 0 4px;

  text-transform: capitalize;
  font-size: 14px;
  color: var(--typography-primary-color);
}

.radio-btn {
  display: flex;
  align-items: center;

  margin: 0 0 8px 0;

  cursor: pointer;

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--typography-primary-color);
}

.sentiments-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  gap: 12px;

  width: 408px;
  margin: 10px 0 25px;

  .checkbox {
    display: flex;
    align-items: center;

    padding: 12px;

    border: 1px solid var(--border-color);
    border-radius: 10px;

    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 20px;
  }

  .active {
    background: #fcedf3;
    border: 1px solid var(--border-active-color);
  }
  .sentiment-icon {
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
