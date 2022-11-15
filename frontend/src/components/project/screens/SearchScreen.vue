<template>
  <div v-if="currentProject">
    <NavigationBar
      v-if="currentProject"
      :title="currentProject.title"
      hint="Search by keywords and phrases "
    >
      <BaseButton class="button" @click="updateProjectData">Save</BaseButton>
    </NavigationBar>

    <div class="search-settings-wrapper">
      <ProjectKeywords
        :main-keywords="currentKeywords"
        :additional-keywords="currentAdditionalKeywords"
        :exclude-keywords="currentExcludeKeywords"
        @show-result="showResults"
        @update-collection="updateCollection"
      />
      <SearchResults
        :current-project="currentProject"
        :is-checkbox-clipping-widget="true"
        :clipping-content="clippingContent"
        @update-page="showResults"
        @update-posts-count="showResults"
      />
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import NavigationBar from '@/components/navigation/NavigationBar'
import ProjectKeywords from '@/components/workspace/ProjectKeywords'
import SearchResults from '@/components/SearchResults'
import BaseButton from '@/components/buttons/BaseButton'

export default {
  name: 'SearchScreen',
  components: {BaseButton, SearchResults, ProjectKeywords, NavigationBar},
  props: {
    currentProject: {
      type: [Array, Object],
      required: true,
    },
  },
  created() {
    this[action.UPDATE_ADDITIONAL_FILTERS]({
      date_range: [
        new Date(this.currentProject.start_search_date),
        new Date(this.currentProject.end_search_date),
      ],
    })

    this.showResults()

    this[action.GET_CLIPPING_FEED_CONTENT_WIDGET](this.currentProject.id)
  },
  computed: {
    ...mapGetters({
      additionalFilters: get.ADDITIONAL_FILTERS,
      keywords: get.KEYWORDS,
      clippingContent: get.CLIPPING_FEED_CONTENT_WIDGET,
    }),
    currentKeywords() {
      return this.currentProject?.keywords
    },
    currentAdditionalKeywords() {
      return this.currentProject?.additional_keywords
    },
    currentExcludeKeywords() {
      return this.currentProject?.ignore_keywords
    },
  },
  methods: {
    ...mapActions([
      action.POST_SEARCH,
      action.UPDATE_PROJECT,
      action.UPDATE_KEYWORDS_LIST,
      action.UPDATE_ADDITIONAL_FILTERS,
      action.GET_CLIPPING_FEED_CONTENT_WIDGET,
    ]),
    showResults(pageNumber, numberOfPosts) {
      try {
        this[action.POST_SEARCH]({
          keywords: this.currentKeywords || this.keywords?.keywords,
          additions:
            this.currentAdditionalKeywords ||
            this.keywords?.additional_keywords,
          exceptions:
            this.currentExcludeKeywords || this.keywords?.ignore_keywords,
          country: this.currentProject?.country || [],
          language: this.currentProject?.language || [],
          sentiment: this.currentProject?.sentiment || [],
          date_range: [
            this.additionalFilters?.date_range[0] ||
              this.currentProject?.start_search_date,

            this.additionalFilters?.date_range[1] ||
              this.currentProject?.end_search_date,
          ],
          source: [],
          author: this.currentProject?.author || [],
          posts_per_page: numberOfPosts || 20,
          page_number: pageNumber || 1,
        })
      } catch (e) {
        console.log(e)
      }
    },
    updateProjectData: function () {
      try {
        this[action.UPDATE_PROJECT]({
          projectId: this.currentProject?.id,
          data: {
            title: this.currentProject?.title,
            note: this.currentProject?.note,
            keywords: this.currentKeywords || this.keywords?.keywords,
            additional_keywords:
              this.currentAdditionalKeywords ||
              this.keywords?.additional_keywords,
            ignore_keywords:
              this.currentExcludeKeywords || this.keywords?.ignore_keywords,
            max_items: '',
            image: null,
            arabic_name: '',
            english_name: '',
            creator: this.currentProject?.creator,
            source: this.currentProject?.source,
            workspace: this.currentProject?.workspace,
            start_search_date:
              this.additionalFilters?.date_range[0] ||
              this.currentProject?.start_search_date,
            end_search_date:
              this.additionalFilters?.date_range[1] ||
              this.currentProject?.end_search_date,
          },
        })
      } catch (e) {
        console.log(e)
      }
    },
    updateCollection(name, val) {
      this[action.UPDATE_KEYWORDS_LIST]({
        [name]: val,
      })
    },
  },
}
</script>

<style scoped>
.search-settings-wrapper {
  display: flex;
  justify-content: space-between;
  gap: 108px;
}

.button {
  width: 105px;
}
</style>
