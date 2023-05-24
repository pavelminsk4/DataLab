<template>
  <MainLayout>
    <div class="content-header">
      <MainLayoutTitleBlock title="24/7" />

      <BaseButtonWithTooltip
        v-if="!workspaces?.length"
        :is-disabled="isProjectCreationAvailable"
        :has-tooltip="isProjectCreationAvailable"
        class="create-new-button"
        @click="$emit('create-workspace')"
      >
        <PlusIcon />
        <span>Create new workspace</span>
      </BaseButtonWithTooltip>
    </div>

    <WorkspacesScreen
      v-if="workspaces?.length"
      :workspaces="workspaces"
      :isProjectCreationAvailable="isProjectCreationAvailable"
      @create-workspace="$emit('create-workspace')"
      @open-workspace="openWorkspaceFolder"
      @add-new-project="addNewProject"
      @save-settings="saveSettings"
      @delete-workspace="deleteWorkspace"
    />

    <div v-else class="no-tfs-wrapper">
      <img
        src="@/assets/twenty-four-seven/no-tfs-workspaces.svg"
        alt="No 24/7 image"
      />
      <div>There's nothing here &#128064;</div>
    </div>
  </MainLayout>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'

import BaseButtonWithTooltip from '@/components/BaseButtonWithTooltip'
import WorkspacesScreen from '@/components/dashboard/WorkspacesScreen'
import MainLayoutTitleBlock from '@/components/layout/MainLayoutTitleBlock'
import MainLayout from '@components/layout/MainLayout'
import PlusIcon from '@/components/icons/PlusIcon'

const {mapActions} = createNamespacedHelpers('twentyFourSeven')

export default {
  name: 'TFSModuleScreen',
  components: {
    MainLayout,
    MainLayoutTitleBlock,
    BaseButtonWithTooltip,
    PlusIcon,
    WorkspacesScreen,
  },
  props: {
    workspaces: {type: Array, default: () => []},
    isProjectCreationAvailable: {type: Boolean, default: true},
  },
  methods: {
    ...mapActions([action.UPDATE_WORKSPACE, action.DELETE_WORKSPACE]),
    openWorkspaceFolder(workspaceId) {
      this.$emit('open-workspace', workspaceId)
    },
    addNewProject(workspaceId) {
      this.$emit('add-new-project', workspaceId)
    },
    saveSettings(settings) {
      this[action.UPDATE_WORKSPACE](settings)
    },

    deleteWorkspace(workspaceId) {
      this[action.DELETE_WORKSPACE](workspaceId)
    },
  },
}
</script>

<style lang="scss" scoped>
.content-header {
  display: flex;
  justify-content: space-between;
}

.no-tfs-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;

  width: 100%;

  font-weight: 500;
  font-size: 18px;
}
</style>
