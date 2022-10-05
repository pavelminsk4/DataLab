<template>
  <MainLayout>
    <SettingsWorkspaceModal
      v-if="isOpenModal"
      :workspace-id="1"
      modal-frame-style="width: 510px;"
      @close="toggleModal"
      @save-settings="saveSettings"
    />

    <div class="create-project-wrapper">
      <div>
        <h1 class="title">Dashboard</h1>
        <span class="hint"
          >Keep all your projects in order by arranging them by topic</span
        >

        <div class="sort-wrapper">
          <span class="hint">Sort by</span>
          <div class="sort-option">Latest <SortIcon class="sort-icon" /></div>
        </div>
      </div>

      <BaseButton class="create-new-button" @click="createWorkspace">
        Create new workspace
      </BaseButton>
    </div>
    <div v-if="workspaces" class="items-wrapper">
      <ProjectItem
        v-for="(item, index) in sortWorkspaces"
        :key="index"
        :title="item.title"
        :id="item.id"
        :members="item.members"
        @open-modal="toggleModal"
        @add-new-project="addNewProject(item.id)"
        @navigate-to-workspace="navigateToWorkspace(item.id)"
      />
    </div>
  </MainLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import SortIcon from '@components/icons/SortIcon'

import MainLayout from '@components/layout/MainLayout'
import ProjectItem from '@components/dashboard/ProjectItem'
import BaseButton from '@components/buttons/BaseButton'
import SettingsWorkspaceModal from '@/components/modals/SettingsWorkspaceModal'

export default {
  name: 'DashboardList',
  components: {
    SortIcon,
    BaseButton,
    MainLayout,
    ProjectItem,
    SettingsWorkspaceModal,
  },
  data() {
    return {
      isOpenModal: false,
      workspaceId: null,
    }
  },
  async created() {
    if (
      !this.workspaces.length ||
      this.workspaces.length !== this.numberOfWorkspaces
    ) {
      await this[action.GET_WORKSPACES]()
    }
  },
  computed: {
    ...mapGetters({workspaces: get.WORKSPACES}),
    numberOfWorkspaces() {
      return this.workspaces.length
    },
    sortWorkspaces() {
      return this.sortingByLastDate(this.workspaces)
    },
  },
  methods: {
    ...mapActions([
      action.GET_WORKSPACES,
      action.CREATE_WORKSPACE,
      action.UPDATE_CURRENT_STEP,
      action.UPDATE_OLD_WORKSPACE,
    ]),
    sortingByLastDate(workspacesList) {
      return workspacesList.sort(function (a, b) {
        return new Date(b.created_at) - new Date(a.created_at)
      })
    },
    createWorkspace() {
      this.loading = true
      this.$router.push({
        name: 'Step1',
      })
    },
    navigateToWorkspace(id) {
      this.loading = true
      this.$router.push({name: 'Workspace', params: {workspaceId: id}})
    },
    addNewProject(id) {
      this[action.UPDATE_CURRENT_STEP]('ProjectStep1')
      this.$router.push({
        name: 'ProjectStep1',
        params: {workspaceId: id},
      })
    },
    toggleModal(id) {
      this.isOpenModal = !this.isOpenModal
      this.workspaceId = id
    },
    saveSettings(title, description) {
      this[action.UPDATE_OLD_WORKSPACE]({
        workspaceId: this.workspaceId,
        data: {title: title, description: description},
      })
      this.toggleModal()
    },
  },
}
</script>

<style lang="scss" scoped>
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

.create-project-wrapper {
  display: flex;
  justify-content: space-between;
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

.items-wrapper {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;

  overflow: auto;

  height: 500px;
  padding-right: 15px;

  &::-webkit-scrollbar {
    height: 5px;
    width: 5px;
  }

  &::-webkit-scrollbar-track {
    background: var(--secondary-bg-color);
    border: 1px solid var(--input-border-color);
    border-radius: 0 10px 10px 0;
  }

  &::-webkit-scrollbar-thumb {
    height: 4px;

    background: var(--secondary-text-color);
    border-radius: 10px;
  }
}
</style>
