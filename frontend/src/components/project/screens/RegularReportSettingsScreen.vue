<template>
  <div>
    <NavigationBar
      v-if="currentProject"
      :title="currentReport?.title || currentProject?.title"
      hint="Set up report for your project with highly customized filters"
    >
      <BaseButton
        v-if="routerName === 'NewRegularReport'"
        @click="saveChanges"
        class="button"
      >
        Save
      </BaseButton>
      <BaseButton
        v-if="routerName === 'UpdateRegularReport'"
        @click="saveChanges"
        class="button-update"
      >
        Update Regular Report
      </BaseButton>
    </NavigationBar>

    <section
      v-if="regularReports.length || $route.name === 'NewRegularReport'"
      class="create-report-section"
    >
      <div class="create-report-wrapper">
        <div class="title">Regular Report Title</div>
        <BaseInput
          v-model.trim="reportData.title"
          :hasError="!!errors.titleError"
          :errorMessage="errors.titleError"
          class="input-title"
          placeholder="Title"
          @blur="validationTitle"
        />

        <div class="title">Recipient's email</div>

        <AddUsersField
          :hasError="!!errors.usersEmailError"
          :errorMessage="errors.usersEmailError"
          :selectedUsers="selectedUsers"
          :usersEmails="companyUsersEmails"
          @select-user="selectUser"
          @remove-user="removeUser"
        />
      </div>
      <DivWithError
        :hasError="!!errors.reportTypeError"
        :errorMessage="errors.reportTypeError"
        class="time-picker-error-wrapper"
      >
        <TimePickerReports
          :regularReport="currentReport"
          :reportSettingsError="errors.reportSettingsError"
          @update-values="updateTimePickerValues"
          @update-time="updateTime"
          @update-report-settings-error="updateReportSettingsError"
        />
      </DivWithError>
    </section>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import {isAllEmptyFields} from '@lib/utilities'

import AddUsersField from '@/components/AddUsersField'
import BaseButton from '@/components/buttons/BaseButton'
import BaseInput from '@/components/BaseInput'
import DivWithError from '@/components/DivWithError.vue'
import NavigationBar from '@/components/navigation/NavigationBar'
import TimePickerReports from '@/components/project/screens/TimePickerReports'

const DEFAULT_ERROR_MESSAGE = 'required'

export default {
  name: 'RegularReportSettingsScreen',
  components: {
    AddUsersField,
    BaseButton,
    BaseInput,
    DivWithError,
    NavigationBar,
    TimePickerReports,
  },
  data() {
    return {
      reportData: {
        title: '',
      },
      errors: {
        titleError: null,
        usersEmailError: null,
        reportTypeError: null,
        reportSettingsError: {
          h_template: null,
          d_template: null,
          w_template: null,
          m_template: null,
          w_day_of_week: null,
        },
      },
      selectedUsers: [],
      usersId: [],
    }
  },
  computed: {
    ...mapGetters({
      workspaces: get.WORKSPACES,
      loading: get.LOADING,
      regularReports: get.REGULAR_REPORTS,
      currentUser: get.USER_INFO,
      companyUsers: get.COMPANY_USERS,
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
    currentProject() {
      return this.currentWorkspace[0]?.projects.filter(
        (el) => el.id === +this.projectId
      )[0]
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
      return this.companyUsers
        .filter((i) => this.currentReport?.user.includes(i.id))
        .concat(
          this.currentReport?.user.filter((i) =>
            this.companyUsers.includes(i.id)
          )
        )
    },
    reportUsersId() {
      return this.reportUsers.map((el) => el.id)
    },
    routerName() {
      return this.$route.name
    },
    companyUsersEmails() {
      return this.companyUsers.filter((el) => el.email) || []
    },
  },
  async created() {
    if (!this.workspaces.length) {
      await this[action.GET_WORKSPACES]()
    }

    if (!this.regularReports.length) {
      await this[action.GET_REGULAR_REPORTS](this.projectId)
    }

    if (this.routerName === 'UpdateRegularReport') {
      this.reportData = this.currentReport
    }

    await this[action.GET_COMPANY_USERS](
      this.currentUser?.user_profile?.department.id
    )

    if (this.routerName === 'UpdateRegularReport') {
      this.selectedUsers = [...this.reportUsers]
      this.usersId = [...this.reportUsersId]
    }
  },
  methods: {
    ...mapActions([
      action.GET_WORKSPACES,
      action.CREATE_NEW_REGULAR_REPORT,
      action.UPDATE_REGULAR_REPORT,
      action.GET_REGULAR_REPORTS,
      action.GET_COMPANY_USERS,
      action.GET_USER_INFORMATION,
    ]),
    updateTimePickerValues(name, value) {
      if (this.errors.reportTypeError) {
        this.errors.reportTypeError = null
      }

      this.reportData[name] = value
    },
    updateTime(type, val) {
      this.reportData[`${type}_hour`] = val.hours
      this.reportData[`${type}_minute`] = val.minutes
    },
    updateReportSettingsError(name) {
      this.errors.reportSettingsError[name] = null
    },
    createRegularReport() {
      this[action.CREATE_NEW_REGULAR_REPORT]({
        projectId: this.projectId,
        data: {
          ...this.reportData,
          project: this.projectId,
          user: [...this.usersId],
        },
      })
    },
    updateRegularReport() {
      this[action.UPDATE_REGULAR_REPORT]({
        projectId: this.projectId,
        regularReportId: this.$route.params.regularReportId,
        data: {
          ...this.reportData,
          project: this.projectId,
          user: [...this.usersId],
        },
      })
    },
    saveChanges() {
      if (!this.validation()) return

      if (this.routerName === 'NewRegularReport') {
        this.createRegularReport()
      }

      if (this.routerName === 'UpdateRegularReport') {
        this.updateRegularReport()
      }

      this.$router.push({
        name: 'Reports',
      })
    },
    selectUser(item) {
      this.usersId.push(item.id)
      this.selectedUsers.push(item)
      this.errors.usersEmailError = null
    },
    removeUser(index) {
      this.selectedUsers.splice(index, 1)
      this.usersId.splice(index, 1)
    },
    validationTitle() {
      this.errors.titleError = this.reportData.title
        ? null
        : DEFAULT_ERROR_MESSAGE
    },
    validation() {
      this.validationTitle()

      this.errors.titleError = this.reportData.title
        ? null
        : DEFAULT_ERROR_MESSAGE
      this.errors.usersEmailError = this.selectedUsers.length
        ? null
        : DEFAULT_ERROR_MESSAGE

      const isSelectedReportType =
        this.reportData.hourly_enabled ||
        this.reportData.daily_enabled ||
        this.reportData.weekly_enabled ||
        this.reportData.monthly_enabled
      this.errors.reportTypeError = isSelectedReportType
        ? null
        : DEFAULT_ERROR_MESSAGE

      if (this.reportData.hourly_enabled) {
        this.errors.reportSettingsError.h_template = this.reportData.h_template
          ? null
          : DEFAULT_ERROR_MESSAGE
      }
      if (this.reportData.daily_enabled) {
        this.errors.reportSettingsError.d_template = this.reportData.d_template
          ? null
          : DEFAULT_ERROR_MESSAGE
      }
      if (this.reportData.weekly_enabled) {
        this.errors.reportSettingsError.w_template = this.reportData.w_template
          ? null
          : DEFAULT_ERROR_MESSAGE

        this.errors.reportSettingsError.w_day_of_week = this.reportData
          .w_day_of_week
          ? null
          : DEFAULT_ERROR_MESSAGE
      }
      if (this.reportData.monthly_enabled) {
        this.errors.reportSettingsError.m_template = this.reportData.m_template
          ? null
          : DEFAULT_ERROR_MESSAGE
      }

      return isAllEmptyFields(this.errors)
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
    color: var(--typography-primary-color);
  }

  .additional-settings {
    display: flex;
    gap: 20px;
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

.time-picker-error-wrapper {
  --error-top: 5px;
  width: 100%;
  padding-top: 20px;
  margin-top: -20px;

  border-radius: 15px;
}
</style>
