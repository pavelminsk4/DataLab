<template>
  <MainLayout>
    <template #default>
      <SettingsWorkspaceModal
        v-if="isOpenModal"
        :currentWorkspace="currentWorkspace"
        modal-frame-style="width: 510px;"
        @close="toggleModal"
        @save-settings="saveSettings"
      />

      <div class="content-header">
        <MainLayoutTitleBlock v-if="!isLoading && department" title="Online">
          <OnlineIcon class="online-icon" />
        </MainLayoutTitleBlock>

        <BaseButtonWithTooltip
          :is-disabled="isProjectCreationAvailable"
          :has-tooltip="isProjectCreationAvailable"
          tooltip-title="Created the maximum possible number of projects!"
          class="create-new-button"
          @click="createWorkspace"
        >
          Create new workspace
        </BaseButtonWithTooltip>
      </div>

      <BaseSpinner v-if="isLoading" class="spinner" />

      <div v-if="!isLoading && workspaces.length">
        <div class="sort-wrapper">
          <span class="hint">Sort by</span>
          <div class="sort-option">Latest <SortIcon class="sort-icon" /></div>
        </div>

        <div class="items-wrapper scroll">
          <ProjectItem
            v-for="(item, index) in sortWorkspaces"
            :key="index"
            :title="item.title"
            :description="item.description"
            :number-projects="item.projects.length"
            :id="item.id"
            :members="item.members"
            @open-modal="toggleModal(item)"
            @add-new-project="addNewProject(item.id)"
            @navigate-to-workspace="navigateToWorkspace(item.id)"
          />
        </div>
      </div>

      <BlankPage v-else page-name="Workspace" />

      <div class="background-icon"></div>
    </template>
  </MainLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import OnlineIcon from '@components/icons/OnlineIcon'
import SortIcon from '@components/icons/SortIcon'

import BaseButtonWithTooltip from '@/components/BaseButtonWithTooltip'
import BaseSpinner from '@/components/BaseSpinner'
import BlankPage from '@/components/BlankPage'
import MainLayout from '@components/layout/MainLayout'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import ProjectItem from '@components/dashboard/ProjectItem'
import SettingsWorkspaceModal from '@/components/modals/SettingsWorkspaceModal'

export default {
  name: 'WorkspacesView',
  components: {
    BaseButtonWithTooltip,
    BaseSpinner,
    BlankPage,
    SortIcon,
    MainLayout,
    MainLayoutTitleBlock,
    ProjectItem,
    SettingsWorkspaceModal,
    OnlineIcon,
  },
  data() {
    return {
      isOpenModal: false,
      currentWorkspace: null,
    }
  },
  computed: {
    ...mapGetters({
      workspaces: get.WORKSPACES,
      department: get.DEPARTMENT,
      isLoading: get.LOADING,
    }),
    sortWorkspaces() {
      return this.sortingByLastDate(this.workspaces)
    },
    isProjectCreationAvailable() {
      return (
        this.department?.current_number_of_projects >=
        this.department?.max_projects
      )
    },
  },
  methods: {
    ...mapActions([
      action.CREATE_WORKSPACE,
      action.UPDATE_CURRENT_STEP,
      action.UPDATE_WORKSPACE,
    ]),
    sortingByLastDate(workspacesList) {
      return workspacesList.sort(function (a, b) {
        return new Date(b.created_at) - new Date(a.created_at)
      })
    },
    createWorkspace() {
      this.$router.push({
        name: 'Step1',
      })
    },
    navigateToWorkspace(id) {
      this.$router.push({name: 'Workspace', params: {workspaceId: id}})
    },
    addNewProject(id) {
      this[action.UPDATE_CURRENT_STEP]('ProjectStep1')
      this.$router.push({
        name: 'ProjectStep1',
        params: {workspaceId: id},
      })
    },
    toggleModal(workspace) {
      if (workspace) {
        const {id, title, description, members} = workspace
        this.currentWorkspace = {id, title, description, members}
      }
      this.isOpenModal = !this.isOpenModal
      this.togglePageScroll(false)
    },
    saveSettings(title, description) {
      this[action.UPDATE_WORKSPACE]({
        workspaceId: this.currentWorkspace.id,
        data: {title, description},
      })
      this.toggleModal()
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

.hint {
  color: var(--typography-secondary-color);
}

.sort-wrapper {
  display: flex;

  margin-bottom: 24px;
  padding: 8px 0;
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
  align-self: flex-end;

  &:hover {
    .tooltip {
      visibility: visible;
    }
  }
}

.items-wrapper {
  --gap: 32px;

  display: flex;
  flex-wrap: wrap;
  gap: var(--gap);

  overflow: auto;

  max-height: 90%;
  padding: 20px 26px;
  margin: -20px -26px;

  @media (max-height: 850px) {
    max-height: 85%;
  }
}

.spinner {
  margin: 40px auto auto auto;
}

.tooltip {
  visibility: visible;
  margin-right: 218px;
}

.background-icon {
  position: absolute;
  left: 0;
  bottom: 0;
  z-index: -1;

  width: 100vw;
  height: 75vh;

  background: center / cover no-repeat url(@/assets/Background.svg);
  pointer-events: none;

  @media (max-height: 800px) {
    height: 66vh;
  }
}
</style>
