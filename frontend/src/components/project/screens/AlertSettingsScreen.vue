<template>
  <NavigationBar
    v-if="projectId"
    :title="currentProject.title"
    hint="Set up alerts for your project with highly customized filters"
  >
    <BaseButton @click="createAlert" class="button"> Save </BaseButton>
  </NavigationBar>

  <div class="create-alert-wrapper">
    <div class="title">Alert Title</div>

    <BaseInput :model-value="title" placeholder="Alert Title" />

    <div class="title">Alert e-mail</div>

    <BaseInput v-model="email" />

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
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseButton from '@/components/buttons/BaseButton'
import NavigationBar from '@/components/navigation/NavigationBar'
import BaseInput from '@/components/BaseInput'
import ArrowDownIcon from '@/components/icons/ArrowDownIcon'

export default {
  name: 'AlertSettingsScreen',
  components: {ArrowDownIcon, BaseInput, BaseButton, NavigationBar},
  data() {
    return {
      title: '',
      email: '',
      trigger: '',
      posts: '',
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
  },
  computed: {
    ...mapGetters({
      workspaces: get.WORKSPACES,
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
  },
  methods: {
    ...mapActions([
      action.GET_WORKSPACES,
      action.CREATE_NEW_ALERT,
      action.GET_ALERTS,
    ]),
    createAlert() {
      this[action.CREATE_NEW_ALERT]({
        title: this.title,
        triggered_on_every_n_new_posts: this.trigger,
        how_many_posts_to_send: this.posts,
        alert_condition: '',
        project: this.projectId,
        user: [...this.currentProject.members],
      })

      this.$router.push({
        name: 'Alerts',
      })
    },
    increase(val) {
      this[val] = this[val] + 1
    },
    decrease(val) {
      this[val] = this[val] - 1
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
</style>
