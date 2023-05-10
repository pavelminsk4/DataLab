<template>
  <DimensionsModal
    :project-id="projectId"
    :currentProject="currentProject"
    :module-name="currentProject.source"
    @save-dimensions-settings="saveChanges"
  />
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import DimensionsModal from '@/components/project/modals/DimensionsModal'

export default {
  name: 'OnlineDimensionsModal',
  components: {DimensionsModal},
  props: {
    projectId: {type: [String, Number], required: false},
    currentProject: {type: [Array, Object], required: false},
  },
  computed: {
    ...mapGetters({
      selectedDimensions: get.SELECTED_DIMENSIONS,
    }),
  },
  methods: {
    ...mapActions([action.UPDATE_PROJECT, action.GET_WORKSPACES]),
    async saveChanges() {
      try {
        await this[action.UPDATE_PROJECT]({
          projectId: this.projectId,
          data: {
            sentiment_dimensions: this.selectedDimensions.sentiments,
            author_dimensions: this.selectedDimensions.authors,
            country_dimensions: this.selectedDimensions.countries,
            language_dimensions: this.selectedDimensions.languages,
            source_dimensions: this.selectedDimensions.sources,
          },
        })

        this.$emit('update-search-results')
        this.$emit('close')
      } catch (e) {
        console.log(e)
      }
    },
  },
}
</script>
