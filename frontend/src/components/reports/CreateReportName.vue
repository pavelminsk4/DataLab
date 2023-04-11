<template>
  <div class="form-wrapper">
    <BaseInput v-model="reportName" label="Name" class="input-name" />

    <BaseTextarea
      v-model="reportDescription"
      placeholder="Some words about Workspace"
      label="Description"
    />

    <AddUsersField
      :hasError="!!errors.usersEmailError"
      :errorMessage="errors.usersEmailError"
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
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import createReportMixin from '@/lib/mixins/create-report.js'

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
      reportName: '',
      reportDescription: '',
      selectedUsers: [],
      errors: {
        usersEmailError: null,
        reportName: null,
      },
    }
  },
  computed: {
    ...mapGetters({
      // change
      user: get.USER_INFO,
    }),
    users() {
      //change
      return []
    },
    usersEmails() {
      return this.users.filter((el) => el.email) || []
    },
  },
  created() {
    this[action.CLEAR_NEW_REPORT]()
  },
  methods: {
    ...mapActions([action.CLEAR_NEW_REPORT]),
    selectUser(user) {
      this.selectedUsers.push(user)
      this.errors.usersEmailError = null
    },
    removeUser(index) {
      this.selectedUsers.splice(index, 1)
    },
    nextStep() {
      const nextStep = 2
      const nextStepName = this.getNextStepName(nextStep)

      this[action.UPDATE_NEW_REPORT]({
        step: nextStep,
        title: this.reportName,
        description: this.reportDescription,
        users: this.selectedUsers,
        department: this.user.user_profile.department.id,
      })
      this.$router.push({name: nextStepName})
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
  margin-top: 32px;
}
</style>
