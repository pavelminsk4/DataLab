<template>
  <div>
    <NavigationBar
      v-if="currentProject"
      :title="currentAlert?.title || currentProject?.title"
      hint="Set up alerts for your project with highly customized filters"
    >
      <BaseButton
        v-if="this.$route.name === 'NewAlert'"
        @click="saveChanges"
        class="button"
      >
        Save
      </BaseButton>
      <BaseButton
        v-if="this.$route.name === 'UpdateAlert'"
        @click="saveChanges"
        class="button"
      >
        Update Alert
      </BaseButton>
    </NavigationBar>

    <div class="create-alert-wrapper">
      <div class="title">Alert Title</div>

      <BaseInput
        v-model.trim="titleProxy"
        placeholder="Alert Title"
        :hasError="!!errors.titleError"
        :errorMessage="errors.titleError"
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

      <div class="additional-settings">
        <div>
          <div class="title">Trigger on every N new posts</div>
          <BaseInput
            v-model="triggerProxy"
            inputType="number"
            placeholder="Number"
            :hasError="!!errors.triggerError"
            :errorMessage="errors.triggerError"
            @blur="maskForNumber('triggerProxy')"
          >
            <div class="control-buttons">
              <button class="control-button">
                <ArrowDownIcon
                  @click="increase('triggerProxy')"
                  class="arrow-input arrow-increase"
                />
              </button>
              <button class="control-button">
                <ArrowDownIcon
                  @click="decrease('triggerProxy')"
                  class="arrow-input"
                />
              </button>
            </div>
          </BaseInput>
        </div>

        <div>
          <div class="title">How many posts to send</div>
          <BaseInput
            v-model="postsProxy"
            inputType="number"
            placeholder="Number"
            :hasError="!!errors.postsError"
            :errorMessage="errors.postsError"
            @blur="maskForNumber('postsProxy')"
          >
            <div class="control-buttons">
              <button class="control-button">
                <ArrowDownIcon
                  @click="increase('postsProxy')"
                  class="arrow-input arrow-increase"
                />
              </button>
              <button class="control-button">
                <ArrowDownIcon
                  @click="decrease('postsProxy')"
                  class="arrow-input"
                />
              </button>
            </div>
          </BaseInput>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import {isAllEmptyFields} from '@lib/utilities'

import AddUsersField from '@/components/AddUsersField'
import BaseInput from '@/components/common/BaseInput'
import BaseButton from '@/components/common/BaseButton'
import ArrowDownIcon from '@/components/icons/ArrowDownIcon'
import NavigationBar from '@/components/navigation/NavigationBar'

const MIN_NUMBER = 1
const MAX_NUMBER = 50

export default {
  name: 'AlertSettingsScreen',
  components: {
    AddUsersField,
    BaseInput,
    BaseButton,
    NavigationBar,
    ArrowDownIcon,
  },
  data() {
    return {
      title: null,
      email: '',
      trigger: null,
      posts: null,
      selectedUsers: [],
      usersId: [],
      errors: {
        titleError: null,
        triggerError: null,
        postsError: null,
        usersEmailError: null,
      },
    }
  },
  computed: {
    ...mapGetters({
      workspaces: get.WORKSPACES,
      loading: get.LOADING,
      alerts: get.ALERTS,
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
    workspaceMembers() {
      return this.currentWorkspace[0]?.members
    },
    currentProject() {
      return this.currentWorkspace[0]?.projects.filter(
        (el) => el.id === +this.projectId
      )[0]
    },
    alertId() {
      return this.$route.params.alertId
    },
    currentAlert() {
      return this.alerts.filter((el) => +el.id === +this.alertId)[0]
    },
    alertUsers() {
      return this.companyUsers
        .filter((i) => this.currentAlert?.user.includes(i.id))
        .concat(
          this.currentAlert?.user.filter((i) =>
            this.companyUsers.includes(i.id)
          )
        )
    },
    alertUsersId() {
      return this.alertUsers.map((el) => el.id)
    },
    companyUsersEmails() {
      return this.companyUsers.filter((el) => el.email)
    },
    titleProxy: {
      get() {
        if (this.title !== null) return this.title
        return this.currentAlert?.title || ''
      },
      set(val) {
        this.title = val
        if (val) this.errors.titleError = null
      },
    },
    triggerProxy: {
      get() {
        if (this.trigger !== null) return this.trigger
        return this.currentAlert?.triggered_on_every_n_new_posts || MIN_NUMBER
      },
      set(val) {
        this.trigger = val
        if (val) this.errors.triggerError = null
      },
    },
    postsProxy: {
      get() {
        if (this.posts !== null) return this.posts
        return this.currentAlert?.how_many_posts_to_send || MIN_NUMBER
      },
      set(val) {
        this.posts = val
        if (val) this.errors.postsError = null
      },
    },
  },
  async created() {
    if (!this.workspaces.length) {
      await this[action.GET_WORKSPACES]()
    }

    if (!this.alerts.length) {
      await this[action.GET_ALERTS](this.projectId)
    }

    await this[action.GET_COMPANY_USERS](
      this.currentUser?.user_profile?.department.id
    )

    if (this.$route.name === 'UpdateAlert') {
      this.selectedUsers = [...this.alertUsers]
      this.usersId = [...this.alertUsersId]
    }
  },
  methods: {
    ...mapActions([
      action.GET_WORKSPACES,
      action.CREATE_NEW_ALERT,
      action.UPDATE_ALERT,
      action.GET_ALERTS,
      action.GET_COMPANY_USERS,
    ]),
    async createAlert() {
      this[action.CREATE_NEW_ALERT]({
        data: {
          title: this.titleProxy,
          triggered_on_every_n_new_posts: +this.triggerProxy,
          how_many_posts_to_send: +this.postsProxy,
          alert_condition: '',
          project: this.projectId,
          user: [...this.usersId],
        },
        projectId: this.projectId,
      })

      await this[action.GET_ALERTS](this.projectId)
    },
    updateAlert() {
      this[action.UPDATE_ALERT]({
        data: {
          title: this.titleProxy,
          triggered_on_every_n_new_posts: +this.triggerProxy,
          how_many_posts_to_send: +this.postsProxy,
          alert_condition: '',
          project: this.projectId,
          user: [...this.usersId],
        },
        alertId: this.alertId,
      })
    },
    async saveChanges() {
      if (!this.validationForm()) return

      if (this.$route.name === 'NewAlert') {
        await this.createAlert()

        await this.$router.push({
          name: 'Alerts',
        })
      } else {
        this.updateAlert()

        await this.$router.push({
          name: 'Alerts',
        })
      }
    },
    validationForm() {
      const defaultErrorMessage = 'required'

      this.errors.titleError = this.titleProxy ? null : defaultErrorMessage

      this.errors.usersEmailError = this.selectedUsers.length
        ? null
        : defaultErrorMessage

      return isAllEmptyFields(this.errors)
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
    increase(val) {
      if (this[val] >= MAX_NUMBER) return
      this[val] = +this[val] + 1
    },
    decrease(val) {
      if (this[val] <= MIN_NUMBER) return
      this[val] = +this[val] - 1
    },
    maskForNumber(val) {
      if (+this[val] > MAX_NUMBER) {
        this[val] = MAX_NUMBER
      }
      if (+this[val] < MIN_NUMBER) {
        this[val] = MIN_NUMBER
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.create-alert-wrapper {
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

.button {
  width: 116px;
}
.control-buttons {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 3px;

  margin-right: 18px;

  cursor: pointer;

  .control-button {
    border: none;
    background-color: transparent;
    cursor: pointer;
  }

  .arrow-input {
    color: var(--typography-primary-color);

    &:hover {
      color: var(--button-primary-color);
    }
  }

  .arrow-increase {
    margin-left: 0.5px;
    transform: rotate(180deg);

    &:hover {
      color: var(--button-primary-color);
    }
  }
}

@keyframes shake {
  10%,
  90% {
    transform: scale(0.9) translate3d(-1px, 0, 0);
  }
  20%,
  80% {
    transform: scale(0.9) translate3d(2px, 0, 0);
  }
  30%,
  50%,
  70% {
    transform: scale(0.9) translate3d(-4px, 0, 0);
  }
  40%,
  60% {
    transform: scale(0.9) translate3d(4px, 0, 0);
  }
}
</style>
