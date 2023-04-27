<template>
  <div class="form-wrapper">
    <AccountAnalysisSourcesTabs />

    <BaseInput
      v-model="projectName"
      label="Name"
      placeholder="Project Name"
      class="input-name"
    />

    <BaseSelect v-model="profileHandle" />

    <footer class="create-reports__footer">
      <ButtonWithArrow :is-disabled="!projectName" @click="nextStep">
        <span>Save Project</span>
      </ButtonWithArrow>
    </footer>
  </div>
</template>

<script>
import {mapActions, mapGetters, mapState} from 'vuex'
import {action, get} from '@store/constants'
import createReportMixin from '@/lib/mixins/create-report.js'

import BaseInput from '@/components/common/BaseInput'
import BaseSelect from '../BaseSelect2.vue'
import AccountAnalysisSourcesTabs from '@/components/account-analysis/AccountAnalysisSourcesTabs'

export default {
  name: 'CreateAccountAnalysisProject',
  mixins: [createReportMixin],
  components: {
    BaseInput,
    BaseSelect,
    AccountAnalysisSourcesTabs,
  },
  data() {
    return {
      projectName: '',
      profileHandle: '',
      selectedUsers: [],
      errors: {
        usersEmailError: null,
        projectName: null,
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
      const nextStep = 2
      const nextStepName = this.getNextStepName(nextStep)

      this[action.UPDATE_NEW_REPORT]({
        step: nextStep,
        title: this.projectName,
        user: this.selectedUsers.map((user) => user.id),
        department: this.department?.id,
        creator: this.userInfo.id,
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

  width: 90%;
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
