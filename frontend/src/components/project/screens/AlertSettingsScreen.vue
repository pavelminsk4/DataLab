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
        @click="updateAlert"
        class="button"
      >
        Update Alert
      </BaseButton>
    </NavigationBar>

    <div class="create-alert-wrapper">
      <div class="title">Alert Title</div>

      <BaseInput v-model="title" placeholder="Alert Title" />

      <div class="title">Alert e-mail</div>

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

      <div class="additional-settings">
        <div>
          <div class="title">Trigger on every N new posts</div>
          <BaseInput v-model="trigger">
            <div class="arrows-wrapper">
              <ArrowDownIcon
                @click="increase('trigger')"
                class="arrow-input arrow-increase"
              />
              <ArrowDownIcon @click="decrease('trigger')" class="arrow-input" />
            </div>
          </BaseInput>
        </div>

        <div>
          <div class="title">How many posts to send</div>
          <BaseInput v-model="posts">
            <div class="arrows-wrapper">
              <ArrowDownIcon
                @click="increase('posts')"
                class="arrow-input arrow-increase"
              />
              <ArrowDownIcon @click="decrease('posts')" class="arrow-input" />
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
      title: '',
      email: '',
      trigger: '',
      posts: '',
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

    if (!this.alerts.length) {
      await this[action.GET_ALERTS](this.projectId)
    }

    if (this.$route.name === 'UpdateAlert') {
      this.title = this.currentAlert?.title
      this.trigger = this.currentAlert?.triggered_on_every_n_new_posts
      this.posts = this.currentAlert?.how_many_posts_to_send
    }

    if (this.projectMembers.length && this.$route.name === 'UpdateAlert') {
      this.selectedUsers = [...this.alertUsers]
      this.usersId = [...this.alertUsersId]
    }

    document.addEventListener('click', this.close)
  },
  computed: {
    ...mapGetters({
      workspaces: get.WORKSPACES,
      loading: get.LOADING,
      alerts: get.ALERTS,
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
    alertId() {
      return this.$route.params.alertId
    },
    currentAlert() {
      return this.alerts.filter((el) => +el.id === +this.alertId)[0]
    },
    alertUsers() {
      return this.projectMembers
        .filter((i) => this.currentAlert?.user.includes(i.id))
        .concat(
          this.currentAlert?.user.filter((i) =>
            this.projectMembers.includes(i.id)
          )
        )
    },
    alertUsersId() {
      return this.alertUsers.map((el) => el.id)
    },
  },
  methods: {
    ...mapActions([
      action.GET_WORKSPACES,
      action.CREATE_NEW_ALERT,
      action.UPDATE_NEW_ALERT,
      action.GET_ALERTS,
    ]),
    createAlert() {
      this[action.CREATE_NEW_ALERT]({
        title: this.title,
        triggered_on_every_n_new_posts: this.trigger,
        how_many_posts_to_send: this.posts,
        alert_condition: '',
        project: this.projectId,
        user: [...this.usersId],
      })
    },
    updateAlert() {
      this[action.UPDATE_NEW_ALERT]({
        data: {
          title: this.title,
          triggered_on_every_n_new_posts: this.trigger,
          how_many_posts_to_send: this.posts,
          alert_condition: '',
          project: this.projectId,
          user: [...this.usersId],
        },
        alertId: this.alertId,
      })
    },
    saveChanges() {
      if (this.$route.name === 'NewAlert') {
        this.createAlert()

        this.loading = true
        this[action.GET_ALERTS](this.projectId)

        this.loading = true
        this.$router.push({
          name: 'Alerts',
        })
      } else {
        this.updateAlert()

        this[action.GET_ALERTS](this.projectId)

        this.$router.push({
          name: 'Alerts',
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
    increase(val) {
      this[val] = this[val] + 1
    },
    decrease(val) {
      this[val] = this[val] - 1
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
.arrows-wrapper {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 3px;

  margin-right: 18px;

  cursor: pointer;

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
