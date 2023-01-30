<template>
  <MainLayout>
    <div v-if="workspace" class="create-project-wrapper">
      <div>
        <div class="back-button" @click="backToPage">
          <ArrowLeftIcon class="arrow-back" />
          <span>Back to dashboard</span>
        </div>
        <h1 class="title">{{ workspace.title }}</h1>
        <span class="hint">
          Select the project you want to work on or create a new search
        </span>

        <div class="sort-wrapper">
          <span class="hint">Sort by</span>
          <div class="sort-option">Latest <SortIcon class="sort-icon" /></div>
        </div>
      </div>

      <BaseButtonWithTooltip
        :is-disabled="isProjectCreationAvailable"
        :has-tooltip="isProjectCreationAvailable"
        tooltip-title="Created the maximum possible number of projects!"
        class="create-new-button"
        @click="createProject"
      >
        Create new project
      </BaseButtonWithTooltip>
    </div>

    <ProjectsTable
      @go-to-project="goToProjectSettings"
      :values="workspace?.projects"
    />
  </MainLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import SortIcon from '@components/icons/SortIcon'

import MainLayout from '@components/layout/MainLayout'
import ProjectsTable from '@/components/ProjectsTable'
import ArrowLeftIcon from '@/components/icons/ArrowLeftIcon'
import BaseButtonWithTooltip from '@/components/BaseButtonWithTooltip'

export default {
  name: 'WorkspaceView',
  components: {
    BaseButtonWithTooltip,
    ArrowLeftIcon,
    ProjectsTable,
    MainLayout,
    SortIcon,
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
        this.department.current_number_of_projects ===
        this.department.max_projects
      )
    },
  },
  created() {
    if (!this.workspaces.length) {
      this[action.GET_WORKSPACES]()
    }

    this[action.CLEAR_STATE]()
  },
  methods: {
    ...mapActions([action.GET_WORKSPACES, action.CLEAR_STATE]),
    createProject() {
      this.$router.push({
        name: 'ProjectStep1',
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

    backToPage() {
      this.$router.push({
        name: 'Home',
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.create-project-wrapper {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.back-button {
  margin-bottom: 15px;
  max-width: fit-content;

  cursor: pointer;

  color: var(--secondary-text-color);
  font-size: 14px;

  .arrow-back {
    margin-right: 5px;
  }

  &:hover {
    color: var(--primary-button-color);
  }
}

.title {
  margin: 0 0 8px;

  color: var(--primary-text-color);

  font-style: normal;
  font-weight: 600;
  font-size: 36px;
  line-height: 42px;
}

.hint {
  color: var(--secondary-text-color);

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
}

.sort-wrapper {
  display: flex;

  margin: 34px 0 22px;

  color: var(--primary-text-color);

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
}

.sort-option {
  display: flex;
  align-items: center;

  margin-left: 15px;
}

.sort-icon {
  margin-left: 7px;
}

.create-new-button {
  width: 178px;
}
</style>
