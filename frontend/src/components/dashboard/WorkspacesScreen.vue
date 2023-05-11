<template>
  <SettingsWorkspaceModal
    v-if="isOpenModal"
    :currentWorkspace="currentWorkspace"
    modal-frame-style="width: 510px;"
    @close="toggleModal"
    @save-settings="saveSettings"
  />

  <BaseSpinner v-if="isLoading" class="spinner" />

  <div v-else>
    <div class="sort-wrapper">
      <span class="hint">Sort by</span>
      <div class="sort-option">Latest <SortIcon class="sort-icon" /></div>
      <BaseButtonWithTooltip
        :is-disabled="isProjectCreationAvailable"
        :has-tooltip="isProjectCreationAvailable"
        tooltip-title="Created the maximum possible number of projects!"
        class="create-new-button"
        @click="$emit('create-workspace')"
      >
        <PlusIcon />
        <span>Create new workspace</span>
      </BaseButtonWithTooltip>
    </div>

    <div class="items-wrapper scroll">
      <WorkspaceCard
        v-for="(item, index) in sortWorkspaces"
        :key="index"
        :title="item.title"
        :description="item.description"
        :number-projects="item.projects?.length"
        :id="item.id"
        :members="item.members"
        @open-modal="toggleModal(item)"
        @delete-workspace="$emit('delete-workspace', item.id)"
        @add-new-project="$emit('add-new-project', item.id)"
        @navigate-to-workspace="$emit('open-workspace', item.id)"
      />
    </div>
  </div>

  <div class="background-icon"></div>
</template>

<script>
import {mapGetters} from 'vuex'
import {get} from '@store/constants'

import SortIcon from '@components/icons/SortIcon'
import PlusIcon from '@/components/icons/PlusIcon'

import BaseButtonWithTooltip from '@/components/BaseButtonWithTooltip'
import BaseSpinner from '@/components/BaseSpinner'
import WorkspaceCard from '@components/dashboard/WorkspaceCard'
import SettingsWorkspaceModal from '@/components/modals/SettingsWorkspaceModal'

export default {
  name: 'WorkspacesScreen',
  components: {
    BaseButtonWithTooltip,
    BaseSpinner,
    SortIcon,
    PlusIcon,
    WorkspaceCard,
    SettingsWorkspaceModal,
  },
  props: {
    workspaces: {
      type: Array,
      default: () => [],
    },
    isProjectCreationAvailable: {
      type: Boolean,
      default: true,
    },
  },
  emits: [
    'create-workspace',
    'add-new-project',
    'save-settings',
    'open-workspace',
    'delete-workspace',
  ],
  data() {
    return {
      isOpenModal: false,
      currentWorkspace: null,
    }
  },
  computed: {
    ...mapGetters({
      department: get.DEPARTMENT,
      isLoading: get.LOADING,
    }),
    sortWorkspaces() {
      return this.sortingByLastDate(this.workspaces)
    },
  },
  methods: {
    sortingByLastDate(workspacesList) {
      return workspacesList.sort(function (a, b) {
        return new Date(b.created_at) - new Date(a.created_at)
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
      this.$emit('save-settings', {
        workspaceId: this.currentWorkspace.id,
        data: {title, description},
      })
      this.toggleModal()
    },
  },
}
</script>

<style lang="scss" scoped>
.hint {
  color: var(--typography-secondary-color);
}

.sort-wrapper {
  display: flex;
  align-items: center;

  margin-bottom: 24px;
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

  max-height: calc(100% - 140px);
  padding: 10px 26px;
  margin: -10px -26px;

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
