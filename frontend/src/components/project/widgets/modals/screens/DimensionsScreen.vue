<template>
  <div v-if="dimensions?.length">
    <div class="tags-wrapper">
      <div v-for="(tag, index) in tags" :key="tag">
        <div v-if="tag.value" class="tag-value">
          {{ tag.value }}
          <DeleteTagButton class="delete" @click="removeTag(tag.name, index)" />
        </div>
      </div>
    </div>

    <section class="dimensions-list scroll">
      <DimensionsItem
        v-for="(item, index) in dimensions"
        :key="'dimension' + index"
        :title="item.dimension.title"
        :is-disabled="!isDisabled(item.dimension.id)"
        :select-list="selectedList(item.dimension.title)"
        :selected-value="selectedValue(item.dimension.title)"
        @update-widget-view="updateWidgetView"
      />
    </section>

    <BaseButton @click="saveChanges" class="button">Save</BaseButton>
  </div>

  <div v-else class="no-dimensions">Select the type of dimensions!</div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseButton from '@/components/buttons/BaseButton'
import DimensionsItem from '@/components/project/widgets/modals/screens/dimensions/DimensionsItem'
import DeleteTagButton from '@/components/icons/DeleteTagButton'

export default {
  name: 'DimensionsScreen',
  components: {DeleteTagButton, BaseButton, DimensionsItem},
  props: {
    activeDimensions: {
      type: [Array, Object],
      default: () => [],
    },
    projectId: {
      type: Number,
      required: true,
    },
    widgetAuthor: {
      type: String,
      required: false,
    },
    widgetLanguage: {
      type: String,
      required: false,
    },
    widgetCountry: {
      type: String,
      required: false,
    },
  },
  data() {
    return {
      author: '',
      country: '',
      language: '',
      tags: [
        {
          name: 'Author',
          value: this.author || this.widgetAuthor,
        },
        {
          name: 'Language',
          value: this.language || this.widgetLanguage,
        },
        {
          name: 'Country',
          value: this.country || this.widgetCountry,
        },
      ],
    }
  },
  created() {
    this[action.GET_SELECTED_DIMENSIONS](this.projectId)
    this[action.GET_DIMENSION_AUTHORS](this.projectId)
    this[action.GET_DIMENSION_LANGUAGES](this.projectId)
    this[action.GET_DIMENSION_COUNTRIES](this.projectId)
  },
  computed: {
    ...mapGetters({
      dimensions: get.SELECTED_DIMENSIONS,
      dimensionAuthors: get.DIMENSION_AUTHORS,
      dimensionLanguages: get.DIMENSION_LANGUAGES,
      dimensionCountries: get.DIMENSION_COUNTRIES,
    }),
    authorsList() {
      return this.dimensionAuthors?.map((el) => el.entry_author)
    },
    languageList() {
      return this.dimensionLanguages?.map((el) => el.feed_language__language)
    },
    countryList() {
      return this.dimensionCountries?.map((el) => el.feedlink__country)
    },
  },
  methods: {
    ...mapActions([
      action.GET_SELECTED_DIMENSIONS,
      action.GET_DIMENSION_AUTHORS,
      action.GET_DIMENSION_LANGUAGES,
      action.GET_DIMENSION_COUNTRIES,
      action.UPDATE_AVAILABLE_WIDGETS,
    ]),
    isDisabled(id) {
      return this.activeDimensions.linked_dimensions.some((el) => el === id)
    },
    updateWidgetView(name, val) {
      let indexAuthor = this.tags.findIndex((el) => el.name === 'Author')
      let indexLanguage = this.tags.findIndex((el) => el.name === 'Language')
      let indexCountry = this.tags.findIndex((el) => el.name === 'Country')

      switch (name) {
        case 'Author':
          this.author = val
          if (this.tags.find((el) => el.name === 'Author')) {
            this.tags.splice(indexAuthor, 1)
          }
          this.tags.push({
            name: 'Author',
            value: this.author,
          })
          break
        case 'Language':
          this.language = val
          if (this.tags.find((el) => el.name === 'Language')) {
            this.tags.splice(indexLanguage, 1)
          }
          this.tags.push({
            name: 'Language',
            value: this.language,
          })
          break
        case 'Country':
          this.country = val
          if (this.tags.find((el) => el.name === 'Country')) {
            this.tags.splice(indexCountry, 1)
          }
          this.tags.push({
            name: 'Country',
            value: this.country,
          })
          break
      }
    },
    selectedList(title) {
      switch (title) {
        case 'Author':
          return this.authorsList
        case 'Language':
          return this.languageList
        case 'Country':
          return this.countryList
      }
    },
    selectedValue(title) {
      switch (title) {
        case 'Author':
          if (this.author || this.author === '') {
            return this.authorsList?.find((el) => el === this.widgetAuthor)
          }
          this.author = null
          break
        case 'Language':
          if (this.language || this.language === '') {
            return this.languageList?.find((el) => el === this.widgetLanguage)
          }
          this.language = null
          break
        case 'Country':
          if (this.country || this.country === '') {
            return this.countryList?.find((el) => el === this.widgetCountry)
          }
          this.country = null
          break
      }
    },
    removeTag(name, index) {
      this.tags.splice(index, 1)
      switch (name) {
        case 'Author':
          this.author = null
          break
        case 'Language':
          this.language = null
          break
        case 'Country':
          this.country = null
          break
      }
    },
    saveChanges() {
      this.$emit(
        'save-dimensions-settings',
        this.author,
        this.language,
        this.country
      )
    },
  },
}
</script>

<style lang="scss" scoped>
.dimensions-list {
  overflow-y: auto;

  height: 360px;
  margin-top: 18px;
  padding: 16px 20px 40px;

  background: var(--secondary-bg-color);
  border: 1px solid var(--input-border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
  border-radius: 10px;
}

.button {
  height: 55px;
  margin-top: 25px;
}

.no-dimensions {
  margin: 10px 0;

  font-style: normal;
  font-size: 18px;
  font-weight: 400;
}

.tags-wrapper {
  display: flex;

  margin-top: 25px;

  .tag-value {
    display: flex;
    align-items: center;
    justify-content: center;
    white-space: nowrap;
    gap: 10px;

    margin-right: 10px;
    padding: 0 8px 0 10px;
    max-width: 100%;

    border-radius: 8px;

    color: var(--primary-text-color);
    background-color: var(--progress-line);
  }

  .delete {
    cursor: pointer;
  }
}
</style>
