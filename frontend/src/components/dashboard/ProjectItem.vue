<template>
  <div class="project-cart-wrapper transition" @click="openWorkspace">
    <div class="project-title-wrapper">
      <div class="title">{{ title }}</div>

      <BaseTooltipSettings :id="id">
        <div class="tooltip-item" @click.stop="openSettingsModal">
          <EditIcon />Edit
        </div>
        <div class="tooltip-item" @click.stop="toggleDeleteModal">
          <DeleteIcon />Delete
        </div>
      </BaseTooltipSettings>
    </div>

    <div class="cart-button-wrapper">
      <MembersIconsBar :members="members" />

      <button
        :style="`z-index=${members.length + 1}`"
        class="new-project"
        @click="addNewProject"
      >
        <span class="button-text">new</span>
        <span class="circle" aria-hidden="true"><PlusIcon /></span>
      </button>
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
import MembersIconsBar from '@components/MembersIconsBar.vue'
import BaseTooltipSettings from '@/components/BaseTooltipSettings'
import EditIcon from '@/components/icons/EditIcon'
import DeleteIcon from '@/components/icons/DeleteIcon'
import AreYouSureModal from '@/components/modals/AreYouSureModal'

export default {
  name: 'ProjectItem',
  components: {
    AreYouSureModal,
    DeleteIcon,
    EditIcon,
    BaseTooltipSettings,
    MembersIconsBar,
    PlusIcon,
  },
  props: {
    title: {
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
  },
  data() {
    return {
      isOpenDeleteModal: false,
      workspaceItem: {
        type: 'workspace',
        name: this.title,
      },
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
  },
}
</script>

<style lang="scss" scoped>
.project-cart-wrapper {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-shrink: 1;

  width: calc((100% / 5) - (4rem / 5));
  height: 130px;
  padding: 16px 21px 13px 18px;

  border: 1px solid var(--border-color);
  border-radius: 15px;
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);

  cursor: pointer;

  background: linear-gradient(to left, rgba(5, 95, 252, 0.7), #242529, #242529);
  background-size: 200%;
  transition: 0.5s;

  &:hover {
    background-position: right;
  }
}

.project-title-wrapper {
  display: flex;
  justify-content: space-between;

  color: var(--primary-text-color);
}

.title {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;

  font-style: normal;
  font-weight: 600;
  font-size: 16px;
  line-height: 22px;
}

.cart-button-wrapper {
  position: relative;

  display: flex;
  justify-content: space-between;
  align-items: center;
}

.new-project {
  position: absolute;
  right: 0;

  width: 74px;
  height: 30px;
}

button {
  position: relative;

  display: flex;
  align-items: flex-end;
  justify-content: flex-end;

  padding: 0;

  border: 0;
  background: transparent;

  font-size: inherit;
  font-family: inherit;

  cursor: pointer;
  outline: none;
  vertical-align: middle;
  text-decoration: none;
  transition: 3s;
}

button.new-project .circle {
  position: relative;

  display: flex;
  align-items: center;

  padding: 0 5px 0 9px;
  margin: 0;
  width: 32px;
  height: 30px;

  background: var(--icon-bg-color);
  border-radius: 1.625rem;
  color: var(--primary-text-color);

  transition: all 0.45s cubic-bezier(0.65, 0, 0.076, 1);
}

button.new-project .button-text {
  position: absolute;
  top: 50%;
  left: 60%;
  transform: translate(-50%, -50%);

  text-align: center;

  opacity: 0;
  z-index: 2;
  transition: all 0.45s cubic-bezier(0.65, 0, 0.076, 1);
}

button:hover .circle {
  width: 100%;
  background: var(--primary-button-color);
}

button:hover .button-text {
  opacity: 1;
  color: var(--primary-text-color);
}

.tooltip-item {
  display: flex;
  align-items: center;
  gap: 5px;

  &:first-child {
    margin-bottom: 6px;
  }

  &:hover {
    color: var(--primary-button-color);
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
