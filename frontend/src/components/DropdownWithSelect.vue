<template>
  <div :class="[`dropdown-wrapper-${name}`, 'dropdown-wrapper', 'scroll']">
    <div v-if="modelValue.title" class="title" @click="openMainDropdown">
      {{ modelValue.title }}
    </div>
    <CustomText
      v-else
      text="Select project from workspaces"
      class="title"
      @click="openMainDropdown"
    />
    <section v-if="isOpenMainDropdown" class="container-workspaces">
      <div v-for="workspace in workspaces" :key="workspace" class="workspace">
        <BaseDropdown
          v-for="projects in workspace"
          :key="projects"
          :name="stringToPascalCase(Object.keys(workspace)[0])"
          :title="Object.keys(workspace)[0]"
          :custom-style="dropdownStyles"
          :title-style="titleStyles"
        >
          <span
            v-for="project in projects"
            :key="project.id"
            :value="project"
            class="project"
            @click="handleProjectClick(project)"
          >
            {{ project.title }}
          </span>
        </BaseDropdown>
      </div>
    </section>
  </div>
</template>

<script>
import CustomText from '@/components/CustomText'
import BaseDropdown from '@/components/BaseDropdown'
import {stringToPascalCase} from '@/lib/utilities'

export default {
  name: 'DropdownWithSelect',
  components: {BaseDropdown, CustomText},
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
    this.titleStyles =
      'font-size: 16px; font-weight: 500; color: var(--typography-primary-color);'

    document.addEventListener('click', this.closeDropdown)
  },
  unmounted() {
    document.addEventListener('click', this.closeDropdown)
  },
  methods: {
    stringToPascalCase,

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
  display: flex;
  flex-direction: column;

  height: fit-content;

  background-color: var(--background-secondary-color);
  border: var(--border-primary);
  border-radius: 8px;

  cursor: pointer;
  white-space: nowrap;

  .title {
    display: flex;
    align-items: center;

    margin-left: 5px;
    height: 100%;
  }

  .container-workspaces {
    position: absolute;
    z-index: 2;

    width: 100%;
    margin-top: 40px;

    background-color: var(--background-secondary-color);
    border: var(--border-primary);
    border-radius: 8px;

    .workspace {
      z-index: 2;

      display: flex;
      flex-direction: column;
      width: 100%;

      cursor: pointer;
      padding: 5px;

      font-size: 12px;
      color: #484c52;
      .project {
        padding-left: 10px;

        border-radius: 8px;
      }

      .project:hover {
        color: var(--button-text-color);
        background-color: var(--primary-hover-color);
      }

      .dropdown-wrapper {
        border: none;
      }
    }
  }
}
</style>
