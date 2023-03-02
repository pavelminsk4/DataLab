<template>
  <MainLayout>
    <div class="content-header">
      <MainLayoutTitleBlock title="Social Media">
        <SocialMediaIcon class="title-icon" />
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
    />

    <BlankPage v-else page-name="SocialMediaWorkspaces" />
  </MainLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseButtonWithTooltip from '@/components/BaseButtonWithTooltip'
import BlankPage from '@/components/BlankPage'
import MainLayout from '@components/layout/MainLayout'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import WorkspacesScreen from '@/components/dashboard/WorkspacesScreen'

import SocialMediaIcon from '@components/icons/SocialMediaIcon'
import PlusIcon from '@/components/icons/PlusIcon'

export default {
  name: 'SocialMediaWorkspacesView',
  components: {
    BaseButtonWithTooltip,
    BlankPage,
    MainLayout,
    MainLayoutTitleBlock,
    SocialMediaIcon,
    PlusIcon,
    WorkspacesScreen,
  },
  computed: {
    //TODO: change
    ...mapGetters({
      department: get.DEPARTMENT,
      // workspaces: get.WORKSPACES,
    }),
    workspaces() {
      return []
    },
    isProjectCreationAvailable() {
      return (
        this.department?.current_number_of_projects >=
        this.department?.max_projects
      )
    },
  },
  methods: {
    //TODO: change
    ...mapActions([
      action.CREATE_WORKSPACE,
      action.UPDATE_CURRENT_STEP,
      action.UPDATE_WORKSPACE,
    ]),
    createWorkspace() {
      this.$router.push({
        name: 'SocialCreateWorkspace',
        params: {workspaceId: 'new'},
      })
    },
    addNewProject(workspaceId) {
      //TODO: change
      this[action.UPDATE_CURRENT_STEP]('SocialWorkspaceStep2')
      this.$router.push({
        name: 'SocialWorkspaceStep2',
        params: {workspaceId},
      })
    },
    saveSettings(settings) {
      //TODO: change
      this[action.UPDATE_WORKSPACE](settings)
    },

    openWorkspace(workspaceId) {
      this.$router.push({name: 'SocialWorkspace', params: {workspaceId}})
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
