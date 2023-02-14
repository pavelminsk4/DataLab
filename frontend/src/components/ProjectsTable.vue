<template>
  <BaseTable v-if="workspaces" :table-header="tableHeader">
    <TableRow
      v-for="(item, index) in values"
      :key="index"
      v-model="selectedProjects[`project${item.id}`]"
      @delete-project="toggleDeleteModal(item.title, item.id)"
    >
      <td class="td_name">{{ item.title }}</td>
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
      <td class="project-creation-date">
        {{ projectCreationDate(item.created_at) }}
      </td>
    </TableRow>
  </BaseTable>

  {{ selectedProjects }}

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

import MembersIconsBar from '@components/MembersIconsBar.vue'
import TagsCollapsible from '@components/TagsCollapsible.vue'
import AreYouSureModal from '@/components/modals/AreYouSureModal'
import BaseTable from '@components/BaseTable'
import TableRow from '@components/TableRow'

export default {
  name: 'ProjectsTable',
  components: {
    AreYouSureModal,
    MembersIconsBar,
    TagsCollapsible,
    BaseTable,
    TableRow,
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
      selectedProjects: {},
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
  created() {
    this.tableHeader = [
      {name: 'name', width: ''},
      {name: 'keywords', width: '20%'},
      {name: 'creator', width: '16%'},
      {name: 'assigned user', width: '11%'},
      {name: 'date', width: '11%'},
    ]
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
  border: 1px solid var(--typography-secondary-color);

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

.project-creation-date {
  font-weight: 600;
}
</style>
