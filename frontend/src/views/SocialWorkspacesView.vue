<template>
  <MainLayout>
    <div class="content-header">
      <MainLayoutTitleBlock title="Social Media">
        <SocialIcon class="title-icon" />
      </MainLayoutTitleBlock>

      <BaseButtonWithTooltip
        v-if="!workspaces?.length"
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

    <BaseSpinner v-if="isLoading" :is-full-space="true" />

    <WorkspacesScreen
      v-else-if="workspaces?.length"
      :workspaces="workspaces"
      :isProjectCreationAvailable="isProjectCreationAvailable"
      @create-workspace="createWorkspace"
      @save-settings="saveSettings"
      @add-new-project="addNewProject"
      @open-workspace="openWorkspace"
      @delete-workspace="deleteWorkspace"
    />

    <BlankPage v-else page-name="SocialMediaWorkspaces" />
  </MainLayout>
</template>

<script>
import {mapActions, mapGetters, createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'
import {action as actionSocial, get as getSocial} from '@store/constants'

import BaseButtonWithTooltip from '@/components/BaseButtonWithTooltip'
import BlankPage from '@/components/BlankPage'
import MainLayout from '@components/layout/MainLayout'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import WorkspacesScreen from '@/components/dashboard/WorkspacesScreen'
import BaseSpinner from '@/components/BaseSpinner'

import SocialIcon from '@components/icons/SocialIcon'
import PlusIcon from '@/components/icons/PlusIcon'

const {mapActions: mapSocialActions, mapGetters: mapSocialGetters} =
  createNamespacedHelpers('social')

export default {
  name: 'SocialWorkspacesView',
  components: {
    BaseButtonWithTooltip,
    BaseSpinner,
    BlankPage,
    MainLayout,
    MainLayoutTitleBlock,
    SocialIcon,
    PlusIcon,
    WorkspacesScreen,
  },
  computed: {
    ...mapGetters({department: get.DEPARTMENT}),
    ...mapSocialGetters({
      workspaces: getSocial.WORKSPACES,
      isLoading: get.LOADING,
    }),
    isProjectCreationAvailable() {
      return (
        this.department?.current_number_of_projects >=
        this.department?.max_projects
      )
    },
  },
  methods: {
    ...mapActions([action.UPDATE_CURRENT_STEP]),
    ...mapSocialActions([
      actionSocial.UPDATE_WORKSPACE,
      actionSocial.DELETE_WORKSPACE,
    ]),
    createWorkspace() {
      this.$router.push({
        name: 'SocialCreateWorkspace',
        params: {workspaceId: 'new'},
      })
    },
    addNewProject(workspaceId) {
      this[action.UPDATE_CURRENT_STEP]('SocialWorkspaceStep2')
      this.$router.push({
        name: 'SocialWorkspaceStep2',
        params: {workspaceId},
      })
    },
    saveSettings(settings) {
      this[action.UPDATE_WORKSPACE](settings)
    },

    openWorkspace(workspaceId) {
      this.$router.push({name: 'SocialWorkspace', params: {workspaceId}})
    },

    deleteWorkspace(workspaceId) {
      this[actionSocial.DELETE_WORKSPACE](workspaceId)
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
