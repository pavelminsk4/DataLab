<template>
  <div v-if="currentProject">
    <NavigationBar
      v-if="currentProject"
      :title="currentProject.title"
      hint="Search by keywords and phrases "
      :is-show-button="false"
    />

    <div class="search-settings-wrapper">
      <ProjectKeywords
        :main-keywords="currentKeywords"
        :additional-keywords="currentAdditionalKeywords"
        :exclude-keywords="currentExcludeKeywords"
        @show-result="showResults"
        @update-collection="updateCollection"
      />
      <SearchResults :current-project="currentProject" />
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import NavigationBar from '@/components/navigation/NavigationBar'
import ProjectKeywords from '@/components/workspace/ProjectKeywords'
import SearchResults from '@/components/SearchResults'

export default {
  name: 'SearchScreen',
  components: {SearchResults, ProjectKeywords, NavigationBar},
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
  },
  computed: {
    ...mapGetters({
      additionalFilters: get.ADDITIONAL_FILTERS,
      keywords: get.KEYWORDS,
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
      action.UPDATE_KEYWORDS_LIST,
      action.UPDATE_ADDITIONAL_FILTERS,
    ]),
    showResults() {
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
        })
      } catch (e) {
        console.log(e)
      }
    },
    updateCollection(name, val) {
      console.log(name, val)
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
</style>
