<template>
  <div
    class="project-cart-wrapper transition"
    @click="openWorkspace"
    @mousemove="isShowMenu = true"
    @mouseleave="hideMenu"
  >
    <div class="cart-button-wrapper">
      <div class="number-projects">{{ numberProjects }} projects</div>
      <UsersIconsBar :users="members" />
    </div>

    <div class="project-title-wrapper">
      <h3 class="title">{{ title }}</h3>
      <div class="description">{{ description }}</div>
    </div>

    <div class="cart-button-wrapper">
      <BaseButton
        :is-not-background="true"
        :style="`z-index=${members.length + 1}`"
        class="add-button"
        @click="addNewProject"
      >
        <PlusIcon class="plus-icon" />
        <span class="button-text">Add Project</span>
      </BaseButton>

      <BaseTooltipSettings v-if="isShowMenu" :id="id">
        <div class="tooltip-item" @click.stop="openSettingsModal">
          <EditIcon />
          <span>Edit</span>
        </div>
        <div class="tooltip-item" @click.stop="toggleDeleteModal">
          <DeleteIcon />
          <span>Delete</span>
        </div>
      </BaseTooltipSettings>
    </div>
  </div>

  <AreYouSureModal
    v-if="isOpenDeleteModal"
    :item-to-delete="workspaceItem"
    @close="toggleDeleteModal"
    @delete="deleteWorkspace"
  />
</template>

<script>
import {mapActions} from 'vuex'
import {action} from '@store/constants'

import PlusIcon from '@components/icons/PlusIcon'
import UsersIconsBar from '@components/UsersIconsBar'
import BaseTooltipSettings from '@/components/BaseTooltipSettings'
import EditIcon from '@/components/icons/EditIcon'
import DeleteIcon from '@/components/icons/DeleteIcon'
import AreYouSureModal from '@/components/modals/AreYouSureModal'
import BaseButton from '@/components/common/BaseButton'

export default {
  name: 'ProjectItem',
  components: {
    AreYouSureModal,
    BaseButton,
    DeleteIcon,
    EditIcon,
    BaseTooltipSettings,
    UsersIconsBar,
    PlusIcon,
  },
  emits: ['add-new-project', 'navigate-to-workspace', 'open-modal'],
  props: {
    title: {
      type: String,
      default: '',
    },
    description: {
      type: String,
      default: '',
    },
    id: {
      type: Number,
      required: true,
    },
    members: {
      type: [Array, Object],
      required: true,
    },
    numberProjects: {
      type: Number,
      default: 0,
    },
  },
  data() {
    return {
      isOpenDeleteModal: false,
      workspaceItem: {
        type: 'workspace',
        name: this.title,
      },
      isShowMenu: false,
    }
  },
  methods: {
    ...mapActions([action.DELETE_WORKSPACE]),
    openWorkspace() {
      this.$emit('navigate-to-workspace')
    },
    addNewProject() {
      this.$emit('add-new-project')
    },
    openSettingsModal() {
      this.$emit('open-modal', this.id)
    },
    deleteWorkspace() {
      this[action.DELETE_WORKSPACE](this.id)
    },
    toggleDeleteModal() {
      this.isOpenDeleteModal = !this.isOpenDeleteModal
      this.togglePageScroll(this.isOpenDeleteModal)
    },
    hideMenu() {
      this.isShowMenu = false
    },
  },
}
</script>

<style lang="scss" scoped>
.project-cart-wrapper {
  --items-in-row: 4;
  display: flex;
  flex-direction: column;
  flex-shrink: 1;

  width: calc(
    (100% - var(--gap) * (var(--items-in-row) - 1)) / var(--items-in-row)
  );
  height: 176px;
  padding: 16px 21px 13px 18px;

  background: var(--background-secondary-color);
  border: var(--border-primary);
  border-radius: 8px;
  box-shadow: 1px 4px 16px rgba(135, 135, 135, 0.2);

  cursor: pointer;
  transition-duration: 0.4s;

  &:hover {
    box-shadow: 0px 21px 21px rgba(113, 93, 231, 0.09),
      0px 5px 11px rgba(113, 93, 231, 0.1), 0px 0px 0px rgba(113, 93, 231, 0.1);

    transform: scale(1.1);

    .title {
      color: var(--primary-color);
    }
  }
}

.number-projects {
  padding: 6px 8px;

  background: var(--background-additional-color);
  border-radius: 4px;

  font-size: 11px;
}

.project-title-wrapper {
  display: flex;
  flex-direction: column;
  flex-grow: 1;

  margin-top: 16px;
  color: var(--typography-primary-color);
}

.title {
  overflow: hidden;

  white-space: nowrap;
  text-overflow: ellipsis;
  font-style: normal;
  font-weight: 500;
  font-size: 18px;
}

.description {
  margin-top: 4px;

  font-size: 14px;
}

.cart-button-wrapper {
  position: relative;

  display: flex;
  justify-content: space-between;
  align-items: center;
}

.add-button {
  border-color: transparent;

  color: var(--primary-color);
}

.plus-icon {
  margin-right: 8px;
}

.tooltip-item {
  display: flex;
  align-items: center;
  gap: 10px;

  width: 152px;
  padding: 6px 10px;

  border-radius: 8px;

  &:hover {
    background-color: var(--background-additional-color);
  }
}

@media screen and (max-width: 1080px) {
  .project-cart-wrapper {
    width: calc((100% / 4) - (3rem / 4));
  }
}

@media screen and (max-width: 750px) {
  .project-cart-wrapper {
    width: calc((100% / 2) - (2rem / 3));
    height: 160px;
  }
}
</style>
