<template>
  <div class="form-wrapper">
    <BaseInput
      v-model="reportName"
      label="Name"
      :hasError="!!errors.reportName"
      :errorMessage="errors.reportName"
      class="input-name"
    />

    <BaseTextarea
      v-model="reportDescription"
      placeholder="Some words about Report"
      label="Description"
    />

    <AddUsersField
      :hasError="!!errors.usersEmail"
      :errorMessage="errors.usersEmail"
      :selectedUsers="selectedUsers"
      :usersEmails="usersEmails"
      class="report-add-users"
      @select-user="selectUser"
      @remove-user="removeUser"
    />
    <footer class="create-reports__footer">
      <ButtonWithArrow
        :is-disabled="!reportName"
        class="next-button"
        @click="nextStep"
      >
        <span>Next</span>
      </ButtonWithArrow>
    </footer>
  </div>
</template>

<script>
import {mapActions, mapGetters, mapState} from 'vuex'
import {action, get} from '@store/constants'
import createReportMixin from '@/lib/mixins/create-report.js'
import {isAllFieldsEmpty} from '@lib/utilities'

import BaseInput from '@/components/common/BaseInput'
import BaseTextarea from '@/components/common/BaseTextarea'
import AddUsersField from '@/components/AddUsersField'

export default {
  name: 'CreateReportName',
  mixins: [createReportMixin],
  components: {
    BaseInput,
    BaseTextarea,
    AddUsersField,
  },
  data() {
    return {
      newReportName: '',
      reportDescription: '',
      selectedUsers: [],
      errors: {
        usersEmail: null,
        reportName: null,
      },
    }
  },
  computed: {
    ...mapState(['companyUsers', 'userInfo']),
    ...mapGetters({
      department: get.DEPARTMENT,
    }),
    usersEmails() {
      return this.companyUsers?.filter((el) => el.email) || []
    },
    reportName: {
      get() {
        return this.newReportName
      },
      set(val) {
        this.newReportName = val
        this.errors.reportName = null
      },
    },
  },
  created() {
    this[action.CLEAR_NEW_REPORT]()
    this[action.GET_COMPANY_USERS](this.department.id)
  },
  methods: {
    ...mapActions([action.CLEAR_NEW_REPORT, action.GET_COMPANY_USERS]),
    selectUser(user) {
      this.selectedUsers.push(user)
      this.errors.usersEmailError = null
    },
    removeUser(index) {
      this.selectedUsers.splice(index, 1)
    },
    nextStep() {
      if (!this.validationData()) return

      const nextStep = 2
      const nextStepName = this.getNextStepName(nextStep)

      this[action.UPDATE_NEW_REPORT]({
        step: nextStep,
        title: this.reportName,
        description: this.reportDescription,
        user: this.selectedUsers.map((user) => user.id),
        department: this.department?.id,
        creator: this.userInfo.id,
      })
      this.$router.push({name: nextStepName})
    },
    validationData() {
      const defaultErrorMessage = 'required'

      this.errors.reportName = this.reportName ? null : defaultErrorMessage
      this.errors.usersEmail = this.selectedUsers.length
        ? null
        : defaultErrorMessage

      return isAllFieldsEmpty(this.errors)
    },
  },
}
</script>

<style lang="scss" scoped>
.form-wrapper {
  display: flex;
  flex-direction: column;

  width: 56%;
  margin-top: 40px;
}

.input-name {
  margin-bottom: 32px;
}

.report-add-users {
  width: 100%;
  margin-top: 32px;
}
</style>
