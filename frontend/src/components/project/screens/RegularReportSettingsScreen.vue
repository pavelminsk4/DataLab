<template>
  <div>
    <NavigationBar
      v-if="currentProject"
      :title="currentReport?.title || currentProject?.title"
      hint="Set up report for your project with highly customized filters"
    >
      <BaseButton
        v-if="this.$route.name === 'NewRegularReport'"
        @click="saveChanges"
        class="button"
      >
        Save
      </BaseButton>
      <BaseButton
        v-if="this.$route.name === 'UpdateRegularReport'"
        @click="updateRegularReport"
        class="button-update"
      >
        Update Regular Report
      </BaseButton>
    </NavigationBar>

    <section v-if="regularReports.length" class="create-report-section">
      <div class="create-report-wrapper">
        <div class="title">Regular Report Title</div>
        <BaseInput v-model="title" class="input-title" placeholder="Title" />

        <div class="title">Recipient's email</div>

        <div class="email-wrapper">
          <div :class="['email-field', visible && 'active-email-field']">
            <div
              v-for="(item, index) in selectedUsers || []"
              :key="item"
              :class="['selected-user', 'duplicate' && isDuplicate]"
            >
              {{ item.email }}
              <DeleteTagButton @click="removeTag(index)" />
            </div>
            <div @click="addUsers" class="add-users-button">
              Add Users <AddButtonIcon />
            </div>
          </div>

          <ul v-if="visible" class="select-list">
            <li
              v-for="(item, index) in projectMembers"
              :key="item.username + index"
              class="select-item"
              @click="select(item)"
            >
              {{ item.email }}
            </li>
          </ul>
        </div>

        <div class="title">Email Title</div>
        <BaseInput
          v-model="emailTitle"
          class="input-title"
          placeholder="Title"
        />
      </div>
      <TimePickerReports
        :regular-report="currentReport"
        @repeat-time="repeatTime"
        @update-time-daily="updateTimeDaily"
        @choose-weekly-day="chooseWeeklyDay"
        @update-time-weekly="updateTimeWeekly"
        @ending-date-hourly="endingDateHourly"
        @update-ending-date-hourly="updateEndingDateHourly"
        @update-time-monthly="updatePickerTimeMonthly"
        @select-hourly-template="selectHourlyTemplate"
      />
    </section>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseButton from '@/components/buttons/BaseButton'
import NavigationBar from '@/components/navigation/NavigationBar'
import TimePickerReports from '@/components/project/screens/TimePickerReports'
import DeleteTagButton from '@/components/icons/DeleteTagButton'
import AddButtonIcon from '@/components/icons/AddButtonIcon'
import BaseInput from '@/components/BaseInput'

export default {
  name: 'RegularReportSettingsScreen',
  components: {
    TimePickerReports,
    BaseInput,
    AddButtonIcon,
    DeleteTagButton,
    BaseButton,
    NavigationBar,
  },
  data() {
    return {
      title: '',
      emailTitle: '',
      hour: '*',
      hourlyEnabled: false,
      endingTimeHourly: null,
      hourlyTemplate: '',
      dailyEnabled: false,
      endingTimeDaily: null,
      timePickerDailyValue: [],
      dailyTemplate: '',
      weeklyEnabled: false,
      dayOfWeek: '*',
      timePickerWeeklyValue: [],
      weeklyTemplate: '',
      endingTimeWeekly: null,
      dayOfMonth: '*',
      monthlyEnabled: false,
      timePickerMonthlyValue: [],
      endingTimeMonthly: null,
      monthlyTemplate: '',
      visible: false,
      isDuplicate: false,
      selectedUsers: [],
      usersId: [],
    }
  },
  async created() {
    if (!this.workspaces.length) {
      await this[action.GET_WORKSPACES]()
    }

    if (!this.regularReports.length) {
      await this[action.GET_REGULAR_REPORTS](this.projectId)
    }

    if (this.$route.name === 'UpdateRegularReport') {
      this.title = this.currentReport?.title
      this.emailTitle = this.currentReport?.email_title
    }

    if (
      this.projectMembers.length &&
      this.$route.name === 'UpdateRegularReport'
    ) {
      this.selectedUsers = [...this.reportUsers]
      this.usersId = [...this.reportUsersId]
    }

    document.addEventListener('click', this.close)
  },
  computed: {
    ...mapGetters({
      workspaces: get.WORKSPACES,
      loading: get.LOADING,
      regularReports: get.REGULAR_REPORTS,
    }),
    workspaceId() {
      return this.$route.params.workspaceId
    },
    projectId() {
      return this.$route.params.projectId
    },
    currentWorkspace() {
      return this.workspaces.filter((el) => el.id === +this.workspaceId)
    },
    workspaceMembers() {
      return this.currentWorkspace[0]?.members
    },
    currentProject() {
      return this.currentWorkspace[0]?.projects.filter(
        (el) => el.id === +this.projectId
      )[0]
    },
    projectMembers() {
      return this.workspaceMembers
        .filter((i) => this.currentProject.members.includes(i.id))
        .concat(
          this.currentProject.members.filter((i) =>
            this.workspaceMembers.includes(i.id)
          )
        )
    },
    projectMembersId() {
      return this.projectMembers.map((el) => el.id)
    },
    regularReportId() {
      return this.$route.params.regularReportId
    },
    currentReport() {
      return this.regularReports.filter(
        (el) => +el.id === +this.regularReportId
      )[0]
    },
    reportUsers() {
      return this.projectMembers
        .filter((i) => this.currentReport?.user.includes(i.id))
        .concat(
          this.currentReport?.user.filter((i) =>
            this.projectMembers.includes(i.id)
          )
        )
    },
    reportUsersId() {
      return this.reportUsers.map((el) => el.id)
    },
  },
  methods: {
    ...mapActions([
      action.GET_WORKSPACES,
      action.CREATE_NEW_REGULAR_REPORT,
      action.UPDATE_NEW_REGULAR_REPORT,
      action.GET_REGULAR_REPORTS,
    ]),
    repeatTime(val, name) {
      this.hourlyEnabled = true
      this.monthlyEnabled = true
      this[name] = val
    },
    updateTimeDaily(val) {
      this.dailyEnabled = true
      this.timePickerDailyValue = val
    },
    updateTimeWeekly(val) {
      this.timePickerWeeklyValue = val
    },
    chooseWeeklyDay(val) {
      this.weeklyEnabled = true
      this.dayOfWeek = val
    },
    updatePickerTimeMonthly(val) {
      this.timePickerMonthlyValue = val
    },
    endingDateHourly(val, name) {
      this[name] = val
    },
    updateEndingDateHourly(val, name) {
      this[name] = val
    },
    selectHourlyTemplate(val, name) {
      this[name] = val
    },
    async createRegularReport() {
      await this[action.CREATE_NEW_REGULAR_REPORT]({
        projectId: this.projectId,
        data: {
          title: this.title,
          project: this.projectId,
          email_title: this.emailTitle,
          h_hour: this.hour,
          h_minute: 0,
          hourly_enabled: this.hourlyEnabled,
          h_ending_date: this.endingTimeHourly,
          h_template: this.hourlyTemplate,
          daily_enabled: this.dailyEnabled,
          d_hour: this.timePickerDailyValue.hours,
          d_minute: this.timePickerDailyValue.minutes,
          d_ending_date: this.endingTimeDaily,
          d_template: this.dailyTemplate,
          weekly_enabled: this.weeklyEnabled,
          w_day_of_week: this.dayOfWeek,
          w_hour: this.timePickerWeeklyValue.hours,
          w_minute: this.timePickerWeeklyValue.minutes,
          w_ending_date: this.endingTimeWeekly,
          w_template: this.weeklyTemplate,
          m_day_of_month: this.dayOfMonth,
          monthly_enabled: this.monthlyEnabled,
          m_hour: this.timePickerMonthlyValue.hours,
          m_minute: this.timePickerMonthlyValue.minutes,
          m_ending_date: this.endingTimeMonthly,
          m_template: this.monthlyTemplate,
          user: [...this.usersId],
        },
      })

      this.loading = true
      await this[action.GET_REGULAR_REPORTS](this.projectId)
    },
    updateRegularReport() {
      this[action.UPDATE_NEW_REGULAR_REPORT]({
        projectId: this.projectId,
        regularReportId: this.$route.params.regularReportId,
        data: {
          title: this.title,
          project: this.projectId,
          email_title: this.emailTitle,
          user: [...this.usersId],
        },
      })
    },
    saveChanges() {
      if (this.$route.name === 'NewRegularReport') {
        this.createRegularReport()

        this.loading = true
        this.$router.push({
          name: 'Reports',
        })
      } else {
        this.updateRegularReport()

        this.$router.push({
          name: 'Reports',
        })
      }
    },
    addUsers() {
      this.visible = !this.visible
    },
    select(item) {
      if (this.usersId.includes(item.id)) {
        this.isDuplicate = true
      } else {
        this.usersId.push(item.id)
        this.selectedUsers.push(item)
      }
    },
    removeTag(index) {
      this.selectedUsers.splice(index, 1)
      this.usersId.splice(index, 1)
    },
    close() {
      const selectList = document.querySelectorAll('.email-wrapper')

      if (!Array.from(selectList).find((el) => el.contains(event.target))) {
        this.visible = false
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.create-report-section {
  display: flex;
  gap: 78px;
}

.create-report-wrapper {
  width: 100%;
  margin-top: 40px;

  .title {
    margin: 25px 0 14px;

    font-style: normal;
    font-weight: 500;
    font-size: 14px;
    line-height: 110%;
    color: var(--primary-text-color);
  }

  .additional-settings {
    display: flex;
    gap: 20px;
  }
}

.email-wrapper {
  .email-field {
    display: flex;
    gap: 8px;

    height: auto;
    width: 516px;
    padding: 8px;

    background: var(--secondary-bg-color);
    border: 1px solid var(--input-border-color);
    box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
    border-radius: 10px;

    overflow-y: hidden;
    overflow-x: auto;

    .selected-user {
      display: flex;
      align-items: center;
      gap: 6px;

      height: 25px;
      padding: 8px;

      border-radius: 8px;
      background-color: rgba(255, 255, 255, 0.2);

      cursor: pointer;

      font-style: normal;
      font-weight: 400;
      font-size: 14px;
      line-height: 20px;
      color: var(--primary-text-color);
    }

    .duplicate {
      color: var(--primary-text-color);

      background: var(--negative-status);
      animation: shake 1s;
    }
    .add-users-button {
      display: flex;
      align-items: center;
      flex-shrink: 0;
      gap: 6px;

      height: 25px;
      padding: 8px;

      border-radius: 8px;
      background-color: rgba(145, 152, 167, 0.2);

      cursor: pointer;

      font-style: normal;
      font-weight: 400;
      font-size: 14px;
      line-height: 20px;
      color: var(--secondary-text-color);

      &:hover {
        background-color: var(--hover-button-color);
      }
    }

    &::-webkit-scrollbar {
      height: 5px;
      width: 5px;
    }

    &::-webkit-scrollbar-track {
      background: var(--secondary-bg-color);
      border: 1px solid var(--input-border-color);
      border-radius: 0 10px 10px 0;
    }

    &::-webkit-scrollbar-thumb {
      height: 4px;

      background: var(--secondary-text-color);
      border-radius: 10px;
    }
  }

  .active-email-field {
    outline: 1px solid var(--primary-button-color);
    border-radius: 10px 10px 0 0;
  }

  .select-list {
    position: absolute;
    z-index: 1;

    padding: 0;
    margin: 0;
    width: 516px;
    max-height: 250px;

    outline: 1px solid var(--primary-button-color);
    border-top: 1px solid var(--modal-line-color);
    box-shadow: 0 3px 4px rgba(5, 95, 252, 0.49);
    border-radius: 0 0 10px 10px;
    background-color: var(--secondary-bg-color);

    font-size: 14px;
    list-style-type: none;
    overflow-y: auto;
    overflow-x: hidden;

    .select-item {
      padding: 10px;

      cursor: pointer;
      list-style-type: none;

      color: var(--primary-text-color);

      &:hover {
        background: var(--primary-button-color);
      }
    }

    &::-webkit-scrollbar {
      height: 5px;
      width: 5px;
    }

    &::-webkit-scrollbar-track {
      background: var(--secondary-bg-color);
      border: 1px solid var(--input-border-color);
      border-radius: 0 10px 10px 0;
    }

    &::-webkit-scrollbar-thumb {
      height: 4px;

      background: var(--secondary-text-color);
      border-radius: 10px;
    }
  }
}

.input-title {
  width: 516px;
  height: 43px;
}

.button {
  width: 116px;
}

.button-update {
  width: 184px;
}

@media screen and (max-width: 1050px) {
  .create-report-section {
    flex-direction: column;
  }
}
</style>
