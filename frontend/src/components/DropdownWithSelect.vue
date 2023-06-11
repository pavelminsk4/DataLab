<template>
  <div :class="[`dropdown-wrapper-${name}`, 'dropdown-wrapper']">
    <div class="title" @click="openMainDropdown">
      {{ modelValue.title || 'Select project' }}
    </div>
    <template v-if="isOpenMainDropdown">
      <div v-for="workspace in workspaces" :key="workspace" class="workspace">
        <BaseDropdown
          v-for="projects in workspace"
          :key="projects"
          :name="Object.keys(workspace)[0]"
          :title="Object.keys(workspace)[0]"
          :custom-style="dropdownStyles"
        >
          <span
            v-for="project in projects"
            :key="project.id"
            :value="project"
            @click="handleProjectClick(project)"
          >
            {{ project.title }}
          </span>
        </BaseDropdown>
      </div>
    </template>
  </div>
</template>

<script>
import BaseDropdown from '@/components/BaseDropdown'

export default {
  name: 'DropdownWithSelect',
  components: {BaseDropdown},
  props: {
    name: {type: String, required: true},
    workspaces: {type: Array, required: true},
    modelValue: {type: Object, required: true},
  },
  data() {
    return {
      isOpenMainDropdown: false,
    }
  },
  computed: {},
  created() {
    this.dropdownStyles =
      'position: static; background: var(--background-secondary-color); box-shadow: none;'

    document.addEventListener('click', this.closeDropdown)
  },
  unmounted() {
    document.addEventListener('click', this.closeDropdown)
  },
  methods: {
    openMainDropdown() {
      this.isOpenMainDropdown = !this.isOpenMainDropdown
    },
    handleProjectClick(project) {
      this.$emit('update:modelValue', project)
      this.isOpenMainDropdown = false
    },
    closeDropdown({target}) {
      const dropdownList = document.querySelector(
        `.dropdown-wrapper-${this.name}`
      )

      if (!dropdownList?.contains(target)) {
        this.isOpenMainDropdown = false
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.dropdown-wrapper {
  position: relative;

  display: flex;
  flex-direction: column;

  padding: 5px;

  color: var(--typography-title-color);
  background-color: var(--background-secondary-color);
  border: var(--border-primary);
  border-radius: 8px;

  cursor: pointer;

  white-space: nowrap;

  .workspace {
    z-index: 2;

    top: 35px;
    right: 2px;

    display: flex;
    flex-direction: column;

    cursor: pointer;

    min-width: 100%;

    background-color: #ffffff;
    box-shadow: 1px 2px 6px rgba(135, 135, 135, 0.25);
    border-radius: 8px;

    font-size: 12px;
    color: var(--typography-primary-color);

    &__title {
      font-size: 16px;
    }
  }
}
</style>
