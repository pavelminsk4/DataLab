<template>
  <BaseModal
    modal-frame-style="max-width: 60vw; min-width: 40vw; max-height: 80vh;"
    title="Widgets Dimensions"
  >
    <DimensionsScreen
      :project-id="projectId"
      :authors-dimensions="currentProject.author_dimensions"
      :countries-dimensions="currentProject.country_dimensions"
      :languages-dimensions="currentProject.language_dimensions"
      :sources-dimensions="currentProject.source_dimensions"
      :sentiments-dimensions="currentProject.sentiment_dimensions"
    />

    <BaseButton class="button" @click="saveChanges">Save</BaseButton>
  </BaseModal>
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import BaseModal from '@/components/modals/BaseModal'
import BaseButton from '@/components/common/BaseButton'
import DimensionsScreen from '@/components/project/screens/DimensionsScreen'

export default {
  name: 'AllDimensionsModal',
  components: {
    DimensionsScreen,
    BaseButton,
    BaseModal,
  },
  props: {
    projectId: {
      type: [String, Number],
      required: false,
    },
    currentProject: {
      type: [Array, Object],
      required: false,
    },
  },
  computed: {
    ...mapGetters({
      selectedDimensions: get.SELECTED_DIMENSIONS,
    }),
  },
  methods: {
    ...mapActions([action.UPDATE_PROJECT, action.GET_WORKSPACES]),
    saveChanges() {
      try {
        this[action.UPDATE_PROJECT]({
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

<style lang="scss" scoped>
.chips {
  margin-bottom: 36px;
}

.title {
  margin-bottom: 4px;

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
  color: var(--typography-title-color);
}

.select {
  margin-bottom: 20px;
}

.sentiments {
  display: flex;
  gap: 8px;

  .item {
    padding: 6px 12px;

    border: var(--border-primary);
    border-radius: 12px;

    cursor: pointer;

    font-style: normal;
    font-weight: 400;
    font-size: 14px;
    line-height: 20px;
    color: var(--typography-title-color);
  }

  .neutral-item {
    border: 1px solid var(--neutral-primary-color);

    color: var(--neutral-primary-color);
  }

  .negative-item {
    border: 1px solid var(--negative-primary-color);

    color: var(--negative-primary-color);
  }

  .positive-item {
    border: 1px solid var(--positive-primary-color);

    color: var(--positive-primary-color);
  }
}

.button {
  width: 59px;
  margin-top: 32px;
  margin-left: auto;
}
</style>
