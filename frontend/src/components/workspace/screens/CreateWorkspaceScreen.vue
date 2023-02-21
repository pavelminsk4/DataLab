<template>
  <MainLayoutTitleBlock
    title="The Workspace -"
    description="Create a new workspace on your Dashboard"
    :back-page="{
      name: 'main page',
      routName: 'Home',
    }"
  />

  <ProgressBar />

  <div class="form-wrapper">
    <h4 class="label">Name</h4>
    <BaseInput v-model="workspaceName" />

    <h4 class="label">Description</h4>
    <BaseTextarea
      v-model="workspaceDescription"
      placeholder="Some words about Workspace"
    />

    <BaseButton
      :is-disabled="!workspaceName"
      class="next-button"
      @click="nextStep"
    >
      <span>Next</span>
      <ArrowLeftIcon class="button-arrow-icon" />
    </BaseButton>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import ArrowLeftIcon from '@/components/icons/ArrowLeftIcon'
import BaseButton from '@/components/buttons/BaseButton'
import BaseInput from '@/components/BaseInput'
import BaseTextarea from '@/components/BaseTextarea'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import ProgressBar from '@/components/workspace/ProgressBar'

export default {
  name: 'CreateWorkspaceScreen',
  components: {
    ArrowLeftIcon,
    BaseButton,
    BaseInput,
    BaseTextarea,
    MainLayoutTitleBlock,
    ProgressBar,
  },
  data() {
    return {
      workspaceName: '',
      workspaceDescription: '',
    }
  },
  created() {
    this[action.CLEAR_STATE]()
  },
  computed: {
    ...mapGetters({
      user: get.USER_INFO,
    }),
    members() {
      return [this.user.id]
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
          title: this.workspaceName,
          description: this.workspaceDescription,
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
.form-wrapper {
  display: flex;
  flex-direction: column;

  width: 56%;
  margin-top: 40px;
}

.label {
  margin: 20px 0 4px;

  font-weight: 400;

  &:first-child {
    margin-top: 0;
  }
}

.next-button {
  align-self: flex-end;

  margin-top: 32px;

  .button-arrow-icon {
    margin-left: 10px;
    transform: rotate(180deg);
  }
}
</style>
