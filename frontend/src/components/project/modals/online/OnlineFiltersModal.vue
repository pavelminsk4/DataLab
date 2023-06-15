<template>
  <FiltersModal
    :project-id="projectId"
    :currentProject="currentProject"
    :module-name="currentProject.source"
    @save-filters-settings="saveChanges"
  />
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import FiltersModal from '@/components/project/modals/FiltersModal'

export default {
  name: 'OnlineFiltersModal',
  components: {FiltersModal},
  props: {
    projectId: {type: [String, Number], required: false},
    currentProject: {type: [Array, Object], required: false},
  },
  computed: {
    ...mapGetters({
      selectedFilters: get.SELECTED_FILTERS,
    }),
  },
  methods: {
    ...mapActions([action.UPDATE_PROJECT, action.GET_WORKSPACES]),
    async saveChanges() {
      try {
        await this[action.UPDATE_PROJECT]({
          projectId: this.projectId,
          data: {
            sentiment_dimensions: this.selectedFilters.sentiments,
            author_dimensions: this.selectedFilters.authors,
            country_dimensions: this.selectedFilters.countries,
            language_dimensions: this.selectedFilters.languages,
            source_dimensions: this.selectedFilters.sources,
          },
        })

        this.$emit('update-search-results')
        this.$emit('close')
      } catch (e) {
        console.error(e)
      }
    },
  },
}
</script>
