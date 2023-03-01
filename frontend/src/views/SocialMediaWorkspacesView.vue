<template>
  <MainLayout>
    <div class="content-header">
      <MainLayoutTitleBlock title="Online">
        <OnlineIcon class="online-icon" />
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

import OnlineIcon from '@components/icons/OnlineIcon'
import PlusIcon from '@/components/icons/PlusIcon'

export default {
  name: 'SocialMediaWorkspacesView',
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
    ...mapActions([
      action.CREATE_WORKSPACE,
      action.UPDATE_CURRENT_STEP,
      action.UPDATE_WORKSPACE,
    ]),
    createWorkspace() {
      this.$router.push({
        name: 'Step1',
      })
    },
    addNewProject(workspaceId) {
      this[action.UPDATE_CURRENT_STEP]('WorkspaceStep2')
      this.$router.push({
        name: 'WorkspaceStep2',
        params: {workspaceId},
      })
    },
    saveSettings(settings) {
      this[action.UPDATE_WORKSPACE](settings)
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
</style>
