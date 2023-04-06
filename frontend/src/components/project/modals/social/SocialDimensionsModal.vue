<template>
  <DimensionsModal
    :project-id="projectId"
    :currentProject="currentProject"
    @save-dimensions-settings="saveChanges"
  />
</template>

<script>
import {mapGetters, createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'
import DimensionsModal from '@/components/project/modals/DimensionsModal'

const {mapActions} = createNamespacedHelpers('social')

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
