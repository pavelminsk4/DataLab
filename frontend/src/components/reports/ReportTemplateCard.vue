<template>
  <div class="card">
    <BaseCheckbox v-model="isChecked" class="card__header">
      <span class="card__title">{{
        capitalizeFirstLetter(templateTitle)
      }}</span>
    </BaseCheckbox>
    <BaseSelect
      v-model="selectedValues"
      :options="projects"
      :select-name="templateTitle"
      :is-disabled="templateChecked"
    >
      <li>
        <BaseCheckbox v-model="isSelectAllProxy" class="option">
          <span class="option__title">Choose all</span>
        </BaseCheckbox>
      </li>
      <li v-for="option in projects" :key="option">
        <BaseCheckbox v-model="selectedValues" :id="option" class="option">
          <span class="option__title">{{ option }}</span>
        </BaseCheckbox>
      </li>
    </BaseSelect>
    <div class="card__preview">
      <img
        :src="require(`@/assets/reports/templates/${templateTitle}.png`)"
        alt="Template image"
      />
    </div>
  </div>
</template>

<script>
import {capitalizeFirstLetter} from '@/lib/utilities'
import BaseCheckbox from '@/components/BaseCheckbox2'
import BaseSelect from '@/components/BaseSelect2'

export default {
  name: 'ReportTemplateCard',
  components: {BaseSelect, BaseCheckbox},
  props: {
    templateTitle: {type: String, required: true},
    projects: {type: Array, required: true},
    templateChecked: {type: Boolean, required: true},
    selectedProjects: {type: Array, required: true},
  },
  emits: ['update:templateChecked', 'update:selectedProjects'],
  data() {
    return {
      isSelectAll: false,
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
    isSelectAllProxy: {
      get() {
        return this.isSelectAll
      },
      set(val) {
        this.isSelectAll = val
        const currProjects = this.isSelectAll ? this.projects : []
        this.$emit('update:selectedProjects', currProjects)
      },
    },
  },
  created() {
    this.isSelectAllProxy = true
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

  background-color: var(--background-secondary-color);
  border: var(--border-primary);
  border-radius: var(--border-radius);

  width: 240px;

  &__header {
    gap: 10px;
    align-items: center;
  }

  &__title {
    display: flex;
    height: 100%;
    align-self: center;
    font-size: 16px;
  }

  .option {
    display: flex;
    gap: 10px;
    &__title {
      display: flex;
      align-self: center;
      height: 100%;
      font-size: 16px;
    }
  }
}
</style>
