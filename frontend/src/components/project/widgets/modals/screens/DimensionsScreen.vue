<template>
  <div v-if="dimensions?.length">
    <div class="tags-wrapper">
      <div v-for="(tag, index) in tags" :key="tag" class="tag-value">
        {{ tag }}
        <DeleteTagButton class="delete" @click="removeTag(index)" />
      </div>
    </div>

    <section class="dimensions-list">
      <DimensionsItem
        v-for="(item, index) in dimensions"
        :key="'dimension' + index"
        :title="item.dimension.title"
        :is-disabled="!isDisabled(item.dimension.id)"
        :select-list="selectedList(item.dimension.title)"
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
  },
  data() {
    return {
      tags: ['a', 'b'],
      author: '',
      country: '',
      language: '',
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
      switch (name) {
        case 'Author':
          this.author = val
          break
        case 'Language':
          this.language = val
          break
        case 'Country':
          this.country = val
      }
    },
    selectedList(title) {
      switch (title) {
        case 'Author':
          return this.dimensionAuthors?.map((el) => el.entry_author)
        case 'Language':
          return this.dimensionLanguages?.map(
            (el) => el.feed_language__language
          )
        case 'Country':
          return this.dimensionCountries?.map((el) => el.feedlink__country)
      }
    },
    removeTag(index) {
      this.tags.splice(index, 1)
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

  &::-webkit-scrollbar {
    height: 5px;
    width: 5px;
  }

  &::-webkit-scrollbar-track {
    background: var(--secondary-bg-color);
    border: 1px solid var(--input-border-color);
    border-radius: 0 10px 10px 0;
  }

  &::-webkit-scrollbar-thumb {
    height: 4px;

    background: var(--secondary-text-color);
    border-radius: 10px;
  }
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
