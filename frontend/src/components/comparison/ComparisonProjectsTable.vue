<template>
  <BaseTable
    :table-header="tableHeader"
    :selected-items="selectedProjects"
    @select-all="selectAll"
  >
    <BaseTableRow
      v-for="(item, index) in valuesProxy"
      :key="index"
      v-model="selectedProjects"
      :id="item.id"
      @delete-entity="toggleDeleteModal(item.title, item.id)"
      @click="goToProject($event, item.id)"
    >
      <td class="td_name">{{ item.title }}</td>
      <td
        v-for="project in item.cmpr_items"
        :key="project.id"
        class="competitor-project"
      >
        {{ project.project_name }}
      </td>
      <td>
        <div class="creator">
          <UserAvatar
            :avatar-url="item.creator?.user_profile.photo"
            :first-name="item.creator?.first_name"
            :last-name="item.creator?.last_name"
            :username="item.creator?.username"
          />
          <div>{{ item.creator?.username }}</div>
        </div>
      </td>

      <td class="td_name">
        {{ defaultDate(item.created_at, platformLanguage) }}
      </td>
    </BaseTableRow>
  </BaseTable>

  <AreYouSureModal
    v-if="isOpenDeleteModal"
    :item-to-delete="projectValue"
    @close="toggleDeleteModal"
    @delete="deleteProject(projectId)"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'
import {defaultDate} from '@lib/utilities'

import AreYouSureModal from '@components/modals/AreYouSureModal'
import BaseTable from '@components/common/BaseTable'
import BaseTableRow from '@components/common/BaseTableRow'
import UserAvatar from '@components/UserAvatar'

const {mapActions} = createNamespacedHelpers('comparison')

export default {
  name: 'ComparisonProjectsTable',
  components: {
    AreYouSureModal,
    BaseTable,
    BaseTableRow,
    UserAvatar,
  },
  emits: ['go-to-project'],
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
  computed: {
    valuesProxy() {
      const emptyProject = {
        id: null,
        project_name: null,
        module_type: null,
        module_project_id: null,
        project: null,
      }
      return this.values.map((value) => {
        if (value.cmpr_items.length === 2) {
          value.cmpr_items.push(emptyProject)
        }
        return value
      })
    },
  },
  created() {
    this.tableHeader = [
      {name: 'Project name', width: ''},
      {name: 'Competitor project', width: '15%'},
      {name: 'Competitor project', width: '15%'},
      {name: 'Competitor project', width: '15%'},
      {name: 'Creator', width: '10%'},
      {name: 'Date', width: '10%'},
    ]
  },
  methods: {
    defaultDate,
    ...mapActions([action.DELETE_WORKSPACE_PROJECT]),
    projectCreationDate(date) {
      return new Date(date).toLocaleDateString('ro-RO')
    },
    goToProject(event, id) {
      if (!event.target.closest('.checkbox-container')) {
        this.$emit('go-to-project', id)
      }
    },
    deleteProject(projectId) {
      const {workspaceId} = this.$route.params
      this[action.DELETE_WORKSPACE_PROJECT]({workspaceId, projectId})
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

  border: var(--border-primary);
  border-radius: var(--border-radius);
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
