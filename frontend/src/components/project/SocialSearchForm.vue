<template>
  <div class="filters-wrapper">
    <template v-for="{name, listName} in searchFields" :key="name">
      <CustomText tag="span" :text="name" class="second-title" />
      
      <FilterChips
        v-if="selectedFilters(name)?.length"
        :items="selectedFilters(name)"
        class="chips"
        @clear-all="clearAll(name)"
        @remove-item="removeChipsItem($event, name)"
      />

      <SelectWithCheckboxes
        v-model="search[name]"
        :name="name"
        :is-search="true"
        :placeholder="`Enter the ${name}`"
        :list="searchLists[listName]"
        :selected-checkboxes="selectedFilters(name)"
        @update-list="updateList(searchLists[listName], name)"
        @update:modelValue="getFilterList($event, name)"
        @get-selected-items="updateAdditionalFilters"
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
import FilterChips from '@components/FilterChips'
import BaseCheckbox from '@components/BaseCheckbox'
import BaseRadio from '@components/BaseRadio'
import PositiveIcon from '@components/icons/PositiveIcon'
import NegativeIcon from '@components/icons/NegativeIcon'
import NeutralIcon from '@components/icons/NeutralIcon'
import SelectWithCheckboxes from '@components/SelectWithCheckboxes'
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
    PositiveIcon,
    NegativeIcon,
    NeutralIcon,
    BaseCheckbox,
    CustomText,
    FilterChips,
    ProjectCalendar,
    SelectWithCheckboxes,
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
        author: '',
      },
      numItemsInList: {
        country: 20,
        language: 20,
        author: 20,
      },
    }
  },
  computed: {
    ...mapSocialGetters({
      searchLists: get.SEARCH_LISTS,
    }),
    ...mapGetters({
      keywords: get.KEYWORDS,
      additionalFilters: get.ADDITIONAL_FILTERS,
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
  async created() {
    this.searchFields = SEARCH_FIELDS

    await this.searchFields.forEach(({name}) => this.getFilterList('', name))

    await this[action.UPDATE_ADDITIONAL_FILTERS]({
      country: this.currentProject?.country_filter,
      language: this.currentProject?.language_filter,
      author: this.currentProject?.author_filter,
      sentiment: this.currentProject?.sentiment_filter,
    })
  },
  methods: {
    ...mapActions([action.UPDATE_ADDITIONAL_FILTERS]),
    ...mapSocialActions([
      action.GET_AUTHORS,
      action.GET_COUNTRIES,
      action.GET_LANGUAGES,
    ]),

    selectedFilters(name) {
      return this.additionalFilters[name] || []
    },

    isSelectedItem(item) {
      return this.selectedValueProxy.some((el) => item === el)
    },

    async updateList(list, name) {
      if (list.length < 20) return
      this.numItemsInList[name] = this.numItemsInList[name] + 20
      await this.getFilterList(this.search[name], name)
    },

    async updateAdditionalFilters(values, name) {
      await this[action.UPDATE_ADDITIONAL_FILTERS]({[name]: values})
    },

    async getFilterList(searchValue, name) {
      switch (name) {
        case 'country':
          return await this[action.GET_COUNTRIES]({
            word: searchValue,
            limit: this.numItemsInList.country,
          })
        case 'language':
          return await this[action.GET_LANGUAGES]({
            word: searchValue,
            limit: this.numItemsInList.language,
          })
        case 'author':
          return await this[action.GET_AUTHORS]({
            word: searchValue,
            limit: this.numItemsInList.author,
          })
      }
    },

    async removeChipsItem(item, name) {
      const newCollection = this.additionalFilters[name].filter(
        (element) => element !== item
      )
      await this[action.UPDATE_ADDITIONAL_FILTERS]({[name]: newCollection})
    },

    async clearAll(name) {
      await this[action.UPDATE_ADDITIONAL_FILTERS]({[name]: []})
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

.chips {
  margin: 10px 0 15px;
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
