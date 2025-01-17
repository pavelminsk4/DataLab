<template>
  <MainLayoutTitleBlock
    title="The Workspace -"
    description="Create a new workspace on your Dashboard"
    :back-page="{
      name: 'main page',
      routeName: `${moduleName}Home`,
    }"
  />

  <ProgressBar />

  <div class="form-wrapper">
    <BaseInput v-model="workspaceName" label="Name" />

    <BaseTextarea
      v-model="workspaceDescription"
      label="Description"
      placeholder="Some words about Workspace"
    />

    <BaseButton
      :is-disabled="!workspaceName"
      class="next-button"
      @click="nextStep"
    >
      <CustomText tag="span" text="Next" />
      <ArrowLeftIcon class="button-arrow-icon" />
    </BaseButton>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import ArrowLeftIcon from '@components/icons/ArrowLeftIcon'
import BaseButton from '@components/common/BaseButton'
import BaseInput from '@components/common/BaseInput'
import BaseTextarea from '@components/common/BaseTextarea'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import ProgressBar from '@components/workspace/WorkspaceProgressBar'
import CustomText from '@components/CustomText'

export default {
  name: 'CreateWorkspaceScreen',
  components: {
    ArrowLeftIcon,
    BaseButton,
    BaseInput,
    BaseTextarea,
    MainLayoutTitleBlock,
    ProgressBar,
    CustomText,
  },
  props: {
    moduleName: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      workspaceName: '',
      workspaceDescription: '',
    }
  },
  computed: {
    ...mapGetters({
      user: get.USER_INFO,
    }),
    members() {
      return [this.user.id]
    },
    routeName() {
      return this.$route.name
    },
  },
  created() {
    this[action.CLEAR_STATE]()
  },
  methods: {
    ...mapActions([
      action.UPDATE_NEW_WORKSPACE,
      action.UPDATE_CURRENT_STEP,
      action.CLEAR_STATE,
    ]),
    nextStep() {
      const nextStep = this.routeName.replace(/\d/g, '2')
      try {
        this[action.UPDATE_CURRENT_STEP](nextStep)
        this[action.UPDATE_NEW_WORKSPACE]({
          title: this.workspaceName,
          description: this.workspaceDescription,
          members: this.members,
          department: this.user.user_profile.department.id,
        })
        this.$router.push({name: nextStep})
      } catch (e) {
        console.error(e)
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.form-wrapper {
  display: flex;
  flex-direction: column;

  width: 75%;
  margin-top: 40px;
  gap: 25px;
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

  .button-arrow-icon {
    margin-left: 10px;
    transform: rotate(180deg);
  }
}
</style>
