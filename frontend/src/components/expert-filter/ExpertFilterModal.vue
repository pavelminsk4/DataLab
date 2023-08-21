<template>
  <BaseModal style="--base-modal-content-padding: 0">
    <template #title>
      <span>Expert filter</span>
    </template>

    <div class="wrapper">
      <section class="expert-filter-section">
        <ExpertField v-model="expValue" label="Filter query" />

        <div class="expert-filter-buttons">
          <BaseButton :is-not-background="true">
            Detailed search syntax
          </BaseButton>
          <BaseButton :is-not-background="true">Reset</BaseButton>
        </div>
      </section>
      <section class="presets-section">
        <div class="preset-label">Presets</div>
        <div v-if="false">
          <BaseSearchField />
          <SelectWithCheckboxes />
        </div>
      </section>
    </div>

    <footer class="footer">
      <BaseButton :is-not-background="true">Save as</BaseButton>
      <BaseButton :is-not-background="true">Save</BaseButton>
      <BaseButton :is-not-background="true">Add Filter</BaseButton>
    </footer>
  </BaseModal>
</template>

<script>
import BaseButton from '@/components/common/BaseButton'
import BaseModal from '@/components/modals/BaseModal'
import ExpertField from '@components/expert-filter/ExpertField'
import SelectWithCheckboxes from '@components/SelectWithCheckboxes'
import BaseSearchField from '@components/BaseSearchField'

export default {
  name: 'ExpertFilterModal',
  components: {
    BaseButton,
    BaseModal,
    BaseSearchField,
    ExpertField,
    SelectWithCheckboxes,
  },
  data() {
    return {
      expValue: '',
    }
  },
}
</script>

<style lang="scss" scoped>
.wrapper {
  display: flex;

  width: 75vw;
}

.expert-filter-section {
  width: 100%;
  padding: 24px;

  background-color: var(--background-secondary-color);
}

.expert-filter-buttons {
  display: flex;
  justify-content: flex-end;

  gap: 16px;
  margin-top: 24px;
}

.presets-section {
  width: 100%;
  padding: 24px;

  background-color: var(--background-primary-color);
  border-left: var(--border-primary);
}

.preset-label {
  margin-bottom: 8px;

  color: var(--typography-title-color);
}

.footer {
  display: flex;
  justify-content: flex-end;

  width: 100%;
  padding: 18px 24px;
  gap: 16px;

  background-color: var(--background-secondary-color);
  border-top: var(--border-primary);
}
</style>
