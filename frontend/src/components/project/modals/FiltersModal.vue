<template>
  <BaseModal
    modal-frame-style="max-width: 60vw; min-width: 40vw; max-height: 80vh;"
    title="Widgets Filters"
  >
    <FiltersScreen
      :project-id="projectId"
      :module-name="moduleName"
      :authors-filters="currentProject.author_dimensions"
      :countries-filters="currentProject.country_dimensions"
      :languages-filters="currentProject.language_dimensions"
      :sources-filters="currentProject.source_dimensions"
      :sentiments-filters="currentProject.sentiment_dimensions"
    />

    <BaseButton class="button" @click="saveFiltersSettings">
      <CustomText text="Save" />
    </BaseButton>
  </BaseModal>
</template>

<script>
import CustomText from '@components/CustomText'
import BaseModal from '@components/modals/BaseModal'
import BaseButton from '@components/common/BaseButton'
import FiltersScreen from '@components/project/screens/FiltersScreen'

export default {
  name: 'FiltersModal',
  components: {
    FiltersScreen,
    BaseButton,
    BaseModal,
    CustomText,
  },
  props: {
    moduleName: {type: String, required: true},
    projectId: {type: [String, Number], required: false},
    currentProject: {type: [Array, Object], required: false},
  },
  methods: {
    saveFiltersSettings() {
      this.$emit('save-filters-settings')
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
