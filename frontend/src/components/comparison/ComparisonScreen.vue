<template>
  <MainLayout>
    <div class="header">
      <MainLayoutTitleBlock
        title="Comparison Module"
        :back-page="{name: 'main page', routeName: 'MainView'}"
      />
      <BaseButtonWithTooltip
        v-if="!workspaces?.length"
        :is-disabled="false"
        :has-tooltip="false"
        class="create-new-button"
        @click="$emit('create-workspace')"
      >
        <PlusIcon />
        <span>Create new workspace</span>
      </BaseButtonWithTooltip>
    </div>
    <AreYouSureModal
      v-if="isOpenDeleteModal"
      :item-to-delete="workspaceToDelete"
      @close="toggleDeleteModal"
      @delete="deleteWorkspace(workspaceId)"
    />

    <BaseSpinner v-if="isLoading" :is-full-space="true" />

    <WorkspacesScreen
      v-else-if="workspaces.length"
      :workspaces="workspaces"
      :is-project-creation-available="false"
      @add-new-project="addNewProject"
      @create-workspace="$emit('create-workspace')"
      @delete-workspace="deleteWorkspace"
      @open-workspace="openWorkspace"
      @save-settings="saveSettings"
    />

    <div v-else class="no-comparison-workspaces">
      <img
        src="@assets/comparison/no-comparison-workspaces.svg"
        alt="No comparison workspaces image"
      />
      <div class="no-comparison-workspaces__text">
        No workspaces created &#x1F4EC;
      </div>
    </div>
  </MainLayout>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'
import ComparisonMixin from '@lib/mixins/comparison.js'

import AreYouSureModal from '@components/modals/AreYouSureModal'
import BaseButtonWithTooltip from '@components/BaseButtonWithTooltip'
import MainLayout from '@components/layout/MainLayout'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import PlusIcon from '@components/icons/PlusIcon'
import WorkspacesScreen from '@components/dashboard/WorkspacesScreen'
import BaseSpinner from '@components/BaseSpinner'

const {mapActions, mapGetters} = createNamespacedHelpers('comparison')

export default {
  name: 'ComparisonScreen',
  mixins: [ComparisonMixin],
  components: {
    AreYouSureModal,
    BaseButtonWithTooltip,
    BaseSpinner,
    MainLayout,
    MainLayoutTitleBlock,
    PlusIcon,
    WorkspacesScreen,
  },
  props: {
    workspaces: {type: Array, required: true},
  },
  emits: ['create-workspace'],
  data() {
    return {
      isOpenDeleteModal: false,
    }
  },
  computed: {
    ...mapGetters({isLoading: get.LOADING}),
  },
  methods: {
    ...mapActions([action.DELETE_WORKSPACE, action.UPDATE_WORKSPACE]),

    addNewProject(workspaceId) {
      this[action.UPDATE_NEW_COMPARISON_WORKSPACE]({step: 2})
      this.$router.push({
        name: 'ComparisonWorkspaceStep2',
        params: {workspaceId},
      })
    },
    deleteWorkspace(workspaceId) {
      this[action.DELETE_WORKSPACE](workspaceId)
    },
    openWorkspace(workspaceId) {
      this.$router.push({name: 'ComparisonWorkspace', params: {workspaceId}})
    },
    saveSettings(settings) {
      this[action.UPDATE_WORKSPACE](settings)
    },
  },
}
</script>

<style lang="scss" scoped>
.header {
  display: flex;
  justify-content: space-between;

  .create-new-button {
    align-self: flex-end;
  }
}

.no-comparison-workspaces {
  display: flex;
  align-items: center;
  flex-direction: column;

  gap: 30px;

  &__text {
    display: flex;

    gap: 10px;
  }
}

.creator {
  display: flex;
  align-items: center;
}
</style>
