<template>
  <MainLayout>
    <div class="content-header">
      <MainLayoutTitleBlock
        v-if="workspace?.title"
        :title="workspace.title"
        description="
            Select the project you want to work on or create a new search"
        :back-page="{
          name: 'main page',
          routName: 'OnlineHome',
        }"
      >
        <OnlineIcon class="online-icon" />
      </MainLayoutTitleBlock>

      <BaseButtonWithTooltip
        :is-disabled="isProjectCreationAvailable"
        :has-tooltip="isProjectCreationAvailable"
        tooltip-title="Created the maximum possible number of projects!"
        @click="createProject"
      >
        Create new project
      </BaseButtonWithTooltip>
    </div>

    <div class="sort-wrapper">
      <span class="hint">Sort by</span>
      <div class="sort-option">Latest <SortIcon class="sort-icon" /></div>

      <BaseInput
        v-model="search"
        placeholder="Search users..."
        :isSearch="true"
        class="search-users"
      />
    </div>

    <div class="projects-wrapper scroll">
      <ProjectsTable
        @go-to-project="goToProjectSettings"
        :values="filteredProjects"
      />
    </div>
  </MainLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import SortIcon from '@components/icons/SortIcon'
import OnlineIcon from '@components/icons/OnlineIcon'

import BaseButtonWithTooltip from '@/components/BaseButtonWithTooltip'
import BaseInput from '@/components/common/BaseInput'
import MainLayout from '@components/layout/MainLayout'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import ProjectsTable from '@/components/ProjectsTable'

export default {
  name: 'WorkspaceView',
  components: {
    BaseButtonWithTooltip,
    BaseInput,
    MainLayout,
    MainLayoutTitleBlock,
    OnlineIcon,
    ProjectsTable,
    SortIcon,
  },
  data() {
    return {
      search: '',
    }
  },
  computed: {
    ...mapGetters({
      workspaces: get.WORKSPACES,
      department: get.DEPARTMENT,
      isLoading: get.LOADING,
    }),
    workspaceId() {
      return this.$route.params.workspaceId
    },
    workspace() {
      return this.workspaces.find((el) => el.id === +this.workspaceId)
    },
    isProjectCreationAvailable() {
      return (
        this.department?.current_number_of_projects >=
        this.department?.max_projects
      )
    },
    filteredProjects() {
      if (!this.search) return this.workspace?.projects
      return this.workspace?.projects.filter((project) =>
        project.title.toLowerCase().includes(this.search.toLowerCase())
      )
    },
  },
  async created() {
    if (!this.workspaces.length) {
      await this[action.GET_WORKSPACES]()
    }

    this[action.CLEAR_STATE]()
  },
  methods: {
    ...mapActions([action.GET_WORKSPACES, action.CLEAR_STATE]),
    createProject() {
      this.$router.push({
        name: 'WorkspaceStep2',
      })
    },
    goToProjectSettings(id) {
      this.$router.push({
        name: 'Analytics',
        params: {
          workspaceId: this.workspaceId,
          projectId: id,
        },
      })
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
