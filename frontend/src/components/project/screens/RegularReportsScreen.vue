<template>
  <NavigationBar
    v-if="currentProject"
    :title="currentProject.title"
    hint="Set up and manage reports"
  >
    <BaseButton @click="goToCreateRegularReport" class="new-report-button">
      Create New Report
    </BaseButton>
  </NavigationBar>

  <BaseTable v-if="reports.length" :table-header="tableHeader">
    <BaseTableRow
      v-for="(item, index) in reports"
      :key="'alert' + index"
      @click="goToUpdateReport(item.id)"
    >
      <td>
        {{ item.title }}
      </td>
      <td>
        {{ getReportTypes(item) }}
      </td>
      <td>
        <UsersIconsBar :users="alertUsers(item.user)" />
      </td>
    </BaseTableRow>
  </BaseTable>

  <BlankPage v-else page-name="RegularReports" />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseButton from '@/components/common/BaseButton'
import UsersIconsBar from '@components/UsersIconsBar.vue'
import NavigationBar from '@/components/navigation/NavigationBar'
import BlankPage from '@/components/BlankPage'
import BaseTable from '@components/common/BaseTable'
import BaseTableRow from '@components/common/BaseTableRow'

export default {
  name: 'RegularReportsScreen',
  components: {
    BlankPage,
    BaseButton,
    UsersIconsBar,
    NavigationBar,
    BaseTable,
    BaseTableRow,
  },
  props: {
    currentProject: {
      type: [Array, Object],
      required: true,
    },
  },
  computed: {
    ...mapGetters({
      reports: get.REGULAR_REPORTS,
      workspaces: get.WORKSPACES,
    }),
    workspaceMembers() {
      return this.workspaces.find(
        (el) => el.id === +this.$route.params.workspaceId
      ).members
    },
  },
  created() {
    this.tableHeader = [
      {name: 'name', width: '40%'},
      {name: 'types', width: '30%'},
      {name: `recipient's`, width: '30%'},
    ]

    if (!this.reports.length) {
      this[action.GET_REGULAR_REPORTS](this.currentProject.id)
    }
  },
  methods: {
    ...mapActions([action.GET_REGULAR_REPORTS, action.GET_COMPANY_USERS]),
    goToCreateRegularReport() {
      this.$router.push({
        name: 'NewRegularReport',
      })
    },
    goToUpdateReport(id) {
      this.$router.push({
        name: 'UpdateRegularReport',
        params: {
          regularReportId: id,
        },
      })
    },
    alertUsers(alertUsersIds) {
      return this.workspaceMembers.filter((user) =>
        alertUsersIds.includes(user.id)
      )
    },
    getReportTypes(item) {
      const types = []
      if (item.hourly_enabled) types.push('Hourly')
      if (item.daily_enabled) types.push('Daily')
      if (item.weekly_enabled) types.push('Weekly')
      if (item.monthly_enabled) types.push('Monthly')
      return types.join(', ')
    },
  },
}
</script>

<style lang="scss" scoped>
.new-report-button {
  width: 176px;
  gap: 8px;
}
</style>
