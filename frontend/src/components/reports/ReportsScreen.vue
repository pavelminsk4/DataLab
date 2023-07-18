<template>
  <MainLayout>
    <div class="content-header">
      <MainLayoutTitleBlock
        title="Reports"
        description="Set up and manage reports"
        :back-page="{name: 'main page', routeName: 'MainView'}"
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
        <BaseTable :table-header="tableHeader" @select-all="selectAll">
          <BaseTableRow
            v-for="(item, index) in filteredReports"
            :key="index"
            v-model="selectedReport"
            :id="item.id"
            class="report-table"
            @delete-entity="toggleDeleteModal(item.title, item.id)"
            @click="goToReport($event, item.id)"
          >
            <td class="td_name">{{ item.title }}</td>
            <td class="regularity">
              <div
                v-for="(reportType, index) in getReportTypes(item)"
                :key="`report-type-${index}`"
                class="report-type"
              >
                {{ reportType.type }}
              </div>
            </td>
            <td>
              <div
                v-for="(reportType, index) in getReportTypes(item)"
                :key="`report-type-${index}`"
                class="report-type"
              >
                {{ reportType.date }}
              </div>
            </td>
            <td>
              <div
                v-for="(reportType, index) in getReportTypes(item)"
                :key="`report-type-${index}`"
                class="report-type"
              >
                {{ reportType.time }}
              </div>
            </td>
            <td>{{ item.report_language }}</td>
            <td>
              <BaseChips :chipsType="item.report_format">
                {{ item.report_format.toUpperCase() }}
              </BaseChips>
            </td>
            <td>
              <UsersIconsBar :users="item.user" />
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
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import {weekDays} from '@/lib/constants'

import SortIcon from '@components/icons/SortIcon'

import BaseButton from '@/components/common/BaseButton'
import BaseInput from '@/components/common/BaseInput'
import MainLayout from '@components/layout/MainLayout'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import UsersIconsBar from '@components/UsersIconsBar'
import AreYouSureModal from '@/components/modals/AreYouSureModal'
import BaseTable from '@components/common/BaseTable'
import BaseTableRow from '@components/common/BaseTableRow'
import UserAvatar from '@components/UserAvatar'
import BaseChips from '@/components/BaseChips'

export default {
  name: 'ReportsScreen',
  components: {
    BaseButton,
    BaseInput,
    MainLayout,
    MainLayoutTitleBlock,
    AreYouSureModal,
    UsersIconsBar,
    BaseTable,
    BaseTableRow,
    UserAvatar,
    SortIcon,
    BaseChips,
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
    ...mapGetters({
      department: get.DEPARTMENT,
    }),
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
    ...mapActions([action.DELETE_REGULAR_REPORT]),
    goToReport(event, reportId) {
      if (!event.target.closest('.checkbox-container')) {
        return reportId
      }
    },
    selectAll(isSelectAll) {
      this.selectedReport = isSelectAll
        ? this.filteredReports.map((value) => value.id)
        : []
    },
    deleteReport(id) {
      this[action.DELETE_REGULAR_REPORT]({
        departmentId: this.department.id,
        regularReportId: id,
      })
      this.toggleDeleteModal()
    },
    toggleDeleteModal(title, id) {
      this.isOpenDeleteModal = !this.isOpenDeleteModal
      this.togglePageScroll(this.isOpenDeleteModal)
      this.reportValue.name = title
      this.currentReportId = id
    },
    getReportTypes(report) {
      const reportsTypes = []
      if (report.hourly_enabled)
        reportsTypes.push({
          type: 'Hourly',
          time: `every ${report.h_hour}h`,
          date: '',
        })
      if (report.daily_enabled)
        reportsTypes.push({
          type: 'Daily',
          time: this.getTime(report.d_hour, report.d_minute),
          date: 'every day',
        })
      if (report.weekly_enabled)
        reportsTypes.push({
          type: 'Weekly',
          time: this.getTime(report.w_hour, report.w_minute),
          date: this.getDayWeek(report.w_day_of_week),
        })
      if (report.monthly_enabled)
        reportsTypes.push({
          type: 'Monthly',
          time: this.getTime(report.m_hour, report.m_minute),
          date: this.getDate(report.m_day_of_month),
        })

      return reportsTypes
    },
    addZero(number) {
      return number.length === 1 ? `0${number}` : number
    },
    getTime(hours, minutes) {
      if (hours === '*') return ''

      const currentHours = hours === '12' ? '12' : this.addZero(hours % 12)
      const meridiem = hours > 12 ? 'pm' : 'am'
      return `${currentHours}:${this.addZero(minutes)} ${meridiem}`
    },
    getDayWeek(numberOfDay) {
      const index = +numberOfDay === 7 ? '0' : numberOfDay
      return weekDays[index]
    },
    getDate(numberOfMonth) {
      const currentDate = new Date()
      const today = currentDate.getDate()
      const month = currentDate.getMonth()
      const isPast = today > numberOfMonth
      // TODO: add condition for =
      currentDate.setDate(numberOfMonth)
      if (isPast) {
        currentDate.setMonth(+month + 1)
      }
      return currentDate.toDateString()
    },
  },
}
</script>

<style lang="scss" scoped>
.report-type {
  min-height: 20px;

  &:not(:last-child) {
    margin-bottom: 20px;
  }
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
  vertical-align: top;
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
  font-weight: 600;
}
</style>
