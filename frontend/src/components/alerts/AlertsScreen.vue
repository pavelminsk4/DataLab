<template>
  <MainLayout>
    <div class="header">
      <MainLayoutTitleBlock
        title="Alerts"
        description="Set up alerts for your project with highly customized filters"
        :back-page="{name: 'main page', routName: 'MainView'}"
      />

      <BaseButton @click="$emit('create-alert')"> Create new alert </BaseButton>
    </div>

    <AreYouSureModal
      v-if="isOpenDeleteModal"
      :item-to-delete="alertToDelete"
      @close="toggleDeleteModal"
      @delete="deleteAlert(alertId)"
    />

    <template v-if="alerts.length">
      <div class="table-wrapper scroll">
        <BaseTable :table-header="tableHeader">
          <BaseTableRow
            v-for="(alert, index) in alerts"
            :key="index"
            v-model="selectedAlerts"
            :id="alert.id"
            class="alert-table"
            @delete-entity="toggleDeleteModal(alert.title, alert.id)"
            @click="goToAlert($event, alert.id)"
          >
            <td class="alert__name">{{ alert.title }}</td>
            <td class="alert__trigger">
              {{ alertTriggerCount(alert.triggered_on_every_n_new_posts) }}
            </td>
            <td>
              <UsersIconsBar :users="alert.user" />
            </td>
            <td>
              <div class="creator">
                <UserAvatar
                  :avatar-url="alert.creator?.user_profile.photo"
                  :first-name="alert.creator?.first_name"
                  :last-name="alert.creator?.last_name"
                  :username="alert.creator?.username"
                />
                <div>{{ alert.creator?.username }}</div>
              </div>
            </td>
            <td>
              <div :key="alert.id" class="alert__date">
                {{ getDateFormat(alert.updated_at) }}
              </div>
            </td>
          </BaseTableRow>
        </BaseTable>
      </div>
    </template>
    <div v-else class="no-alerts">
      <img src="@/assets/alerts/no-alerts.svg" alt="No alerts image" />
      <div class="no-alerts__text">
        No alerts created
        <img
          src="@/assets/alerts/mailbox.svg"
          alt="open mailbox with raised flag image"
        />
      </div>
    </div>
  </MainLayout>
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import MainLayout from '@/components/layout/MainLayout'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import BaseTable from '@/components/common/BaseTable'
import BaseTableRow from '@/components/common/BaseTableRow'
import BaseButton from '@/components/common/BaseButton'
import UsersIconsBar from '@components/UsersIconsBar'
import UserAvatar from '@components/UserAvatar'
import AreYouSureModal from '@/components/modals/AreYouSureModal'

export default {
  name: 'AlertsScreen',
  components: {
    MainLayout,
    MainLayoutTitleBlock,
    BaseButton,
    BaseTable,
    BaseTableRow,
    UsersIconsBar,
    UserAvatar,
    AreYouSureModal,
  },
  props: {
    alerts: {type: Array, default: () => []},
  },
  data() {
    return {
      isOpenDeleteModal: false,
      selectedAlerts: [],
      alertToDelete: {
        type: 'alert',
        name: '',
      },
      alertId: 0,
    }
  },
  computed: {
    ...mapGetters({
      department: get.DEPARTMENT,
    }),
  },
  created() {
    this.tableHeader = [
      {name: 'Alert name', width: '25%'},
      {name: 'Trigger', width: ''},
      {name: `Assigned Users`, width: ''},
      {name: `Creator `, width: ''},
      {name: `Date`, width: ''},
    ]
  },
  methods: {
    ...mapActions([action.DELETE_ALERT]),
    alertTriggerCount(count) {
      return `Every ${count} new ${count < 2 ? 'post' : 'posts'}`
    },
    goToAlert(event, alertId) {
      if (!event.target.closest('.checkbox-container')) {
        return alertId
      }
    },
    getDateFormat(date) {
      let formattedDate = new Date(date).toDateString().split(' ')
      return `${formattedDate[1]} ${formattedDate[2]}, ${formattedDate[3]}`
    },
    toggleDeleteModal(title, id) {
      this.isOpenDeleteModal = !this.isOpenDeleteModal
      this.togglePageScroll(this.isOpenDeleteModal)
      this.alertToDelete.name = title
      this.alertId = id
    },
    deleteAlert(id) {
      this[action.DELETE_ALERT]({
        projectId: this.department.id,
        alertId: id,
      })
      this.toggleDeleteModal()
    },
  },
}
</script>

<style lang="scss" scoped>
.header {
  display: flex;
  justify-content: space-between;
}

.no-alerts {
  display: flex;
  align-items: center;
  flex-direction: column;

  gap: 30px;

  &__text {
    display: flex;

    gap: 10px;
  }
}
.table-wrapper {
  height: calc(100% - 200px);
  .alert-table td {
    vertical-align: initial;
  }
}

.creator {
  display: flex;
  align-items: center;
}
</style>
