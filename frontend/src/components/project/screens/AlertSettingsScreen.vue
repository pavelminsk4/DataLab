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
        v-model="titleProxy"
        placeholder="Alert Title"
        :isError="!!errorTitle"
        :errorMessage="errorTitle"
      />

      <div class="title">Recipient's email</div>

      <div class="email-wrapper">
        <div :class="['email-field scroll', visible && 'active-email-field']">
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

        <ul v-if="visible" class="select-list scroll">
          <li
            v-for="(item, index) in companyUsersEmails"
            :key="item.username + index"
            class="select-item"
            @click="select(item)"
          >
            {{ item.email }}
          </li>
        </ul>
      </div>

      <div class="additional-settings">
        <div>
          <div class="title">Trigger on every N new posts</div>
          <BaseInput
            v-model="triggerProxy"
            inputType="number"
            placeholder="Number"
            :isError="!!errorTrigger"
            :errorMessage="errorTrigger"
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
            :isError="!!errorPosts"
            :errorMessage="errorPosts"
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

import BaseInput from '@/components/BaseInput'
import BaseButton from '@/components/buttons/BaseButton'
import ArrowDownIcon from '@/components/icons/ArrowDownIcon'
import NavigationBar from '@/components/navigation/NavigationBar'
import DeleteTagButton from '@/components/icons/DeleteTagButton'
import AddButtonIcon from '@/components/icons/AddButtonIcon'

export default {
  name: 'AlertSettingsScreen',
  components: {
    AddButtonIcon,
    DeleteTagButton,
    BaseInput,
    BaseButton,
    NavigationBar,
    ArrowDownIcon,
  },
  data() {
    return {
      title: null,
      errorTitle: null,
      email: '',
      trigger: null,
      errorTrigger: null,
      posts: null,
      errorPosts: null,
      visible: false,
      isDuplicate: false,
      selectedUsers: [],
      usersId: [],
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
        if (val) this.errorTitle = null
      },
    },
    triggerProxy: {
      get() {
        if (this.trigger !== null) return this.trigger
        return this.currentAlert?.triggered_on_every_n_new_posts || ''
      },
      set(val) {
        this.trigger = val
        if (val) this.errorTrigger = null
      },
    },
    postsProxy: {
      get() {
        if (this.posts !== null) return this.posts
        return this.currentAlert?.how_many_posts_to_send || ''
      },
      set(val) {
        this.posts = val
        if (val) this.errorPosts = null
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

    document.addEventListener('click', this.close)
  },
  unmounted() {
    document.removeEventListener('click', this.close)
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
        title: this.titleProxy,
        triggered_on_every_n_new_posts: +this.triggerProxy,
        how_many_posts_to_send: +this.postsProxy,
        alert_condition: '',
        project: this.projectId,
        user: [...this.usersId],
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
      this.errorTitle = this.titleProxy ? null : 'wrong title'
      this.errorTrigger = this.validationNumberInput(this.triggerProxy)
        ? null
        : 'wrong number'
      this.errorPosts = this.validationNumberInput(this.postsProxy)
        ? null
        : 'wrong number'

      return !this.errorTitle && !this.errorTrigger && !this.errorPosts
    },
    addUsers() {
      this.visible = !this.visible
    },
    validationNumberInput(value) {
      if (typeof value === 'number' || value) {
        return value >= 0
      } else {
        return false
      }
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
    increase(val) {
      this[val] = +this[val] + 1
    },
    decrease(val) {
      this[val] = +this[val] - 1
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
.create-alert-wrapper {
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
    color: var(--primary-text-color);

    &:hover {
      color: var(--primary-button-color);
    }
  }

  .arrow-increase {
    margin-left: 0.5px;
    transform: rotate(180deg);

    &:hover {
      color: var(--primary-button-color);
    }
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
