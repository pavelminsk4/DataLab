<template>
  <BaseTable :table-header="tableHeader" @select-all="selectAll">
    <BaseTableRow
      v-for="(item, index) in values"
      :key="index"
      v-model="selectedProjects"
      :id="item.id"
      @delete-project="toggleDeleteModal(item.title, item.id)"
      @click="goToEntityPage($event, item.id)"
    >
      <td class="td_name">{{ item.title }}</td>
      <td>
        <TagsCollapsible v-if="item.keywords.length" :tags="item.keywords" />
      </td>
      <td>
        <div class="creator">
          <UserAvatar
            :avatar-url="currentUser(item.creator)?.user_profile.photo"
            :first-name="currentUser(item.creator)?.first_name"
            :last-name="currentUser(item.creator)?.last_name"
            :username="currentUser(item.creator)?.username"
          />
          <div>{{ currentUser(item.creator).username }}</div>
        </div>
      </td>
      <td>
        <UsersIconsBar :users="users(item.members)" />
      </td>
      <td class="project-creation-date">
        {{ creationDate(item.created_at) }}
      </td>
    </BaseTableRow>
  </BaseTable>

  <AreYouSureModal
    v-if="isOpenDeleteModal"
    :item-to-delete="projectValue"
    @close="toggleDeleteModal"
    @delete="deleteEntity(projectId)"
  />
</template>

<script>
import UsersIconsBar from '@components/UsersIconsBar.vue'
import TagsCollapsible from '@components/TagsCollapsible.vue'
import AreYouSureModal from '@/components/modals/AreYouSureModal'
import BaseTable from '@components/common/BaseTable'
import BaseTableRow from '@components/common/BaseTableRow'
import UserAvatar from '@components/UserAvatar'

export default {
  name: 'ProjectsTable',
  components: {
    AreYouSureModal,
    UsersIconsBar,
    TagsCollapsible,
    BaseTable,
    BaseTableRow,
    UserAvatar,
  },
  emits: ['go-to-entity'],
  props: {
    values: {type: Array, default: () => []},
    members: {type: Array, default: () => []},
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
  created() {
    this.tableHeader = [
      {name: 'project name', width: ''},
      {name: 'keywords', width: '20%'},
      {name: 'creator', width: '16%'},
      {name: 'assigned user', width: '11%'},
      {name: 'date', width: '11%'},
    ]
  },
  methods: {
    currentUser(id) {
      return this.members.find((el) => el.id === id)
    },
    users(usersIds) {
      return this.members.filter((member) => usersIds.includes(member.id))
    },
    creationDate(date) {
      return new Date(date).toLocaleDateString('ro-RO')
    },
    goToEntityPage(event, id) {
      if (!event.target.closest('.checkbox-container')) {
        this.$emit('go-to-entity', id)
      }
    },
    deleteEntity(id) {
      this.$emit('delete-entity', id)
      this.toggleDeleteModal()
    },
    toggleDeleteModal(title, id) {
      this.isOpenDeleteModal = !this.isOpenDeleteModal
      this.togglePageScroll(this.isOpenDeleteModal)
      this.projectValue.name = title
      this.projectId = id
    },
    selectAll(isSelectAll) {
      this.selectedProjects = isSelectAll
        ? this.values.map((value) => value.id)
        : []
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
  align-items: center;
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
