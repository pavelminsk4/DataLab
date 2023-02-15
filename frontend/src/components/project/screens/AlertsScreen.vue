<template>
  <NavigationBar
    v-if="currentProject"
    :title="currentProject.title"
    hint="Set up alerts for your project with highly customized filters"
  >
    <BaseButton @click="goToCreateAlert" class="button">
      <PlusIcon /> Create New Alert
    </BaseButton>
  </NavigationBar>

  <BaseTable v-if="alerts.length" :table-header="tableHeader">
    <TableRow
      v-for="(item, index) in alerts"
      :key="'alert' + index"
      @click="goToUpdateAlert(item.id)"
    >
      <td>
        {{ item.title }}
      </td>
      <td>
        <span>{{ item.how_many_posts_to_send }}</span>
        <span>{{ item.triggered_on_every_n_new_posts }}</span>
      </td>
      <td>
        <MembersIconsBar :members="alertsUsers(item.user)" />
      </td>
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
    </TableRow>
  </BaseTable>
  <BlankPage v-else page-name="Alerts" />

  <AreYouSureModal
    v-if="isOpenDeleteModal"
    :item-to-delete="alertValue"
    @close="toggleDeleteModal"
    @delete="deleteAlert(currentAlertId)"
  />
</template>
<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BlankPage from '@/components/BlankPage'
import BaseButton from '@/components/buttons/BaseButton'
import MembersIconsBar from '@components/MembersIconsBar.vue'
import NavigationBar from '@/components/navigation/NavigationBar'
import BaseTooltipSettings from '@/components/BaseTooltipSettings'

import PlusIcon from '@/components/icons/PlusIcon'
import DeleteIcon from '@/components/icons/DeleteIcon'
import AreYouSureModal from '@/components/modals/AreYouSureModal'
import BaseTable from '@components/BaseTable'
import TableRow from '@components/TableRow'

export default {
  name: 'AlertsScreen',
  components: {
    BlankPage,
    AreYouSureModal,
    DeleteIcon,
    BaseTooltipSettings,
    PlusIcon,
    BaseButton,
    NavigationBar,
    MembersIconsBar,
    BaseTable,
    TableRow,
  },
  props: {
    currentProject: {
      type: [Array, Object],
      required: true,
    },
  },
  data() {
    return {
      isOpenDeleteModal: false,
      currentAlertId: '',
      alertValue: {
        type: 'alert',
      },
    }
  },
  computed: {
    ...mapGetters({
      alerts: get.ALERTS,
      workspaces: get.WORKSPACES,
    }),
    currentWorkspace() {
      return this.workspaces.find(
        (el) => el.id === +this.$route.params.workspaceId
      )
    },
    workspaceMembers() {
      return this.currentWorkspace.members
    },
  },
  created() {
    this.tableHeader = [
      {name: 'name', width: ''},
      {name: 'conditions', width: ''},
      {name: 'assigned user', width: ''},
    ]

    this[action.GET_ALERTS](this.currentProject.id)
  },
  methods: {
    ...mapActions([action.GET_ALERTS, action.DELETE_ALERT]),
    goToCreateAlert() {
      this.$router.push({
        name: 'NewAlert',
      })
    },
    goToUpdateAlert(id) {
      this.$router.push({
        name: 'UpdateAlert',
        params: {
          alertId: id,
        },
      })
    },
    alertsUsers(alertsUsersIds) {
      return this.workspaceMembers.filter((member) =>
        alertsUsersIds.includes(member.id)
      )
    },
    deleteAlert(id) {
      this[action.DELETE_ALERT]({
        alertId: id,
        projectId: this.currentProject.id,
      })
      this.toggleDeleteModal()
    },
    toggleDeleteModal(title, id) {
      this.isOpenDeleteModal = !this.isOpenDeleteModal
      this.togglePageScroll(this.isOpenDeleteModal)
      this.alertValue.name = title
      this.currentAlertId = id
    },
  },
}
</script>

<style lang="scss" scoped>
.button-icon {
  margin-right: 7px;
}

.type-icon {
  margin-right: 10px;
}

.type {
  display: flex;
  align-items: center;
}

.button {
  width: 176px;
  gap: 8px;
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
