<template>
  <form class="form" @submit.prevent="nextStep">
    <BaseInput
      v-model="alertName"
      label="Name*"
      placeholder="Alert name"
      class="input-name"
    />

    <BaseTextarea
      v-model="alertDescription"
      placeholder="Some words about Alert"
      label="Description"
    />
    <label>
      <span>Recipients' email addresses*</span>
      <AddUsersField
        :hasError="!!errors.usersEmailError"
        :errorMessage="errors.usersEmailError"
        :selectedUsers="selectedUsers"
        :usersEmails="usersEmails"
        class="alert-add-users"
        @select-user="selectUser"
        @remove-user="removeUser"
      />
    </label>

    <footer>
      <ButtonWithArrow
        type="submit"
        :is-disabled="!alertName"
        class="next-button"
      >
        <span>Next</span>
      </ButtonWithArrow>
    </footer>
  </form>
</template>

<script>
import {mapActions, mapState, mapGetters, createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'
import createAlertMixin from '@/lib/mixins/create-alerts.js'

import BaseInput from '@/components/common/BaseInput'
import BaseTextarea from '@/components/common/BaseTextarea'
import AddUsersField from '@/components/AddUsersField'

const {mapActions: mapActionsAlerts} = createNamespacedHelpers('alerts')

export default {
  name: 'CreateAlertName',
  components: {BaseInput, BaseTextarea, AddUsersField},
  mixins: [createAlertMixin],
  data() {
    return {
      alertName: '',
      alertDescription: '',
      selectedUsers: [],
      errors: {
        usersEmailError: null,
        alertName: null,
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
    this[action.CLEAR_NEW_ALERT]()
    this[action.GET_COMPANY_USERS](this.department.id)
  },
  methods: {
    ...mapActions([action.GET_COMPANY_USERS]),
    ...mapActionsAlerts([action.CLEAR_NEW_ALERT]),
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

      this[action.UPDATE_NEW_ALERT]({
        step: nextStep,
        title: this.alertName,
        description: this.alertDescription,
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
.form {
  display: flex;
  flex-direction: column;

  padding: 40px 0px;
  gap: 30px;

  width: 65%;

  @media (max-width: 1100px) {
    width: 100%;
  }
}
</style>
