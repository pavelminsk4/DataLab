<template>
  <MainLayout>
    <div class="content-header">
      <MainLayoutTitleBlock
        v-if="workspace?.title"
        :title="workspace.title"
        :description="workspace.description"
        :back-page="backPage"
        :should-translate="false"
      >
        <component :is="`${moduleName}Icon`" class="online-icon" />
      </MainLayoutTitleBlock>

      <BaseButtonWithTooltip
        :is-disabled="isProjectCreationAvailable"
        :has-tooltip="isProjectCreationAvailable"
        tooltip-title="Created the maximum possible number of projects!"
        @click="$emit('create-project')"
      >
        <CustomText text="Create new project" />
      </BaseButtonWithTooltip>
    </div>

    <div class="sort-wrapper">
      <CustomText tag="span" text="Sort by" class="hint" />
      <CustomText text="Latest" class="sort-option" />

      <BaseInput
        v-model="search"
        label=" "
        placeholder="Search project..."
        :isSearch="true"
        class="search-users"
      />
    </div>

    <div class="projects-wrapper scroll">
      <ProjectsTable
        :table-header="tableHeader"
        :values="filteredProjects"
        :members="workspace.members"
        @delete-project="deleteProject"
        @go-to-project="goToProjectSettings"
        @stop-collecting-data="stopCollectingData"
      />
    </div>
  </MainLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import OnlineIcon from '@components/icons/OnlineIcon'
import SocialIcon from '@components/icons/SocialIcon'

import BaseButtonWithTooltip from '@components/BaseButtonWithTooltip'
import BaseInput from '@components/common/BaseInput'
import MainLayout from '@components/layout/MainLayout'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import ProjectsTable from '@components/ProjectsTable'
import CustomText from '@components/CustomText'

export default {
  name: 'WorkspaceView',
  components: {
    BaseButtonWithTooltip,
    BaseInput,
    MainLayout,
    MainLayoutTitleBlock,
    OnlineIcon,
    ProjectsTable,
    SocialIcon,
    CustomText,
  },
  props: {
    tableHeader: {type: Array, default: () => []},
    moduleName: {type: String, default: 'Online'},
    workspace: {type: Object, default: () => ({})},
    backPage: {type: Object, default: () => ({name: 'page', routeName: ''})},
  },
  data() {
    return {
      search: '',
    }
  },
  computed: {
    ...mapGetters({
      department: get.DEPARTMENT,
      isLoading: get.LOADING,
    }),
    isProjectCreationAvailable() {
      return (
        this.department?.current_number_of_projects >=
        this.department?.max_projects
      )
    },
    sortedProjects() {
      const projects = this.workspace?.projects
      return projects?.sort(
        (projectA, projectB) =>
          new Date(projectB.created_at) - new Date(projectA.created_at)
      )
    },
    filteredProjects() {
      if (!this.search) return this.sortedProjects
      return this.sortedProjects.filter((project) =>
        project.title.toLowerCase().includes(this.search.toLowerCase())
      )
    },
  },
  created() {
    this[action.CLEAR_STATE]()
  },
  methods: {
    ...mapActions([action.CLEAR_STATE]),
    goToProjectSettings(projectId) {
      this.$emit('open-project', projectId)
    },
    deleteProject(id) {
      this.$emit('delete-project', id)
    },
    stopCollectingData(projectId) {
      this.$emit('stop-collecting-data', projectId)
    },
  },
}
</script>

<style lang="scss" scoped>
.content-header {
  display: flex;
  justify-content: space-between;
}

.online-icon {
  width: 20px;
  height: 20px;
}

.sort-wrapper {
  display: flex;
  align-items: center;

  margin-bottom: 22px;
}

.hint {
  color: var(--typography-secondary-color);
}

.sort-option {
  flex-grow: 1;
  display: flex;
  align-items: center;

  margin-left: 15px;
}

.sort-icon {
  margin-left: 7px;
}

.projects-wrapper {
  height: calc(100% - 200px);
}
</style>
