<template>
  <MainLayout>
    <div class="content-header">
      <MainLayoutTitleBlock
        title="Reports"
        description="Set up and manage reports"
        :back-page="{name: 'main page', routName: 'MainView'}"
      />

      <BaseButton @click="$emit('create-report')">
        Create new report
      </BaseButton>
    </div>

    <AreYouSureModal
      v-if="isOpenDeleteModal"
      :item-to-delete="reportValue"
      @close="toggleDeleteModal"
      @delete="deleteReport(currentReportId)"
    />

    <template v-if="reports.length">
      <div class="sort-wrapper">
        <span class="hint">Sort by</span>
        <div class="sort-option">Latest <SortIcon class="sort-icon" /></div>

        <BaseInput
          v-model="search"
          placeholder="Search users..."
          :isSearch="true"
        />
      </div>

      <div class="list-wrapper scroll">
        <BaseTable
          :table-header="tableHeader"
          class="redssd"
          @select-all="selectAll"
        >
          <BaseTableRow
            v-for="(item, index) in filteredReports"
            :key="index"
            v-model="selectedReport"
            :id="item.id"
            class="report-table"
            @delete-project="toggleDeleteModal(item.title, item.id)"
            @click="goToReport($event, item.id)"
          >
            <td class="td_name">{{ item.title }}</td>
            <td class="regularity">
              <div class="test">type</div>
              <div class="test">type</div>
              <div class="test">type</div>
              <div class="test">type</div>
            </td>
            <td>date</td>
            <td>time</td>
            <td>language</td>
            <td>format</td>
            <td>
              <!-- <UsersIconsBar :users="users(item.members)" /> -->
            </td>
            <td>
              <div class="creator">
                <!-- <UserAvatar
                  :avatar-url="currentUser(item.creator)?.user_profile.photo"
                  :first-name="currentUser(item.creator)?.first_name"
                  :last-name="currentUser(item.creator)?.last_name"
                  :username="currentUser(item.creator)?.username"
                /> -->
                <!-- <div>{{ currentUser(item.creator).username }}</div> -->
              </div>
            </td>
          </BaseTableRow>
        </BaseTable>
      </div>
    </template>

    <div v-else class="no-reports-wrapper">
      <img src="@/assets/reports/no-reports.svg" alt="No reports image" />
      <div>No reports created &#x1F4E8;</div>
    </div>
  </MainLayout>
</template>

<script>
import SortIcon from '@components/icons/SortIcon'

import BaseButton from '@/components/common/BaseButton'
import BaseInput from '@/components/common/BaseInput'
import MainLayout from '@components/layout/MainLayout'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
// import UsersIconsBar from '@components/UsersIconsBar.vue'
import AreYouSureModal from '@/components/modals/AreYouSureModal'
import BaseTable from '@components/common/BaseTable'
import BaseTableRow from '@components/common/BaseTableRow'
// import UserAvatar from '@components/UserAvatar'

export default {
  name: 'ReportsScreen',
  components: {
    BaseButton,
    BaseInput,
    MainLayout,
    MainLayoutTitleBlock,
    AreYouSureModal,
    // UsersIconsBar,
    BaseTable,
    BaseTableRow,
    // UserAvatar,
    SortIcon,
  },
  props: {
    reports: {type: Array, default: () => []},
  },
  data() {
    return {
      search: '',
      isOpenDeleteModal: false,
      selectedReport: [],
      isOpenSettings: false,
      currentReportId: '',
      reportValue: {
        type: 'report',
        name: '',
      },
    }
  },
  computed: {
    filteredReports() {
      if (!this.search) return this.reports
      return this.reports?.filter((report) =>
        report.title.toLowerCase().includes(this.search.toLowerCase())
      )
    },
  },
  created() {
    this.tableHeader = [
      {name: 'report name', width: '25%'},
      {name: 'type', width: ''},
      {name: `date`, width: ''},
      {name: `time`, width: ''},
      {name: `language`, width: ''},
      {name: `format`, width: ''},
      {name: `recipient's `, width: ''},
      {name: `creator `, width: ''},
    ]
  },
  methods: {
    goToReport(event, reportId) {
      if (!event.target.closest('.checkbox-container')) {
        // this.$emit('open-report', reportId)
        return reportId
      }
    },
    selectAll(isSelectAll) {
      this.selectedReport = isSelectAll
        ? this.filteredReports.map((value) => value.id)
        : []
    },
    deleteReport(id) {
      this.toggleDeleteModal()
      return id
    },
    toggleDeleteModal(title, id) {
      this.isOpenDeleteModal = !this.isOpenDeleteModal
      this.togglePageScroll(this.isOpenDeleteModal)
      this.reportValue.name = title
      this.currentReportId = id
    },

    //change
    currentUser(id) {
      return this.members.find((el) => el.id === id)
    },
    users(usersIds) {
      return this.members.filter((member) => usersIds.includes(member.id))
    },
  },
}
</script>

<style lang="scss" scoped>
.test {
  padding: 10px 0;
}
.content-header {
  display: flex;
  justify-content: space-between;
}

.sort-wrapper {
  display: flex;
  align-items: center;

  margin-bottom: 22px;
}

.hint {
  color: var(--typography-secondary-color);
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

.list-wrapper {
  height: calc(100% - 200px);
}

.report-table td {
  vertical-align: initial;
}

.no-reports-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;

  width: 100%;
}

.creator {
  display: flex;
  align-items: center;
}

.regularity {
  display: flex;
  flex-direction: column;
}
</style>
