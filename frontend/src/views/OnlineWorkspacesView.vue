<template>
  <MainLayout>
    <div class="content-header">
      <MainLayoutTitleBlock title="Online">
        <OnlineIcon class="title-icon" />
      </MainLayoutTitleBlock>

      <BaseButtonWithTooltip
        v-if="!workspaces.length"
        :is-disabled="isProjectCreationAvailable"
        :has-tooltip="isProjectCreationAvailable"
        tooltip-title="Created the maximum possible number of projects!"
        class="create-new-button"
        @click="createWorkspace"
      >
        <PlusIcon />
        <span>Create new workspace</span>
      </BaseButtonWithTooltip>
    </div>

    <WorkspacesScreen
      v-if="workspaces.length"
      :workspaces="workspaces"
      :isProjectCreationAvailable="isProjectCreationAvailable"
      @create-workspace="createWorkspace"
      @save-settings="saveSettings"
      @add-new-project="addNewProject"
      @open-workspace="openWorkspace"
      @delete-workspace="deleteWorkspace"
    />

    <BlankPage v-else page-name="OnlineWorkspaces" />
  </MainLayout>
</template>

<script>
import {mapActions, mapGetters, createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'
import {action as actionOnline, get as getOnline} from '@store/constants'

import BaseButtonWithTooltip from '@/components/BaseButtonWithTooltip'
import BlankPage from '@/components/BlankPage'
import MainLayout from '@components/layout/MainLayout'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import WorkspacesScreen from '@/components/dashboard/WorkspacesScreen'

import OnlineIcon from '@components/icons/OnlineIcon'
import PlusIcon from '@/components/icons/PlusIcon'

const {mapActions: mapOnlineActions, mapGetters: mapOnlineGetters} =
  createNamespacedHelpers('online')

export default {
  name: 'OnlineWorkspacesView',
  components: {
    BaseButtonWithTooltip,
    BlankPage,
    MainLayout,
    MainLayoutTitleBlock,
    OnlineIcon,
    PlusIcon,
    WorkspacesScreen,
  },
  computed: {
    ...mapGetters({
      department: get.DEPARTMENT,
    }),
    ...mapOnlineGetters({workspaces: getOnline.WORKSPACES}),
    isProjectCreationAvailable() {
      return (
        this.department?.current_number_of_projects >=
        this.department?.max_projects
      )
    },
  },
  methods: {
    ...mapActions([action.UPDATE_CURRENT_STEP]),
    ...mapOnlineActions([
      actionOnline.UPDATE_WORKSPACE,
      actionOnline.DELETE_WORKSPACE,
    ]),
    createWorkspace() {
      this.$router.push({
        name: 'OnlineCreateWorkspace',
        params: {workspaceId: 'new'},
      })
    },
    addNewProject(workspaceId) {
      this[action.UPDATE_CURRENT_STEP]('OnlineWorkspaceStep2')
      this.$router.push({
        name: 'OnlineWorkspaceStep2',
        params: {workspaceId},
      })
    },
    saveSettings(settings) {
      this[actionOnline.UPDATE_WORKSPACE](settings)
    },

    openWorkspace(workspaceId) {
      this.$router.push({name: 'OnlineWorkspace', params: {workspaceId}})
    },

    deleteWorkspace(workspaceId) {
      this[actionOnline.DELETE_WORKSPACE](workspaceId)
    },
  },
}
</script>

<style lang="scss" scoped>
.content-header {
  display: flex;
  justify-content: space-between;
}

.title-icon {
  width: 20px;
  height: 20px;
}
</style>
