<template>
  <div class="card">
    <BaseCheckbox v-model="isChecked" class="card__header">
      <CustomText
        tag="span"
        :text="capitalizeFirstLetter(templateTitle)"
        class="card__title"
      />
    </BaseCheckbox>
    <MultiSelect
      v-model="selectedValues"
      :options="projects"
      :is-disabled="!templateChecked"
      :select-name="templateName"
      item-name="project"
    />
    <div class="card__preview">
      <img
        :src="require(`@assets/reports/templates/${templateName}.png`)"
        alt="Template image"
      />
    </div>
  </div>
</template>

<script>
import {capitalizeFirstLetter} from '@lib/utilities'

import CustomText from '@components/CustomText'
import BaseCheckbox from '@components/BaseCheckbox'
import MultiSelect from '@components/MultiSelect'

export default {
  name: 'ReportTemplateCard',
  components: {BaseCheckbox, MultiSelect, CustomText},
  props: {
    templateTitle: {type: String, required: true},
    templateName: {type: String, required: true},
    projects: {type: Array, required: true},
    templateChecked: {type: Boolean, required: true},
    selectedProjects: {type: Array, required: true},
  },
  emits: ['update:templateChecked', 'update:selectedProjects'],
  data() {
    return {
      isSelectAll: true,
    }
  },
  computed: {
    isChecked: {
      get() {
        return this.templateChecked
      },
      set(val) {
        this.$emit('update:templateChecked', val)
      },
    },
    selectedValues: {
      get() {
        return this.selectedProjects
      },
      set(val) {
        this.$emit('update:selectedProjects', val)
        this.isSelectAll = this.projects.length === val.length
      },
    },
  },
  methods: {
    capitalizeFirstLetter,
  },
}
</script>

<style lang="scss" scoped>
.card {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 15px 20px;
  gap: 15px;

  width: 240px;

  background-color: var(--background-secondary-color);
  border: var(--border-primary);
  border-radius: var(--border-radius);

  &__header {
    gap: 10px;
    align-items: center;
  }

  &__title {
    display: flex;
    align-self: center;
    font-size: 16px;

    height: 100%;
  }
}
</style>
