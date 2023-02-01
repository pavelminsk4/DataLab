<template>
  <table v-if="workspaces" class="table">
    <thead>
      <tr>
        <th class="th-type">TYPE</th>
        <th class="th-name">NAME</th>
        <th class="th-keywords">KEYWORDS</th>
        <th class="th-creator">CREATOR</th>
        <th class="th-assigned-user">ASSIGNED USERS</th>
        <th class="th-date">DATE</th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="(item, index) in values"
        :key="index"
        @click="goToProject(item.id)"
      >
        <td>
          <div class="type">
            <component class="type-icon" :is="item.source + 'RadioIcon'" />
            {{ item.source }}
          </div>
        </td>
        <td>{{ item.title }}</td>
        <td>
          <TagsCollapsible v-if="item.keywords.length" :tags="item.keywords" />
        </td>
        <td>
          <div class="creator">
            <img
              :src="currentMember(item.creator).user_profile.photo"
              class="cart-image"
            />
            <div>{{ currentMember(item.creator).username }}</div>
          </div>
        </td>
        <td>
          <MembersIconsBar :members="projectMembers(item.members)" />
        </td>
        <td>{{ projectCreationDate(item.created_at) }}</td>
        <td>
          <BaseTooltipSettings :id="item.id">
            <div
              @click.stop="toggleDeleteModal(item.title, item.id)"
              class="tooltip-item"
            >
              <DeleteIcon />Delete
            </div>
          </BaseTooltipSettings>
        </td>
      </tr>
    </tbody>
  </table>

  <AreYouSureModal
    v-if="isOpenDeleteModal"
    :item-to-delete="projectValue"
    @close="toggleDeleteModal"
    @delete="deleteProject(projectId)"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import CheckRadioIcon from '@/components/icons/CheckIcon'
import OnlineIcon from '@/components/icons/OnlineIcon'
import PremiumRadioIcon from '@/components/icons/PremiumRadioIcon'
import SocialRadioIcon from '@/components/icons/SocialRadioIcon'

import MembersIconsBar from '@components/MembersIconsBar.vue'
import TagsCollapsible from '@components/TagsCollapsible.vue'
import BaseTooltipSettings from '@/components/BaseTooltipSettings'
import DeleteIcon from '@/components/icons/DeleteIcon'
import AreYouSureModal from '@/components/modals/AreYouSureModal'

export default {
  name: 'ProjectsTable',
  components: {
    AreYouSureModal,
    DeleteIcon,
    BaseTooltipSettings,
    CheckRadioIcon,
    MembersIconsBar,
    OnlineIcon,
    PremiumRadioIcon,
    TagsCollapsible,
    SocialRadioIcon,
  },
  emits: ['go-to-project'],
  props: {
    values: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      selectedProjects: [],
      isOpenSettings: false,
      isOpenDeleteModal: false,
      projectId: '',
      projectValue: {
        type: 'project',
      },
    }
  },
  computed: {
    ...mapGetters({
      workspaces: get.WORKSPACES,
    }),
    currentWorkspace() {
      return this.workspaces.find(
        (el) => el.id === +this.$route.params.workspaceId
      )
    },
    members() {
      return this.currentWorkspace.members
    },
  },
  methods: {
    ...mapActions([action.DELETE_PROJECT]),
    currentMember(id) {
      return this.members.find((el) => el.id === id)
    },
    projectMembers(projectMembersIds) {
      return this.members.filter((member) =>
        projectMembersIds.includes(member.id)
      )
    },
    projectCreationDate(date) {
      return new Date(date).toLocaleDateString('ro-RO')
    },
    goToProject(id) {
      this.$emit('go-to-project', id)
    },
    deleteProject(id) {
      this[action.DELETE_PROJECT](id)
      this.toggleDeleteModal()
    },
    toggleDeleteModal(title, id) {
      this.isOpenDeleteModal = !this.isOpenDeleteModal
      this.togglePageScroll(this.isOpenDeleteModal)
      this.projectValue.name = title
      this.projectId = id
    },
  },
}
</script>

<style lang="scss" scoped>
.table {
  width: 100%;

  border-collapse: separate;
  border-spacing: 0;

  cursor: pointer;

  .th-type {
    width: 13%;
  }
  .th-name {
    width: 16%;
  }
  .th-keywords {
    width: 20%;
  }
  .th-creator {
    width: 16%;
  }
  .th-assigned-user {
    width: 11%;
  }
  .th-date {
    width: 11%;
  }

  thead {
    tr {
      th {
        padding-bottom: 10px;

        text-align: left;

        font-style: normal;
        font-weight: 400;
        font-size: 10px;
        line-height: 20px;
        color: var(--secondary-text-color);
      }

      th:first-child {
        padding: 0 0 0 29px;
      }
    }
  }

  tbody {
    tr {
      background: var(--secondary-bg-color);

      &:hover {
        background: var(--hover-circle-gradient);
        background-size: 200%;
        animation: var(--animation-hover-gradient);
        -webkit-animation: var(--animation-hover-gradient);
      }

      td {
        padding: 20px 5px;

        border-top: 1px solid var(--border-color);

        font-style: normal;
        font-weight: 400;
        font-size: 14px;
        line-height: 20px;
        color: var(--primary-text-color);
        word-break: break-word;

        &:first-child {
          padding: 15px 5px 15px 29px;

          border-left: 1px solid var(--border-color);
        }

        &:last-child {
          border-right: 1px solid var(--border-color);
        }
      }
    }

    tr:first-child td {
      &:first-child {
        border-left: 1px solid var(--border-color);
        border-top-left-radius: 15px;
      }
      &:last-child {
        border-right: 1px solid var(--border-color);
        border-top-right-radius: 15px;
      }
    }

    tr:last-child td {
      border-bottom: 1px solid var(--border-color);

      &:first-child {
        border-left: 1px solid var(--border-color);
        border-bottom: 1px solid var(--border-color);
        border-bottom-left-radius: 15px;
      }
      &:last-child {
        border-right: 1px solid var(--border-color);
        border-bottom: 1px solid var(--border-color);
        border-bottom-right-radius: 15px;
      }
    }
  }
}

.checkmark {
  position: absolute;
  top: 0;
  left: 0;

  display: flex;
  align-items: center;
  justify-content: center;

  height: 20px;
  width: 20px;

  border: 1px solid #9198a7;
  border-radius: 4px;
  background-color: var(--border-color);
}

.type-icon {
  margin-right: 10px;
}

.type {
  display: flex;
  align-items: center;
}

.creator {
  display: flex;
}

.cart-image {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-grow: 0;
  flex-shrink: 0;

  width: 22px;
  height: 22px;
  margin-right: 12px;

  border-radius: 100%;
  border: 1px solid var(--secondary-text-color);

  background-color: white;

  font-size: 10px;

  &:not(:first-child) {
    margin-left: -10px;
  }
}

.tooltip-item {
  display: flex;
  align-items: center;
  gap: 5px;

  &:hover {
    color: var(--button-primary-color);
  }
}
</style>
