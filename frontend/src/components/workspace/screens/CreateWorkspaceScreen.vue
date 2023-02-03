<template>
  <NavigationBar
    :step="step"
    :title="'The Workspace'"
    :hint="'Create a new workspace on your Dashboard'"
    :is-active-button="!!title"
    @next-step="nextStep"
  />

  <div class="workspace-wrapper">
    <h4 class="project-name">Name</h4>
    <BaseInput v-model="title" class="input-field" />

    <h4 class="project-name">Description</h4>
    <textarea
      class="description-field scroll"
      v-model="description"
      placeholder="Some words about Workspace"
    />
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import BaseInput from '@/components/BaseInput'
import NavigationBar from '@/components/navigation/NavigationBar'

export default {
  name: 'CreateWorkspaceScreen',
  components: {NavigationBar, BaseInput},
  component: {
    BaseInput,
  },

  data() {
    return {
      title: '',
      description: '',
    }
  },
  created() {
    this[action.CLEAR_STATE]()
  },
  computed: {
    ...mapGetters({
      user: get.USER_INFO,
    }),
    step() {
      return this.$route.name
    },
    members() {
      let members = []
      members.push(this.user.id)
      return members
    },
  },
  methods: {
    ...mapActions([
      action.UPDATE_NEW_WORKSPACE,
      action.UPDATE_CURRENT_STEP,
      action.CLEAR_STATE,
    ]),
    nextStep() {
      try {
        this[action.UPDATE_CURRENT_STEP]('Step2')
        this[action.UPDATE_NEW_WORKSPACE]({
          title: this.title,
          description: this.description,
          members: this.members,
          department: this.user.user_profile.department.id,
        })
        this.$router.push({
          name: 'Step2',
        })
      } catch (e) {
        console.log(e)
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.workspace-wrapper {
  display: flex;
  flex-direction: column;

  margin-top: 40px;
}

.project-name {
  margin: 25px 0 12px;

  font-size: 14px;

  color: var(--primary-text-color);

  &:first-child {
    margin-top: 0;
  }
}

.description-field {
  width: 475px;
  height: 132px;
  padding: 12px 16px;

  border: 1px solid var(--input-border-color);
  box-shadow: 0 4px 10px rgba(16, 16, 16, 0.25);
  border-radius: 10px;
  background: var(--secondary-bg-color);

  color: var(--primary-text-color);

  resize: none;
}

.description-field::placeholder {
  color: var(--typography-secondary-color);
}
</style>
